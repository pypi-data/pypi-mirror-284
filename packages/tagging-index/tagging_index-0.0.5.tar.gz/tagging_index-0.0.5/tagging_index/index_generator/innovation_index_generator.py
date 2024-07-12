from .common_index_generator import (
    CommonIndexGenerator,
    SourceTable,
    TagIndexConfig,
    TagSourceTable,
)


class InnovationIndexGenerator(CommonIndexGenerator):
    def __init__(self, tag_idx_def_file: str):
        table_name = """ (
        with app_no as (
            SELECT distinct application_no
            ,SUBSTR(application_date,1,4) AS application_year from dwd_patent_desc 
            WHERE   pt = MAX_PT ('dwd_patent_desc') 
            and nullif(content,'') is not null
        )
        ,entity as (
            select distinct application_no,ic_usc_code as social_credit_code
            from dwd_patent_entity 
        LATERAL VIEW EXPLODE(ic_usc_codes) tmp AS ic_usc_code 
        where pt = MAX_PT('dwd_patent_entity') and ic_usc_code <>""
        )
        select social_credit_code as source_comp_id
                    ,a.application_no as entity_id
                    ,application_year as start_year
                    ,application_year as end_year
                    ,'total' as tag_udf_version
                    from app_no a join entity b on a.application_no=b.application_no
            )
        """
        source_table = SourceTable(table_name, comp_type="usc_com")
        tag_source_table = TagSourceTable(
            "dwd_tag_patent_china",
            "social_credit_code",
            "usc_com",
            "application_no",
            "application_year",
            "application_year",
        )
        tag_idx_cfg: TagIndexConfig = TagIndexConfig(
            "innovation", "I", tag_source_table, source_table
        )
        super().__init__(tag_idx_def_file, tag_idx_cfg)
