import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash()

colors = {
    'background': 'white',
    'text': 'mediumturquoise',
    'titletext':'mediumslateblue'
}

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
    labels = {'frac_change':'fractional change in population', 'density':'density'}
)

fig2 = px.scatter(
    ucvkids,
    x="area",
    y="frac_change",
    size="2020",
    #color="continent",
    hover_name="neighborhood",
    log_x=False,
    size_max=60,
    labels = {'frac_change':'fractional change in population', 'area':'area'}
)


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Seattle Urban Center and Village Population Data',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Fractional Change in UCV Population vs Density', style={
        'textAlign': 'center',
        'color': colors['titletext']
    }),

    dcc.Graph(
        id='frac_change_vs_density',
        figure=fig
    ),



    #this adds the second plot
    html.Div(children='Fractional Change in UCV Population vs Area', style={
        'textAlign': 'center',
        'color': colors['titletext']
    }),

    dcc.Graph(
        id='frac_change_vs_area',
        figure=fig2
    ) #end of adding second plot, to add another add a , and another html.Div
]
)



if __name__ == "__main__":
    app.run_server(debug=True)
