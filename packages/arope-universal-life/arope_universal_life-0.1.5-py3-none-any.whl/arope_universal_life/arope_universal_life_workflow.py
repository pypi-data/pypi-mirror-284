from arope_universal_life.universal_life_module import universal_life
from arope_universal_life.aggregation_results import (
    aggregation_monthly_to_quarterly_projection,
)


def arope_universal_life(
    policies,
    ri_rates,
    wop_rates,
    tech_assumptions,
    product,
    save_model_points,
    model_points_path,
    proj_columns,
    non_proj_columns,
    run_settings,
    chuck_size=-100,
    projection_points=700,
    show_excecution_time=True,
):
    """
    Perform Universal Life insurance policy projections and aggregate results quarterly.

    This function processes Universal Life insurance policy data, performs projections,
    and aggregates the monthly results into quarterly data. It uses the `universal_life`
    function to generate projection results and then aggregates them using the
    `aggregation_monthly_to_quarterly_projection` function.

    Args:
        policies (pd.DataFrame): DataFrame containing the policy data.
        ri_rates (pd.DataFrame): DataFrame containing reinsurance rates.
        wop_rates (pd.DataFrame): DataFrame containing waiver of premium rates.
        tech_assumptions (pd.DataFrame): DataFrame containing technical assumptions.
        product (pd.DataFrame): DataFrame containing product details.
        save_model_points (bool): Whether to save model points.
        model_points_path (str): Path to save the model points if `save_model_points` is True.
        proj_columns (list): List of columns to include in the projection.
        non_proj_columns (list): List of columns not included in the projection.
        run_settings (dict): Dictionary containing run settings for the projection.
        chuck_size (int, optional): Chunk size for processing. Defaults to -100.
        projection_points (int, optional): Number of projection points (months). Defaults to 700.
        show_excecution_time (bool, optional): Whether to display execution time. Defaults to True.

    Returns:
        tuple:
            - aggregated_result (pd.DataFrame): DataFrame with quarterly aggregated projection results.
            - non_proj_result_universal_life (pd.DataFrame): DataFrame with non-projection results.
            - not_found_columns (list): List of columns not found during processing.
    """
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
        save_model_points,
        model_points_path,
        proj_columns,
        non_proj_columns,
        run_settings,
        chuck_size,
        projection_points,
        show_excecution_time,
    )
    aggregated_result = aggregation_monthly_to_quarterly_projection(
        proj_result_universal_life
    )
    return aggregated_result, non_proj_result_universal_life, not_found_columns
