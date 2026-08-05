import pandas as pd


def calculate_quality(df):

    rows = len(df)
    cols = len(df.columns)
    total_cells = rows * cols

    # -------------------------
    # Completeness
    # -------------------------

    missing = df.isnull().sum().sum()

    completeness = ((total_cells - missing) / total_cells) * 100

    # -------------------------
    # Uniqueness
    # -------------------------

    duplicates = df.duplicated().sum()

    uniqueness = ((rows - duplicates) / rows) * 100

    # -------------------------
    # Validity
    # -------------------------

    valid = 100

    # -------------------------
    # Consistency
    # -------------------------

    consistency = 100

    overall = round(
        (completeness + uniqueness + valid + consistency) / 4,
        2
    )

    return {

        "Completeness": round(completeness,2),

        "Uniqueness": round(uniqueness,2),

        "Validity": round(valid,2),

        "Consistency": round(consistency,2),

        "Overall": overall,

        "Missing": missing,

        "Duplicates": duplicates

    }


def recommendations(result):

    rec = []

    if result["Missing"] > 0:
        rec.append("Fill or remove missing values.")

    if result["Duplicates"] > 0:
        rec.append("Remove duplicate records.")

    if result["Overall"] > 95:
        rec.append("Excellent dataset quality.")

    elif result["Overall"] > 80:
        rec.append("Dataset is good but can be improved.")

    else:
        rec.append("Dataset requires cleaning before analysis.")

    return rec