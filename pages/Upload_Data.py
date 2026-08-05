import streamlit as st
import pandas as pd
from utils.loader import load_file

st.title("📂 Upload Dataset")

st.write("Upload CSV or Excel dataset")

uploaded_file = st.file_uploader(
    "Choose a file",
    type=["csv", "xlsx"]
)

if uploaded_file:

    df = load_file(uploaded_file)

    st.success("Dataset Uploaded Successfully")

    st.session_state["df"] = df

    st.divider()

    # ---------------- KPI ---------------- #

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Rows", df.shape[0])

    with c2:
        st.metric("Columns", df.shape[1])

    with c3:
        st.metric("Missing Values", df.isnull().sum().sum())

    with c4:
        memory = round(df.memory_usage(deep=True).sum()/1024,2)
        st.metric("Memory (KB)", memory)

    st.divider()

    # Preview

    st.subheader("Dataset Preview")

    st.dataframe(df.head(20), use_container_width=True)

    st.divider()

    # Data Types

    st.subheader("Column Data Types")

    datatype = pd.DataFrame({
        "Column": df.columns,
        "Datatype": df.dtypes.astype(str)
    })

    st.dataframe(datatype, use_container_width=True)

    st.divider()

    # Missing Values

    st.subheader("Missing Value Report")

    missing = pd.DataFrame({
        "Column": df.columns,
        "Missing": df.isnull().sum(),
        "Percentage":
        round(df.isnull().sum()/len(df)*100,2)
    })

    st.dataframe(missing, use_container_width=True)

    st.divider()

    # Dataset Information

    st.subheader("Dataset Information")

    info = pd.DataFrame({

        "Feature":[
            "Rows",
            "Columns",
            "Duplicates",
            "Memory KB"
        ],

        "Value":[
            df.shape[0],
            df.shape[1],
            df.duplicated().sum(),
            memory
        ]

    })

    st.table(info)

    st.divider()

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Dataset",
        csv,
        "dataset.csv",
        "text/csv"
    )