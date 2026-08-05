import pandas as pd
import numpy as np


def numerical_columns(df):
    return df.select_dtypes(include=np.number).columns.tolist()


def descriptive_statistics(df):
    return df.describe().T


def column_statistics(df, column):

    return {

        "Mean": round(df[column].mean(), 2),

        "Median": round(df[column].median(), 2),

        "Mode": df[column].mode().iloc[0],

        "Minimum": df[column].min(),

        "Maximum": df[column].max(),

        "Variance": round(df[column].var(), 2),

        "Standard Deviation": round(df[column].std(), 2),

        "Skewness": round(df[column].skew(), 2),

        "Kurtosis": round(df[column].kurt(), 2)

    }


def correlation(df):
    return df.corr(numeric_only=True)


def covariance(df):
    return df.cov(numeric_only=True)