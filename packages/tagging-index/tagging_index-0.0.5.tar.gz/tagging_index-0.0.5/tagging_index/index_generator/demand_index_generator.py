from .common_index_generator import (
    CommonIndexGenerator,
    SourceTable,
    TagSourceTable,
    TagIndexConfig,
)


class DemandIndexGenerator(CommonIndexGenerator):
    def __init__(self, tag_idx_def_file: str):
        source_table = SourceTable(
            "dwd_scc_com_job_posting",
            "social_credit_code",
            "usc_com",
            "job_id",
            "pt",
            "pt",
            "pt>'2015'",
        )
        tag_source_table = TagSourceTable(
            "dwd_tag_scc_com_job_posting",
            "social_credit_code",
            "usc_com",
            "job_id",
            "activity_year",
            "activity_year",
        )
        tag_idx_cfg: TagIndexConfig = TagIndexConfig(
            "demand", "D", tag_source_table, source_table
        )
        super().__init__(tag_idx_def_file, tag_idx_cfg)
