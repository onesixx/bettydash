import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

import plotly.express as px
import pandas as pd

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')
available_indicators = df['Indicator Name'].unique()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(
    __name__, 
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        external_stylesheets
    ]
)

app.layout = dbc.Container(
    html.Div([
        dbc.Row(
            dbc.Col( dcc.Graph(id='indicator-graphic'), width="auto" ),
        ),
        dbc.Row([
            dbc.Col( dcc.Slider(id='year--slider',
                        value=df['Year'].max(), min=df['Year'].min(), max=df['Year'].max(),
                        marks={str(year): str(year) for year in df['Year'].unique()},
                        step=None,) )
        ],style={'margin-bottom': '2em'}),
        dbc.Row([
            dbc.Col([
                dbc.Row([
                    dbc.Col(html.Label(['x axis:'], style={'font-weight':'bold', "text-align":"right"}), width="auto"),
                    dbc.Col(dcc.Dropdown(id='xaxis-column',
                                options=[{'label': i, 'value': i} for i in available_indicators],
                                value='Fertility rate, total (births per woman)',
                                searchable=False,
                                clearable=False,
                            ))
                ]),
                dbc.Row(
                    dbc.Col(dcc.RadioItems(id='xaxis-type',
                        options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                        value='Linear',
                        labelStyle={'display':'inline-block', 'padding':"6px 16px 6px 6px"}
                    ), width={"size":"auto", "offset":3})
                )
            ],width=5),
            dbc.Col([
                dbc.Row([
                    dbc.Col(html.Label(['y axis:'], style={'font-weight':'bold', "text-align":"right"}), width="auto"),
                    dbc.Col(dcc.Dropdown(id='yaxis-column',
                                options=[{'label': i, 'value': i} for i in available_indicators],
                                value='Life expectancy at birth, total (years)',
                                searchable=False,
                                clearable=False
                            ))
                ]),
                dbc.Row(
                    dbc.Col(dcc.RadioItems(id='yaxis-type',
                                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                                value='Linear',
                                labelStyle={'display':'inline-block', 'padding':"6px 16px 6px 6px"}
                            ), width={"size":"auto", "offset":3})
                )
            ],width={"size":5, "offset":1}),
        ]),
    ])
)

@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value'),
     Input('xaxis-type',   'value'),
     Input('yaxis-type',   'value'),
     Input('year--slider', 'value')]
)
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type, year_value):
    dff = df[df['Year'] == year_value]

    fig = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
                     y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
                     hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    fig.update_xaxes(title=xaxis_column_name,
                     type='linear' if xaxis_type == 'Linear' else 'log')
    fig.update_yaxes(title=yaxis_column_name,
                     type='linear' if yaxis_type == 'Linear' else 'log')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)