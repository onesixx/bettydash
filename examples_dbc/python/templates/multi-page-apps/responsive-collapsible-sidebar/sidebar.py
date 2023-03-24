import dash
from dash import Input, Output, State, dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    # these meta_tags ensure content is scaled correctly on different devices
    # see: https://www.w3schools.com/css/css_rwd_viewport.asp for more
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

# we use the Row and Col components to construct the sidebar header
# it consists of a title, and a toggle, the latter is hidden on large screens
sidebar_header = dbc.Row([
    dbc.Col(
        html.P("1Sidebar1", className="display-4")
    ),
    dbc.Col(width="auto",  align="center", children=[
        html.Button(id="navbar-toggle", className="navbar-toggler", style={"color": "rgba(0,0,0,.5)", "border-color": "rgba(0,0,0,.1)", }, children=[
            "bb", html.Span(className="navbar-toggler-icon"),
        ]),
        html.Button(id="sidebar-toggle", className="navbar-toggler", style={"color": "rgba(0,0,0,.5)", "border-color": "rgba(0,0,0,.1)"}, children=[
            html.Span(className="navbar-toggler-icon"),
        ]),
    ]),
])

sidebar = html.Div(id="sidebar0", children=[
    sidebar_header,
    html.Div(id="blurb", children=[
        html.Hr(),
        html.P("===sidebar===", className="lead",)
    ]),
    dbc.Collapse(id="collapse",  children=[
        dbc.Nav(vertical=False, pills=False, children=[
            dbc.NavLink("home",   href="/", active="exact"),
            dbc.NavLink("menu1", href="/page-1", active="exact"),
            dbc.NavLink("menu2", href="/page-2", active="exact"),
        ]),
    ]),
])

content = html.Div(id="page-content")

app.layout = html.Div(children=[
    dcc.Location(id="urlpath"),
    sidebar,
    content]
)
app.layout = html.Div(className="sidebar-mini", id="sidebar",  children=[
    html.Div(className="wrapper", children=[
        dcc.Location(id="urlpath"),
        sidebar,
        content
    ])
])


@app.callback(
    Output("page-content", "children"),
    [Input("urlpath", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the HOME page!")
    elif pathname == "/page-1":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return html.Div(className="p-3 bg-light rounded-3", children=[
        html.H1("404: Not found", className="text-danger"),
        html.Hr(),
        html.P(f"The pathname {pathname} was not recognised..."),
    ])


@app.callback(
    Output("sidebar", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className")],
)
def toggle_classname(n, classname):
    if n and classname == "":
        return "collapsed"
    return ""


@app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open_yn):
    if n:
        return not is_open_yn
    return is_open_yn


if __name__ == "__main__":
    app.run_server(port=8882, debug=True)
