import plotly.express as px


def bar_chart(df, x, y, color=None):
    return px.bar(df, x=x, y=y, color=color)


def line_chart(df, x, y, color=None):
    return px.line(df, x=x, y=y, color=color)


def scatter_chart(df, x, y, color=None):
    return px.scatter(df, x=x, y=y, color=color)


def histogram(df, x):
    return px.histogram(df, x=x)


def box_plot(df, y):
    return px.box(df, y=y)


def violin_plot(df, y):
    return px.violin(df, y=y, box=True)


def pie_chart(df, names):
    return px.pie(df, names=names)


def area_chart(df, x, y):
    return px.area(df, x=x, y=y)


def heatmap(df):
    return px.imshow(df.corr(numeric_only=True), text_auto=True)


def bubble_chart(df, x, y, size, color):
    return px.scatter(
        df,
        x=x,
        y=y,
        size=size,
        color=color
    )


def treemap(df, path, values):
    return px.treemap(df, path=[path], values=values)


def sunburst(df, path, values):
    return px.sunburst(df, path=[path], values=values)


def scatter3d(df, x, y, z, color):
    return px.scatter_3d(
        df,
        x=x,
        y=y,
        z=z,
        color=color
    )