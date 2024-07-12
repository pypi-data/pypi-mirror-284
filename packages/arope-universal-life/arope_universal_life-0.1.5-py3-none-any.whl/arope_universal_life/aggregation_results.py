from arope_universal_life.abstracted_packages import furtheredge_pandas as pd


def extract_cohort(issue_date):
    """
    Extracts the cohort from the given issue date.

    Args:
        issue_date (pd.Timestamp): The date of issue for the policy.

    Returns:
        str: The cohort string in the format "YYYYQX" where YYYY is the year and X is the quarter.
    """
    year = issue_date.year
    quarter = (issue_date.month - 1) // 3 + 1
    return f"{year}Q{quarter}"


def aggregation_monthly_to_quarterly_projection(proj_result_universal_life):
    """
    Aggregates monthly projection results into quarterly data for Universal Life insurance policies.

    This function processes the monthly projection results, groups the data by annual cohort and
    projection quarter, and sums up the relevant financial metrics for each group. The aggregation
    helps in analyzing the data on a quarterly basis for better financial and actuarial insights.

    Args:
        proj_result_universal_life (pd.DataFrame): DataFrame containing monthly projection results
                                                   for Universal Life insurance policies. The DataFrame
                                                   must include the following columns:
                                                   - 'inception_date'
                                                   - 'proj_date'
                                                   - 'product_type'
                                                   - Columns to be aggregated (e.g., 'paid_premium_amt', 'acq_loading_amt', etc.)

    Returns:
        pd.DataFrame: A DataFrame aggregated on a quarterly basis, with the relevant financial metrics
                      summed for each quarter.
    """
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
    columns_to_aggregate = [
        "paid_premium_amt",
        "acq_loading_amt",
        "fee_amt",
        "net_paid_premium_amt",
        "prev_fund1_av_amt",
        "premium_alloc_amt",
        "sar_death_amt",
        "sar_or_amt",
        "sar_adb_amt",
        "coi_death_amt",
        "coi_or_amt",
        "coi_adb_amt",
        "fund1_value_amt",
        "fmf_amt",
        "fund1_av_amt",
        "fund1_interest_amt",
        "lrc_premium_amt",
        "lrc_commission_amt",
        "death_benefits_amt",
        "or_benefits_amt",
        "adb_benefits_amt",
        "mortality_claims_amt",
        "surrender_claims_amt",
        "maturity_claims_amt",
        "lrc_claims_amt",
        "maintenance_expens_amt",
        "ceded_sa_amt",
        "lrc_re_premium_amt",
        "lrc_re_commission_amt",
        "lrc_re_claims_amt",
        "lrc_re_profitsharing_amt",
    ]

    columns_group_by = ["annual_cohort", "proj_quarter"]

    grouped_df = proj_result_universal_life.groupby(
        columns_group_by, as_index=False
    )[columns_to_aggregate].sum()
    return grouped_df
