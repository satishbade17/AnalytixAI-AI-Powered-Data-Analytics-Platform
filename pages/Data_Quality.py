import streamlit as st
import plotly.graph_objects as go
import pandas as pd

from utils.quality import *

st.title("⭐ Data Quality Analysis")

if "df" not in st.session_state:

    st.warning("Upload dataset first.")

    st.stop()

df = st.session_state["df"]

quality = calculate_quality(df)

# ---------------- Metrics ---------------- #

st.subheader("Overall Quality")

c1,c2,c3,c4,c5 = st.columns(5)

c1.metric("Quality",f"{quality['Overall']}%")

c2.metric("Completeness",f"{quality['Completeness']}%")

c3.metric("Uniqueness",f"{quality['Uniqueness']}%")

c4.metric("Missing",quality["Missing"])

c5.metric("Duplicates",quality["Duplicates"])

st.divider()

# ---------------- Gauge ---------------- #

fig = go.Figure(go.Indicator(

    mode="gauge+number",

    value=quality["Overall"],

    title={"text":"Quality Score"},

    gauge={

        "axis":{"range":[0,100]},

        "bar":{"color":"green"},

        "steps":[

            {"range":[0,50],"color":"red"},

            {"range":[50,80],"color":"orange"},

            {"range":[80,100],"color":"lightgreen"}

        ]

    }

))

st.plotly_chart(fig,use_container_width=True)

st.divider()

# ---------------- Score Table ---------------- #

score = pd.DataFrame({

    "Metric":[

        "Completeness",

        "Uniqueness",

        "Consistency",

        "Validity"

    ],

    "Score":[

        quality["Completeness"],

        quality["Uniqueness"],

        quality["Consistency"],

        quality["Validity"]

    ]

})

st.subheader("Quality Metrics")

st.dataframe(score,use_container_width=True)

st.divider()

# ---------------- Recommendation ---------------- #

st.subheader("AI Recommendations")

for r in recommendations(quality):

    st.success(r)

st.divider()

report = score.to_csv(index=False).encode()

st.download_button(

    "⬇ Download Quality Report",

    report,

    "quality_report.csv",

    "text/csv"

)