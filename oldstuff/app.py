import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash()

ucvpop = pd.read_csv(
    "./data/citydata/Urban_Centers_and_Villages_with_PL_94-171_Redistricting__Data_for_1990-2020.csv"
)
ucvpop['change'] = ucvpop['F2020_PL_data_TOT_POP'] - ucvpop['F2010_PL_data_TOT_POP']
ucvpop['perc_change'] = (ucvpop['F2020_PL_data_TOT_POP'] - ucvpop['F2010_PL_data_TOT_POP'])/ucvpop['F2010_PL_data_TOT_POP']


print(ucvpop.head())
fig = px.scatter(
    ucvpop,
    x="AREA_ACRES",
    y="perc_change",
    size="F2020_PL_data_TOT_POP",
    #color="continent",
    hover_name="NEIGH_NAME",
    log_x=True,
    size_max=60,
)

app.layout = html.Div([dcc.Graph(id="perc_change_vs_area", figure=fig)])


if __name__ == "__main__":
    app.run_server(debug=True)
