import streamlit as st
import pandas as pd
from utils.ai import *

st.title("🤖 AI Insights")

if "df" not in st.session_state:

    st.warning("Upload dataset first.")

    st.stop()

df = st.session_state["df"]

# ---------------- Summary ---------------- #

st.header("📄 Dataset Summary")

for s in generate_summary(df):

    st.info(s)

st.divider()

# ---------------- Correlation ---------------- #

st.header("📈 Correlation Insights")

corr = correlation_insights(df)

if corr:

    for c in corr:

        st.success(c)

else:

    st.info("No strong correlations detected.")

st.divider()

# ---------------- Outliers ---------------- #

st.header("📦 Outlier Detection")

outs = outlier_insights(df)

if outs:

    for o in outs:

        st.warning(o)

else:

    st.success("No significant outliers detected.")

st.divider()

# ---------------- Recommendations ---------------- #

st.header("💡 AI Recommendations")

for r in recommendations(df):

    st.success(r)

st.divider()

# ---------------- Download Report ---------------- #

report = pd.DataFrame({

    "Summary":generate_summary(df)

})

csv = report.to_csv(index=False).encode()

st.download_button(

    "⬇ Download AI Report",

    csv,

    "AI_Report.csv",

    "text/csv"
)