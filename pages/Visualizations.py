import streamlit as st
from utils.charts import *

st.title("📈 Interactive Visualizations")

if "df" not in st.session_state:
    st.warning("Upload dataset first.")
    st.stop()

df = st.session_state["df"]

chart = st.selectbox(
    "Select Chart",
    [
        "Bar",
        "Line",
        "Scatter",
        "Histogram",
        "Box",
        "Violin",
        "Pie",
        "Area",
        "Heatmap",
        "Bubble",
        "Treemap",
        "Sunburst",
        "3D Scatter"
    ]
)

columns = df.columns.tolist()

numeric = df.select_dtypes(include="number").columns.tolist()

categorical = df.select_dtypes(exclude="number").columns.tolist()

if chart == "Bar":

    x = st.selectbox("X-axis", columns)

    y = st.selectbox("Y-axis", numeric)

    color = st.selectbox("Color", ["None"] + columns)

    fig = bar_chart(
        df,
        x,
        y,
        None if color == "None" else color
    )

elif chart == "Line":

    x = st.selectbox("X-axis", columns)

    y = st.selectbox("Y-axis", numeric)

    fig = line_chart(df, x, y)

elif chart == "Scatter":

    x = st.selectbox("X-axis", numeric)

    y = st.selectbox("Y-axis", numeric)

    color = st.selectbox("Color", ["None"] + columns)

    fig = scatter_chart(
        df,
        x,
        y,
        None if color == "None" else color
    )

elif chart == "Histogram":

    x = st.selectbox("Column", numeric)

    fig = histogram(df, x)

elif chart == "Box":

    y = st.selectbox("Column", numeric)

    fig = box_plot(df, y)

elif chart == "Violin":

    y = st.selectbox("Column", numeric)

    fig = violin_plot(df, y)

elif chart == "Pie":

    names = st.selectbox("Category", categorical)

    fig = pie_chart(df, names)

elif chart == "Area":

    x = st.selectbox("X-axis", columns)

    y = st.selectbox("Y-axis", numeric)

    fig = area_chart(df, x, y)

elif chart == "Heatmap":

    fig = heatmap(df)

elif chart == "Bubble":

    x = st.selectbox("X-axis", numeric)

    y = st.selectbox("Y-axis", numeric)

    size = st.selectbox("Bubble Size", numeric)

    color = st.selectbox("Color", columns)

    fig = bubble_chart(df, x, y, size, color)

elif chart == "Treemap":

    path = st.selectbox("Category", categorical)

    values = st.selectbox("Values", numeric)

    fig = treemap(df, path, values)

elif chart == "Sunburst":

    path = st.selectbox("Category", categorical)

    values = st.selectbox("Values", numeric)

    fig = sunburst(df, path, values)

elif chart == "3D Scatter":

    x = st.selectbox("X", numeric)

    y = st.selectbox("Y", numeric)

    z = st.selectbox("Z", numeric)

    color = st.selectbox("Color", columns)

    fig = scatter3d(df, x, y, z, color)

fig.update_layout(
    height=650,
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)