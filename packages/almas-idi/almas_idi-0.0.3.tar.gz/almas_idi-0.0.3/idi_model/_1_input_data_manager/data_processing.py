from idi_model.abstracted_packages import furtheredge_pandas as pd
from idi_model.abstracted_packages import furtheredge_numpy as np


def add_1_day(row):
    return row["issue_date"] + pd.Timedelta(days=1)


def add_10_years(row):
    return row["estimated_date_of_inception"] + pd.DateOffset(years=10)


def add_1_day_act(row):
    return row["issue_date"] + pd.Timedelta(days=1)


def add_10_years_act(row):
    return row["date_of_activation_inception"] + pd.DateOffset(years=10)


def process_deposit_df(df):
    df["issue_date"] = pd.to_datetime(df["issue_date"])
    df["estimated_date_of_inception"] = pd.to_datetime(
        df["estimated_date_of_inception"]
    )
    df["estimated_date_of_expiry"] = pd.to_datetime(
        df["estimated_date_of_expiry"]
    )
    condition = df["issue_date"] >= df["estimated_date_of_inception"]
    df["estimated_date_of_inception"] = np.where(
        condition,
        df.apply(add_1_day, axis=1),
        df["estimated_date_of_inception"],
    )
    df["estimated_date_of_expiry"] = np.where(
        condition,
        df.apply(add_10_years, axis=1),
        df["estimated_date_of_expiry"],
    )
    # df["issue_date"] = df["issue_date"].dt.strftime("%d/%m/%Y")
    # df["estimated_date_of_inception"] = df[
    #     "estimated_date_of_inception"
    # ].dt.strftime("%d/%m/%Y")
    # df["estimated_date_of_expiry"] = df[
    #     "estimated_date_of_expiry"
    # ].dt.strftime("%d/%m/%Y")
    return df


def process_activation_df(df):
    df["issue_date"] = pd.to_datetime(df["issue_date"])
    df["date_of_activation_inception"] = pd.to_datetime(
        df["date_of_activation_inception"]
    )
    df["date_of_activation_expiry"] = pd.to_datetime(
        df["date_of_activation_expiry"]
    )

    condition = df["issue_date"] >= df["date_of_activation_inception"]
    df["date_of_activation_inception"] = np.where(
        condition,
        df.apply(add_1_day, axis=1),
        df["date_of_activation_inception"],
    )

    df["date_of_activation_expiry"] = np.where(
        condition,
        df.apply(add_10_years_act, axis=1),
        df["date_of_activation_expiry"],
    )
    # df["issue_date"] = df["issue_date"].dt.strftime("%d/%m/%Y")
    # df["date_of_activation_inception"] = df[
    #     "date_of_activation_inception"
    # ].dt.strftime("%d/%m/%Y")
    # df["date_of_activation_expiry"] = df[
    #     "date_of_activation_expiry"
    # ].dt.strftime("%d/%m/%Y")
    return df
