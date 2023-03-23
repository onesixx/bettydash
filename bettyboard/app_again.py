import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html

# from dash import dcc, html
# from dash.dependencies import Input, Output, State

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "https://fonts.googleapis.com/css?family=Montserrat:400,700,200",
    "https://maxcdn.bootstrapcdn.com/font-awesome/latest/css/font-awesome.min.css",
    "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css",
    "assets/css/light-bootstrap-dashboard.css?v=2.0.1",
    "assets/css/demo.css",
    'assets/css/styles.css'
]

external_scripts = [
    {'src': "assets/js/light-bootstrap-dashboard.js?v=2.0.1"},
    {'src': "https://code.jquery.com/jquery-3.3.1.slim.min.js"},
    {'src': "https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"},
    {'src': "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"},
]

app_dash = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

app_dash.title = "Dashboard PRO"
server = app_dash.server



Body = html.Body([
    html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Home", href="#")),
                dbc.NavItem(dbc.NavLink("Company", href="#")),
                dbc.NavItem(dbc.NavLink("Portfolio", href="#")),
                dbc.NavItem(dbc.NavLink("Blog", href="#"))
            ],
            brand="Creative Tim",
            brand_href="http://www.creative-tim.com",
            color="orange",
            dark=True,
        ),
        html.Div([
            html.Div([
                html.A(
                    html.Span("Ct", className="logo-mini"),
                    href="http://www.creative-tim.com",
                    className="simple-text logo-mini"
                ),
                html.A(
                    html.Span("Creative Tim", className="logo-normal"),
                    href="http://www.creative-tim.com",
                    className="simple-text logo-normal"
                )
            ], className="logo")
        ], className="sidebar-wrapper")
    ], className="sidebar", **{'data-color': 'orange', 'data-image': 'assets/img/sidebar-5.jpg'}),
    ])


app_dash.layout = html.Div([sidebar, content]) 

if __name__ == "__main__":
    app_dash.run_server(debug=True, port=8887)
dcc.Lo
