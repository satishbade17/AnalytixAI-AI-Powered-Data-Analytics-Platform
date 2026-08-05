import streamlit as st

from utils.cleaning import *

st.title("🧹 Data Cleaning")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["df"]

st.write("### Original Dataset")

st.dataframe(df)

st.divider()

option = st.selectbox(
    "Select Cleaning Operation",
    [
        "Remove Duplicates",
        "Drop Missing Values",
        "Fill Missing (Mean)",
        "Fill Missing (Median)",
        "Fill Missing (Mode)",
        "Fill Missing (Constant)",
        "Label Encoding",
        "Normalize",
        "Standardize",
        "Remove Outliers"
    ]
)

clean_df = df.copy()

if st.button("Apply Cleaning"):

    if option == "Remove Duplicates":
        clean_df = remove_duplicates(df)

    elif option == "Drop Missing Values":
        clean_df = drop_missing(df)

    elif option == "Fill Missing (Mean)":
        clean_df = fill_missing(df, "mean")

    elif option == "Fill Missing (Median)":
        clean_df = fill_missing(df, "median")

    elif option == "Fill Missing (Mode)":
        clean_df = fill_missing(df, "mode")

    elif option == "Fill Missing (Constant)":
        clean_df = fill_missing(df, "constant")

    elif option == "Label Encoding":
        clean_df = label_encode(df)

    elif option == "Normalize":
        clean_df = normalize(df)

    elif option == "Standardize":
        clean_df = standardize(df)

    elif option == "Remove Outliers":
        clean_df = remove_outliers(df)

    st.session_state["df"] = clean_df

    st.success("Cleaning Applied Successfully!")

    st.write("### Cleaned Dataset")

    st.dataframe(clean_df)

    csv = clean_df.to_csv(index=False).encode()

    st.download_button(
        "⬇ Download Clean Dataset",
        csv,
        "clean_dataset.csv",
        "text/csv"
    )