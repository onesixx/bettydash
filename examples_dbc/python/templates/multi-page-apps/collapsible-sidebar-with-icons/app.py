import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME
    ]
)

sidebar = html.Div(className="sidebar", children=[
    html.Div(className="sidebar-header", children=[
        html.Img(src=PLOTLY_LOGO, style={"width": "3rem"}),
        html.H2("Sidebar"),
    ]),
    html.Hr(),
    dbc.Nav(vertical=True, pills=True, children=[
        dbc.NavLink(href="/", active="exact", children=[
            html.I(className="fas fa-home me-2"), html.Span("Home")
        ]),
        dbc.NavLink(href="/calendar", active="exact", children=[
            html.I(className="fas fa-calendar-alt me-2"),
            html.Span("Calendar"),
        ]),
        dbc.NavLink(href="/calendar", active="exact", children=[
            html.I(className="fas fa-envelope-open-text me-2"),
            html.Span("Messages"),
        ]),
    ]),
])
content = html.Div(
    id="page-content", className="content"
)
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# set the content according to the current pathname


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the home page!")
    elif pathname == "/calendar":
        return html.P("This is your calendar... not much in the diary...")
    elif pathname == "/messages":
        return html.P("Here are all your messages")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(className="p-3 bg-light rounded-3", children=[
        html.H1("404: Not found", className="text-danger"),
        html.Hr(),
        html.P(f"The pathname {pathname} was not recognised..."),
    ])


if __name__ == "__main__":
    app.run_server(debug=True, port=8883)
