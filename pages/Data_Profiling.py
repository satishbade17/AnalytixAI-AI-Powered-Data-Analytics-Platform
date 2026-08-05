import streamlit as st
import plotly.express as px
from utils.profiling import *

st.title("📊 Data Profiling")

if "df" not in st.session_state:
    st.warning("Please upload a dataset first.")
    st.stop()

df = st.session_state["df"]

# ----------------------------
# Dataset Overview
# ----------------------------

overview = dataset_overview(df)

st.subheader("📌 Dataset Overview")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Rows", overview["Rows"])
c2.metric("Columns", overview["Columns"])
c3.metric("Duplicates", overview["Duplicates"])
c4.metric("Missing", overview["Missing Values"])
c5.metric("Memory", f"{overview['Memory (KB)']} KB")

st.divider()

# ----------------------------
# Column Summary
# ----------------------------

st.subheader("📋 Column Summary")

summary = column_summary(df)

st.dataframe(summary, use_container_width=True)

st.divider()

# ----------------------------
# Summary Statistics
# ----------------------------

st.subheader("📈 Summary Statistics")

st.dataframe(summary_statistics(df), use_container_width=True)

st.divider()

# ----------------------------
# Numerical Columns
# ----------------------------

st.subheader("🔢 Numerical Columns")

st.write(numerical_columns(df))

# ----------------------------
# Categorical Columns
# ----------------------------

st.subheader("🔤 Categorical Columns")

st.write(categorical_columns(df))

st.divider()

# ----------------------------
# Missing Value Chart
# ----------------------------

missing = df.isnull().sum().reset_index()

missing.columns = ["Column","Missing"]

fig = px.bar(
    missing,
    x="Column",
    y="Missing",
    title="Missing Values"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ----------------------------
# Correlation Heatmap
# ----------------------------

numeric = df.select_dtypes(include="number")

if numeric.shape[1] > 1:

    corr = numeric.corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="Viridis",
        title="Correlation Matrix"
    )

    st.plotly_chart(fig, use_container_width=True)

else:

    st.info("Not enough numerical columns for correlation.")