from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd
from datetime import datetime


def generate_pdf(df, filename):

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(filename)

    elements = []

    elements.append(
        Paragraph("<b>AnalytixAI Report</b>", styles["Title"])
    )

    elements.append(
        Paragraph(
            f"Generated : {datetime.now()}",
            styles["Normal"]
        )
    )

    elements.append(Spacer(1,20))

    summary = [

        ["Rows", df.shape[0]],

        ["Columns", df.shape[1]],

        ["Missing Values", df.isnull().sum().sum()],

        ["Duplicates", df.duplicated().sum()]

    ]

    table = Table(summary)

    table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.lightblue),

        ("GRID",(0,0),(-1,-1),1,colors.black),

        ("BOTTOMPADDING",(0,0),(-1,0),10)

    ]))

    elements.append(table)

    elements.append(Spacer(1,20))

    elements.append(
        Paragraph(
            "<b>Statistics</b>",
            styles["Heading2"]
        )
    )

    stats = df.describe().round(2)

    stat_table = [stats.columns.tolist()] + stats.values.tolist()

    table2 = Table(stat_table)

    table2.setStyle(TableStyle([

        ("GRID",(0,0),(-1,-1),1,colors.black),

        ("BACKGROUND",(0,0),(-1,0),colors.grey),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white)

    ]))

    elements.append(table2)

    doc.build(elements)