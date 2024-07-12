from idi_model.abstracted_packages import furtheredge_pandas as pd


def merge_monthly_loss_ratio(df_input, monthly_loss_ratio_df):

    monthly_loss_ratio_df["monthly_loss_ratio"] = (
        monthly_loss_ratio_df["incurred_pattern"] * 60
    ) / 100
    df_input = pd.merge(
        df_input,
        monthly_loss_ratio_df,
        how="left",
        left_on="Coverage_period_index",
        right_on="cov_month_index",
    )
    df_input = df_input.infer_objects(copy=False).fillna(0)

    return df_input
