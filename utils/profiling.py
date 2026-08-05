import pandas as pd

def dataset_overview(df):
    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Duplicates": df.duplicated().sum(),
        "Missing Values": df.isnull().sum().sum(),
        "Memory (KB)": round(df.memory_usage(deep=True).sum()/1024,2)
    }


def column_summary(df):

    summary = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing": df.isnull().sum(),
        "Missing %": round(df.isnull().sum()/len(df)*100,2),
        "Unique Values": df.nunique(),
    })

    return summary


def numerical_columns(df):
    return df.select_dtypes(include="number").columns.tolist()


def categorical_columns(df):
    return df.select_dtypes(exclude="number").columns.tolist()


def summary_statistics(df):
    return df.describe().T