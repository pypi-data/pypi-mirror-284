from idi_model._1_input_data_manager.data_aggregate import (
    aggregate_projected_quarterly_cohort_level,
)
from idi_model.tools.df_tools.extract_infos import extract_quarter_year


def quarterly_projected_cohort_level(
    df_monthly_policy_level, list_projected_columns_final
):
    df_monthly_policy_level = extract_quarter_year(
        df_monthly_policy_level,
        "Proj_Month",
        "proj_year",
        "quarter_proj_index",
    )
    resulted_df_quarter_cohort_level = (
        aggregate_projected_quarterly_cohort_level(
            df_monthly_policy_level,
            ["Cohort", "proj_year", "quarter_proj_index"],
            list_projected_columns_final,
        )
    )

    return resulted_df_quarter_cohort_level
