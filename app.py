import streamlit as st

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AnalytixAI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD CSS ---------------- #

try:
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except FileNotFoundError:
    pass

# ---------------- HOME PAGE ---------------- #

st.title("📊 AnalytixAI")

st.subheader("AI Powered Data Analytics Studio")

st.write("""
Welcome to **AnalytixAI**!

Upload any CSV or Excel dataset and perform:

- Data Cleaning
- Data Profiling
- Data Quality Analysis
- Analytics Dashboard
- Interactive Visualizations
- AI Insights
- Machine Learning
- Report Generation
""")

st.divider()

# ---------------- BUTTONS ---------------- #

col1, col2, col3 = st.columns(3)

with col1:
    st.button(
        "📂 Upload Dataset",
        use_container_width=True
    )

with col2:
    st.button(
        "🤖 AI Insights",
        use_container_width=True
    )

with col3:
    st.button(
        "📄 Generate Report",
        use_container_width=True
    )

st.divider()

# ---------------- FEATURES ---------------- #

st.header("✨ Features")

c1, c2 = st.columns(2)

with c1:
    st.info("""
### 🧹 Data Processing

- Remove Missing Values
- Remove Duplicates
- Handle Outliers
- Normalize Data
- Data Quality Analysis
""")

with c2:
    st.success("""
### 📊 Analytics

- Interactive Charts
- Correlation Analysis
- AI Insights
- Machine Learning
- PDF & Excel Reports
""")

st.divider()

# ---------------- MODULES ---------------- #

st.header("📌 Included Modules")

modules = [
    "Home",
    "Upload Data",
    "Data Cleaning",
    "Data Profiling",
    "Data Quality",
    "Analytics",
    "Visualizations",
    "AI Insights",
    "Machine Learning",
    "Reports"
]

for i, module in enumerate(modules, start=1):
    st.write(f"{i}. {module}")

st.divider()

st.success(
    "AnalytixAI v1.0 | Built with Streamlit, Pandas, Plotly, Scikit-learn"
)