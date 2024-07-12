from arope_universal_life.universal_life_module import universal_life
from arope_universal_life.abstracted_packages import furtheredge_pandas as pd

dict_month_to_quarter = {
    "1": "1",
    "2": "1",
    "3": "1",
    "4": "2",
    "5": "2",
    "6": "2",
    "7": "3",
    "8": "3",
    "9": "3",
    "10": "4",
    "11": "4",
    "12": "4",
}


def extract_cohort(issue_date):
    year = issue_date.year
    quarter = (issue_date.month - 1) // 3 + 1
    return f"{year}Q{quarter}"


def arope_model_workflow(
    policies,
    ri_rates,
    wop_rates,
    tech_assumptions,
    product,
    proj_columns,
    non_proj_columns,
    run_settings,
    columns_to_aggregate,
):

    (
        proj_result_universal_life,
        non_proj_result_universal_life,
        not_found_columns,
    ) = universal_life(
        policies,
        ri_rates,
        wop_rates,
        tech_assumptions,
        product,
        False,
        "outputs/model_points.csv",
        proj_columns,
        non_proj_columns,
        run_settings,
        chuck_size=-10,
        projection_points=700,
        show_excecution_time=True,
    )
    proj_result_universal_life["inception_date"] = pd.to_datetime(
        proj_result_universal_life["inception_date"]
    )
    proj_result_universal_life["proj_date"] = pd.to_datetime(
        proj_result_universal_life["proj_date"]
    )

    proj_result_universal_life["annual_cohort"] = proj_result_universal_life[
        "product_type"
    ] + (proj_result_universal_life["inception_date"].dt.year).astype(str)

    proj_result_universal_life["proj_quarter"] = proj_result_universal_life[
        "proj_date"
    ].apply(extract_cohort)

    columns_group_by = ["annual_cohort", "proj_quarter"]

    grouped_df = proj_result_universal_life.groupby(
        columns_group_by, as_index=False
    )[columns_to_aggregate].sum()
    return grouped_df, non_proj_result_universal_life, not_found_columns
