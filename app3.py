import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

colors = {
    'background': 'white',
    'text': 'mediumturquoise',
    'titletext':'mediumslateblue'
}

df = pd.read_csv("./data/seattle_ucv_kids_cleaned.csv")

print(df.head())
fig = px.scatter(
    df,
    x="density",
    y="frac_change",
    size="2020",
    #color="continent",
    hover_name="neighborhood",
    log_x=False,
    size_max=60,
    labels = {'frac_change':'fractional change in population', 'density':'density'}
)

fig2 = px.scatter(
    df,
    x="area",
    y="frac_change",
    size="2020",
    #color="continent",
    hover_name="neighborhood",
    log_x=False,
    size_max=60,
    labels = {'frac_change':'fractional change in population', 'area':'area'}
)




app.layout = html.Div([
    html.Div([
        html.Label(['Choose parameter']),
        dcc.Dropdown(
            id='parameter_dropdown',
            options=[
                     {'label': 'density', 'value': 'density'},
                     {'label': 'area', 'value': 'area'}
            ],
            value='density',
            multi=False,
            clearable=False,
            style={"width": "50%"}
        ),
    ]),

    html.Div([
        dcc.Graph(id='main_graph',figure = fig2)
    ]),

])

@app.callback(
    Output(component_id='main_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)

def update_graph(parameter_dropdown):
    dff = df


    chart = px.scatter(
        df,
        x=parameter_dropdown,
        y="frac_change",
        size="2020",
        #color="continent",
        hover_name="neighborhood",
        log_x=False,
        size_max=60,
        labels = {'frac_change':'fractional change in population', 'density':'density'}
    )

    return (chart)


if __name__ == "__main__":
    app.run_server(debug=True)
