import streamlit as st
import pandas as pd
from utils.report import generate_pdf

st.title("📄 Report Generation")

if "df" not in st.session_state:

    st.warning("Upload dataset first.")

    st.stop()

df = st.session_state["df"]

report_type = st.selectbox(

    "Choose Report",

    [

        "PDF",

        "Excel",

        "CSV",

        "HTML"

    ]

)

if st.button("Generate Report"):

    if report_type == "PDF":

        filename = "reports/report.pdf"

        generate_pdf(df, filename)

        with open(filename,"rb") as f:

            st.download_button(

                "⬇ Download PDF",

                f,

                "AnalytixAI_Report.pdf"

            )

    elif report_type == "Excel":

        filename = "reports/report.xlsx"

        df.to_excel(filename,index=False)

        with open(filename,"rb") as f:

            st.download_button(

                "⬇ Download Excel",

                f,

                "AnalytixAI_Report.xlsx"

            )

    elif report_type == "CSV":

        csv = df.to_csv(index=False).encode()

        st.download_button(

            "⬇ Download CSV",

            csv,

            "AnalytixAI_Report.csv"

        )

    elif report_type == "HTML":

        html = df.to_html()

        st.download_button(

            "⬇ Download HTML",

            html,

            "AnalytixAI_Report.html"

        )

st.divider()

st.subheader("Report Preview")

st.dataframe(df.head())