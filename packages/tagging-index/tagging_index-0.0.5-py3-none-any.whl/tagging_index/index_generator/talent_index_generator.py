from .common_index_generator import (
    CommonIndexGenerator,
    SourceTable,
    TagSourceTable,
    TagIndexConfig,
)


class TalentIndexGenerator(CommonIndexGenerator):

    def __init__(self, tag_idx_def_file: str):
        source_table = SourceTable(
            "dwd_cn_lst_com_pos_linkedin",
            "full_stock_id",
            "lst_com",
            "user_id",
            "start_year",
            "end_year",
            "end_year>2000",
        )
        # 不再使用hire_year, dismiss_year, 和total保持一致
        tag_source_table = TagSourceTable(
            "dwd_tag_lst_com_linkedin_position_skill",
            "full_stock_id",
            "lst_com",
            "user_id",
            "substr(startdate,1,4)",
            "substr(enddate,1,4)",
        )
        tag_idx_cfg: TagIndexConfig = TagIndexConfig(
            "talent", "T", tag_source_table, source_table
        )
        super().__init__(tag_idx_def_file, tag_idx_cfg)
