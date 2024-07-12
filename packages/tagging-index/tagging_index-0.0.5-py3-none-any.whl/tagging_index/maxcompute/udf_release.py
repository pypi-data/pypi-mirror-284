import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
import importlib.util

from tagging_index._udf.tag_matcher import TagMatcher
from tagging_index._udf.tag_converter import TagConverter
from data2cloud.cloud.maxcompute import MaxcomputeSetup

# 文件和版本变量
RES_FILES = {
    "tagging_index._udf.udf_match_tag": "UDF_MATCH_TAG_VERSION",
    "tagging_index._udf.tag_converter": "TAG_CONVERTER_VERSION",
    "tagging_index._udf.tag_matcher": "TAG_MATCHER_VERSION",
}
MAIN_FILE = "udf_match_tag"
DIM_RES_NAME = "res_dim_tag_new"


class UdfRelease:
    def __init__(self):
        self.o = MaxcomputeSetup().default_odps
        self.config_file = ""
        self.matcher = TagMatcher()

    def release_udf(self):
        self._update_py_res()
        updated_files = self._check_res_update()
        self.version = self._update_main_file(updated_files)
        return self.version

    def _read_file_and_version(self, filename, version_info=True):
        if not self.o.exist_resource(filename):
            return "", 0
        with self.o.open_resource(filename, mode="r") as fp:
            content = fp.read()
            version_line = content.split("\n")[0]
            version = int(version_line.split("=")[1]) if version_info else 0  # type: ignore
            return (content if not version_info else content.split("\n", 1)[1], version)

    def _check_res_update(self):
        updated_files = {}
        for module, version_var in RES_FILES.items():
            filename = module.split(".")[-1]
            original_content = read_module_source(module)
            release_file = f"{filename}_release.py"
            release_content, release_version = self._read_file_and_version(release_file)

            # 检查发布文件是否存在，以及内容是否有更新
            if (
                not self.o.exist_resource(release_file)
                or original_content != release_content
            ):
                new_version = release_version + 1 if release_version else 1
                updated_content = f"{version_var}={new_version}\n" + original_content
                updated_files[filename] = {
                    "content": updated_content,
                    "version": new_version,
                    "updated": True,
                }
                # 更新版本文件和发布文件
                versioned_filename = f"{filename}_v{new_version}.py"
                self.o.create_resource(
                    versioned_filename, "py", file_obj=updated_content
                )
                if self.o.exist_resource(release_file):
                    self.o.delete_resource(release_file)
                self.o.create_resource(release_file, "py", file_obj=updated_content)
                print(
                    f"...Updated {filename} to version {new_version} and refreshed {release_file}"
                )
            else:
                updated_files[filename] = {
                    "content": original_content,
                    "version": release_version,
                    "updated": False,
                }
        return updated_files

    def _update_main_file(self, updated_files: Dict[str, Any]):
        main_file = f"{MAIN_FILE}_main.py"  # 发布文件名
        res_versions = ";".join(
            [f"{k}:{v['version']}" for k, v in updated_files.items()]
        )
        main_version = "udf" + "@".join(
            [str(v["version"]) for k, v in updated_files.items()]
        )
        udf_version = main_version
        if any(f["updated"] for f in updated_files.values()):
            # 构建包含所有资源文件版本号的字符串
            version_lines = f"UDF_VERSION='{udf_version}' # {res_versions} \n"
            print(version_lines)
            main_content = updated_files[MAIN_FILE]["content"]
            # 更新主文件内容
            new_release_content = version_lines + "\n" + main_content
            if self.o.exist_resource(main_file):
                self.o.delete_resource(main_file)
            self.o.create_resource(
                main_file,
                "py",
                file_obj=new_release_content,
                comment=f"Updated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            )
            print(
                f"...Updated {main_file} with new UDF version({udf_version}) and resources' versions."
            )
        else:
            print(
                f"...No significant updates detected; main file update skipped. current version: {main_version}"
            )
        return udf_version

    def create_udf_function(self, updated_files: Dict[str, Any]):
        if not self.o.exist_function("udf_match_tag"):
            resources = [
                f"{f if f!=MAIN_FILE else f'{MAIN_FILE}_main'}.py"
                for f in updated_files.keys()
            ]
            resources.append(DIM_RES_NAME)
            self.o.create_function(
                "udf_match_tag",
                class_type=f"{MAIN_FILE}_main.match_tag",
                resources=resources,
            )

    def update_dim_resource(
        self, dim_table="dim_digitalization_tag", version: str = ""
    ):
        """update dim resouce to assigned version, or use latest version if version is ""
        Args:
            version (str, optional): udf version. Defaults to "".
        """

        version_cond = f'"{version}"' if version else f'max_pt("{dim_table}")'
        res_table = "dim_digital_tag_resource_new"
        sql_drop_res_table = f"drop table if exists {res_table};"
        sql_res_create = f"""
            create table {res_table} as 
            -- 不支持复杂类型, 不支持分区
            select tag,
            tag_level,
            to_json(prefix) prefix,
            is_keyword,
            to_json(suffix) suffix,
            language,
            category,
            data_cycle,
            data_phase,
            to_json(parent_tags) parent_tags,
            tag_version from {dim_table} where tag_version={version_cond} ;
        """
        self.o.execute_sql(sql_drop_res_table, hints={"odps.sql.submit.mode": "script"})
        self.o.execute_sql(sql_res_create, hints={"odps.sql.submit.mode": "script"})
        res = self.o.get_resource(DIM_RES_NAME)
        res.update(table_name=res_table)
        print(f"...{res_table}->{DIM_RES_NAME} updated")

    def _update_py_res(self):
        # 本地上传udf相关py资源
        udf_res_dir = f"{Path(__file__).resolve().parent.parent}/udf"
        for module, version_var in RES_FILES.items():
            filename = module.split(".")[-1]
            source_code = read_module_source(module)
            print(f"...updating resource {filename}.py")
            if self.o.exist_resource(f"{filename}.py"):
                self.o.delete_resource(f"{filename}.py")
            self.o.create_resource(f"{filename}.py", "py", fileobj=source_code)

    def test_udf(
        self,
        contents: List[str],
        return_type,
        tag_range: Optional[List[str]] = None,
        alias_dim_table="",
    ):
        """use assigned dim_version to test udf, if version="", use the current dim resource

        Args:
            alias_dim_table (str, optional): tag dim table for alias resource. Defaults to "" to use current resource
        """

        if tag_range is not None:
            tag_range_list = ",".join(f"'{t}'" for t in tag_range)
            tag_range_param = f"Array({tag_range_list})"
        else:
            tag_range_param = "null"
        content_values = [f'("{c}")' for c in contents]
        content_table = f"select * from values {','.join(content_values)} as a(content)"
        sql_udf_test = f"""select content
            ,udf_match_tag(content,{return_type},{tag_range_param}) as result 
            from ({content_table})"""
        if alias_dim_table:
            alias_name = "res_dim_tag_alias"
            if self.o.exist_resource(alias_name):
                table_resource = self.o.get_resource(alias_name)
                table_resource.update(table_name=alias_dim_table)
            else:
                self.o.create_resource(
                    alias_name, "table", table_name=alias_dim_table, temp=True
                )
            sql_instantance = self.o.execute_sql(
                sql_udf_test,
                aliases={DIM_RES_NAME: alias_name},
                hints={"odps.sql.python.version": "cp37"},
            )
        else:
            sql_instantance = self.o.execute_sql(
                sql_udf_test,
                hints={"odps.sql.python.version": "cp37"},
            )
        df = sql_instantance.open_reader().to_pandas()
        # result = df.to_dict(orient="records")
        return df

    def test_local(
        self,
        contents: Dict[str, str],
        return_type,
        tag_range: List[str] = [],
        dim_tag_config="",
    ):
        """_summary_

        Args:
            contents (List[str]): _description_
            return_type (_type_): _description_
            tag_range (List[str], optional): _description_. Defaults to [].
            dim_tag_config (str, optional): config file  Defaults to "" to use default config file.

        Returns:
            _type_: _description_
        """
        current_file = Path(__file__).resolve()
        config_file = (
            f"{current_file.parent.parent.parent}/tag_data/output/new_config_validated.json"
            if dim_tag_config == ""
            else dim_tag_config
        )
        if self.config_file != config_file:
            self.config_file = config_file
            conv = TagConverter()
            tag_config = conv.dict_to_config(json.load(open(self.config_file)))
            self.matcher.load_tags(tag_config)
        match_results = {
            k: self.matcher.match_result(contents[k], return_type, tag_range)
            for k in contents
        }
        return match_results


def read_module_source(module_name):
    # 获取模块的规范（spec）对象
    spec = importlib.util.find_spec(module_name)

    if spec is None or spec.origin is None:
        raise ImportError(f"Module {module_name} not found.")

    # 从规范对象中获取模块文件的实际路径
    module_file_path = spec.origin

    # 使用with语句打开并读取模块文件的内容
    with open(module_file_path, "r", encoding="utf-8") as file:
        source_code = file.read()

    return source_code
