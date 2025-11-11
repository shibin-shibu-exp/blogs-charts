import plotly.express as px
import pandas as pd

# Data
data = {
    "Month": ["Jun", "Jun", "Jun", "Jun", "Jun", "Jun", "Jun", "Jun",
              "Jul", "Jul", "Jul", "Jul", "Jul", "Jul", "Jul", "Jul",
              "Aug", "Aug", "Aug", "Aug", "Aug", "Aug", "Aug", "Aug",
              "Sep", "Sep", "Sep", "Sep", "Sep", "Sep", "Sep", "Sep",
              "Oct", "Oct", "Oct", "Oct", "Oct", "Oct", "Oct", "Oct"],
    "Source": ["Natural Search", "Direct", "Email", "Paid Search", "Internal", "Social (Earned)", "Social (Paid)", "Other Websites"] * 5,
    "Value": [
        58.6, 13.9, 9.8, 8.7, 8.6, 0, 0, 0,       # Jun
        32.4, 6, 54.1, 2.1, 1.9, 0, 0, 3.6,       # Jul
        30, 8.2, 36.7, 11, 4.9, 0, 0, 0,          # Aug
        40, 7.2, 19.6, 7.2, 0, 0, 16, 0,          # Sep
        48.8, 8.7, 5, 0, 0, 12.2, 13.8, 0         # Oct
    ]
}

df = pd.DataFrame(data)

colors = [
    "#FF6600", "#000000", "#4C4C4C", "#B3B3B3",
    "#FF944D", "#262626", "#FFB380", "#E6E6E6"
]

color_map = dict(zip(df["Source"].unique(), colors))

fig = px.sunburst(
    df,
    path=["Month", "Source"],
    values="Value",
    color="Source",
    color_discrete_map=color_map,
    title="Traffic Source Distribution by Month (Sunburst View)"
)

fig.update_traces(textinfo="label+percent entry")
fig.update_layout(
    title_font=dict(size=18, family="Arial", color="#262626"),
    font=dict(size=12),
    margin=dict(t=60, l=10, r=10, b=10)
)

fig.show()
