# seattle_full_dashboard.py
# based on the dash tutorial: https://dash.plotly.com/interactive-graphing
# modified by L. Minter

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# read in our data
df = pd.read_csv('./data/dashdata/dash-data-combined.csv')
enroll = pd.read_csv('./data/dashdata/dash-data-enrollment.csv')

# instantiate the Dash class
app = dash.Dash(__name__)

# get the list of available indicators from the dataframe
available_indicators = df['Indicator Name'].unique()

# set the layout of the dashboard
app.layout = html.Div([
    html.Div([

        html.Div([
            html.Label(['choose horizontal axis:']),
            dcc.Dropdown(
                id='crossfilter-xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='total population'
            ),
            dcc.RadioItems(
                id='crossfilter-xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block', 'marginTop': '5px'}
            )
        ],
        style={'width': '49%', 'display': 'inline-block'}),

        html.Div([
            html.Label(['choose vertical axis:']),
            dcc.Dropdown(
                id='crossfilter-yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='10_year_frac_growth_all'
            ),
            dcc.RadioItems(
                id='crossfilter-yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block', 'marginTop': '5px'}
            )
        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
    ], style={
        'padding': '10px 5px'
    }),

    html.Div([
        dcc.Graph(
            id='crossfilter-indicator-scatter',
            hoverData={'points': [{'customdata': 'Downtown'}]}
        )

    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([
        dcc.Graph(id='x-time-series'),
        dcc.Graph(id='y-time-series'),
    ], style={'display': 'inline-block', 'width': '49%'}),

    html.Div(dcc.Slider(
        id='crossfilter-year--slider',
        min=df['Year'].min(),
        max=df['Year'].max(),
        value=df['Year'].max(),
        marks={str(year): str(year) for year in df['Year'].unique()},
        step=None
    ), style={'width': '49%', 'padding': '0px 20px 20px 20px'})
])


# callbacks
@app.callback(
    dash.dependencies.Output('crossfilter-indicator-scatter', 'figure'),
    [dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-xaxis-type', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-type', 'value'),
     dash.dependencies.Input('crossfilter-year--slider', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    dff = df[df['Year'] == year_value]

    fig = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
            y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
            hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['neighborhood']
            )
    fig.update_traces(customdata=dff[dff['Indicator Name'] == yaxis_column_name]['neighborhood'])
    fig.update_xaxes(title=xaxis_column_name, type='linear' if xaxis_type == 'Linear' else 'log')
    fig.update_yaxes(title=yaxis_column_name, type='linear' if yaxis_type == 'Linear' else 'log')
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig


def create_time_series(dff, title):
    axis_type = 'Linear' #force linear for the time series
    fig = px.scatter(dff, x='Year', y='Value')
    fig.update_traces(mode='lines+markers')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(type='linear')
    fig.add_annotation(x=0, y=0.85, xanchor='left', yanchor='bottom',
                       xref='paper', yref='paper', showarrow=False, align='left',
                       text = title)
    fig.update_layout(height=225, margin={'l': 20, 'b': 30, 'r': 10, 't': 10})
    return fig


@app.callback(
    dash.dependencies.Output('x-time-series', 'figure'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData')])
def update_x_timeseries(hoverData):
    neighborhood_name = hoverData['points'][0]['customdata']
    mydf = df[df['neighborhood']==neighborhood_name].copy()
    elem_school = mydf['main elementary'].unique()[0]
    dff = enroll[enroll['Indicator Name'] == 'Enrollment'].copy()
    dff = dff[dff['School Name']==elem_school]
    title = neighborhood_name+' '+ elem_school
    return create_time_series(dff, title)

@app.callback(
    dash.dependencies.Output('y-time-series', 'figure'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData')])
def update_y_timeseries(hoverData):
    #get neighborhood name from the hover data on the main figure
    neighborhood_name = hoverData['points'][0]['customdata']
    #use neighborhood_name to get the school_name from the areas dataframe
    school_name = df[df['neighborhood']==neighborhood_name]['main elementary'].unique()[0]
    # get the enrollment data for this school_name
    school_name = 'TOTAL'
    dff = enroll[enroll['Indicator Name']=='Enrollment'].copy()
    dff = dff[dff['School Name']==school_name]

    return create_time_series(dff,f'{school_name}')

if __name__ == '__main__':
    app.run_server(debug=True)
