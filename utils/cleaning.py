import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler


def remove_duplicates(df):
    return df.drop_duplicates()


def drop_missing(df):
    return df.dropna()


def fill_missing(df, method="mean"):

    df = df.copy()

    numeric_cols = df.select_dtypes(include=np.number).columns

    categorical_cols = df.select_dtypes(exclude=np.number).columns

    if method == "mean":
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    elif method == "median":
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

    elif method == "mode":
        for col in df.columns:
            df[col] = df[col].fillna(df[col].mode()[0])

    elif method == "constant":
        df = df.fillna(0)

    return df


def label_encode(df):

    df = df.copy()

    encoder = LabelEncoder()

    cols = df.select_dtypes(include="object").columns

    for col in cols:
        df[col] = encoder.fit_transform(df[col].astype(str))

    return df


def normalize(df):

    scaler = MinMaxScaler()

    numeric = df.select_dtypes(include=np.number).columns

    df[numeric] = scaler.fit_transform(df[numeric])

    return df


def standardize(df):

    scaler = StandardScaler()

    numeric = df.select_dtypes(include=np.number).columns

    df[numeric] = scaler.fit_transform(df[numeric])

    return df


def remove_outliers(df):

    numeric = df.select_dtypes(include=np.number).columns

    new_df = df.copy()

    for col in numeric:

        q1 = new_df[col].quantile(0.25)

        q3 = new_df[col].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr

        upper = q3 + 1.5 * iqr

        new_df = new_df[
            (new_df[col] >= lower) &
            (new_df[col] <= upper)
        ]

    return new_df