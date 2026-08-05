import pandas as pd

def generate_summary(df):

    summary = []

    summary.append(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

    numeric = df.select_dtypes(include="number").columns
    categorical = df.select_dtypes(exclude="number").columns

    summary.append(f"Numerical Columns : {len(numeric)}")
    summary.append(f"Categorical Columns : {len(categorical)}")

    missing = df.isnull().sum().sum()

    summary.append(f"Missing Values : {missing}")

    duplicates = df.duplicated().sum()

    summary.append(f"Duplicate Rows : {duplicates}")

    return summary


def correlation_insights(df):

    insights = []

    corr = df.corr(numeric_only=True)

    for col in corr.columns:

        for row in corr.index:

            if row != col:

                value = corr.loc[row, col]

                if abs(value) > 0.8:

                    insights.append(
                        f"{row} and {col} have strong correlation ({value:.2f})"
                    )

    return list(set(insights))


def outlier_insights(df):

    insights = []

    numeric = df.select_dtypes(include="number")

    for col in numeric.columns:

        q1 = numeric[col].quantile(.25)

        q3 = numeric[col].quantile(.75)

        iqr = q3-q1

        outliers = numeric[
            (numeric[col] < q1-1.5*iqr) |
            (numeric[col] > q3+1.5*iqr)
        ]

        if len(outliers) > 0:

            insights.append(
                f"{col} contains {len(outliers)} outliers."
            )

    return insights


def recommendations(df):

    rec = []

    if df.isnull().sum().sum():

        rec.append(
            "Fill missing values before Machine Learning."
        )

    if df.duplicated().sum():

        rec.append(
            "Remove duplicate records."
        )

    if len(df.select_dtypes(include="number").columns) > 5:

        rec.append(
            "Feature Selection may improve model performance."
        )

    rec.append(
        "Visualize important columns before training."
    )

    return rec