import dash
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('Click me!', id='my-button'),
    html.Div(id='output')
])


@app.callback(
    Output('output', 'children'),
    Input('my-button', 'n_clicks')
)
def update_output(n_clicks):
    return f'The button has been clicked {n_clicks} times.'


app.clientside_callback(
    """
    function(n_clicks) {
        console.log('The button has been clicked ' + n_clicks + ' times.');
        var script = document.createElement('script');
        script.src = 'custom_script.js';
        document.head.appendChild(script);
    }
    """,
    Output('output', 'children'),
    Input('my-button', 'n_clicks')
)

if __name__ == '__main__':
    app.run_server(debug=True)
