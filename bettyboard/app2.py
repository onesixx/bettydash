from dash.dependencies import Input, Output, State
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

import bettydash
import bettydash.dash_reusable_components as drc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('Click me', id='my-button'),
    dcc.Store(id='my-store')
])

app.clientside_callback(
    """
    function(click_event) {
        alert('My e was executed!');
        console.log(click_event);
    }
    """,
    Output('my-store', 'data'),
    Input('my-button', 'n_clicks'),
    prevent_initial_call=True,
    # specify the js_event property to capture the click event
    # instead of the default 'clickData' property
    js_event='click'
)

if __name__ == '__main__':
    app.run_server(debug=True)
