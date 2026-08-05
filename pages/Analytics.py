import streamlit as st
import pandas as pd
import plotly.express as px

from utils.analytics import *

st.title("📊 Analytics Dashboard")

if "df" not in st.session_state:

    st.warning("Please upload a dataset first.")

    st.stop()

df = st.session_state["df"]

numeric = numerical_columns(df)

# ---------------- KPI ---------------- #

st.subheader("Dataset Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Rows", df.shape[0])

c2.metric("Columns", df.shape[1])

c3.metric("Numeric Columns", len(numeric))

c4.metric("Missing Values", df.isnull().sum().sum())

st.divider()

# ---------------- Statistics ---------------- #

st.subheader("Descriptive Statistics")

st.dataframe(
    descriptive_statistics(df),
    use_container_width=True
)

st.divider()

# ---------------- Column Analysis ---------------- #

st.subheader("Column Statistics")

column = st.selectbox(
    "Select Numerical Column",
    numeric
)

stats = column_statistics(df, column)

left, right = st.columns(2)

with left:

    st.metric("Mean", stats["Mean"])

    st.metric("Median", stats["Median"])

    st.metric("Mode", stats["Mode"])

    st.metric("Minimum", stats["Minimum"])

    st.metric("Maximum", stats["Maximum"])

with right:

    st.metric("Variance", stats["Variance"])

    st.metric("Std Deviation", stats["Standard Deviation"])

    st.metric("Skewness", stats["Skewness"])

    st.metric("Kurtosis", stats["Kurtosis"])

st.divider()

# ---------------- Distribution ---------------- #

st.subheader("Distribution")

fig = px.histogram(

    df,

    x=column,

    nbins=30,

    title=f"{column} Distribution"

)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------------- Box Plot ---------------- #

st.subheader("Outlier Detection")

fig = px.box(

    df,

    y=column,

    title=f"{column} Box Plot"

)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------------- Correlation ---------------- #

if len(numeric) > 1:

    st.subheader("Correlation Matrix")

    corr = correlation(df)

    fig = px.imshow(

        corr,

        text_auto=True,

        color_continuous_scale="RdBu_r"

    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------------- Covariance ---------------- #

if len(numeric) > 1:

    st.subheader("Covariance Matrix")

    st.dataframe(

        covariance(df),

        use_container_width=True

    )

st.divider()

# ---------------- Value Counts ---------------- #

st.subheader("Category Count")

cat_cols = df.select_dtypes(include="object").columns

if len(cat_cols):

    cat = st.selectbox(

        "Select Category",

        cat_cols

    )

    count = df[cat].value_counts().reset_index()

    count.columns = [cat, "Count"]

    fig = px.bar(

        count,

        x=cat,

        y="Count",

        color="Count"

    )

    st.plotly_chart(fig, use_container_width=True)

else:

    st.info("No categorical columns found.")

st.divider()

csv = descriptive_statistics(df).to_csv().encode()

st.download_button(

    "⬇ Download Analytics Report",

    csv,

    "analytics_report.csv",

    "text/csv"

)