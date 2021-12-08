import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash()

ucvkids = pd.read_csv(
    "./data/seattle_ucv_kids_cleaned.csv")
ucvkids

print(ucvkids.head())
fig = px.scatter(
    ucvkids,
    x="density",
    y="frac_change",
    size="2020",
    #color="continent",
    hover_name="neighborhood",
    log_x=False,
    size_max=60,
)

app.layout = html.Div([dcc.Graph(id="frac_change_vs_area", figure=fig)])


if __name__ == "__main__":
    app.run_server(debug=True)
