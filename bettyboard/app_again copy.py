import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html

app = dash.Dash(
    __name__, 
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME
    ]
)

server = app.server

sidebar = html.Div(className="sidebar", **{"data-color": "orange", "data-image": "assets/img/sidebar-5.jpg", }, children=[
    html.Div(className="sidebar-wrapper", children=[
        ###### LOGO ######
        html.Div(className="logo", style={'display': 'flex',  'align-items': "center","justify-content": "center", 'padding' :'10px'}, children=[
            html.Img(#href="http://www.creative-tim.com",
                    src="assets/logo_small.png", style={'display': 'inline-block'}
                ),
                       #className="simple-text logo-mini"), #, children="Ct"),
            html.A(href="http://www.creative-tim.com", 
                   style={'display': 'inline-block', 'box-sizing': 'border-box', 'padding': '10px'},
                   className="simple-text logo-normal", children="Creative Tim"),
        ]),
        ###### USER ######
        dbc.Nav(className="user", vertical=True, pills=True, children=[
            html.Div(className="photo", children=[
                html.Img(src="assets/user-01.jpg")
            ]),
            html.Div(className="info", children=[
                html.A(
                    html.Span([
                        "Tania Andrew",
                        html.B("", className="caret")
                    ]),
                    # href="#A",
                    className="collapsed",
                    **{"data-toggle": "collapse", "href": "#collapseExample"}
                ),
                html.Div(
                    html.Ul([
                        html.Li(
                            html.A([
                                html.Span(
                                    "MP", className="sidebar-mini"),
                                html.Span("My Profile",
                                          className="sidebar-normal")
                            ], href="#pablo"),
                        ),
                        html.Li(
                            html.A([
                                html.Span(
                                    "EP", className="sidebar-mini"),
                                html.Span("Edit Profile",
                                          className="sidebar-normal")
                            ], href="#pablo"),
                        ),
                        html.Li(
                            html.A([
                                html.Span(
                                    "S", className="sidebar-mini"),
                                html.Span(
                                    "Settings", className="sidebar-normal")
                            ], href="#pablo"),
                        )
                    ], className="nav"),
                    className="collapse",
                    id="collapseExample"
                )
            ])
        ]),
        ###### NAV ######
        html.Div(className="nav", children=[
            ###### dashboard ######
            dbc.Nav(className="nav-item", children=[
                dbc.NavLink(className="nav-link", href="./dashboard.html", children=[
                    html.I(className="nc-icon nc-chart-pie-35"),
                    html.P(children="Dashboard"),
                ]),
            ]),
            ###### Form ######
            dbc.Nav(className="nav", vertical=True, pills=True, children=[
                dbc.NavItem(className="nav-item", children=[
                    dbc.NavLink(className="nav-link", href="#", children=[
                            html.I(className="nc-icon nc-notes"),
                            "Forms",
                            html.B(className="caret")
                            ],
                        id="formsExamples",
                        # data_toggle="collapse"
                    )
                ]),
                dbc.Collapse(id="formsExamples_collapse", children=[
                    dbc.Nav(className="nav", vertical=True, pills=True, children=[
                        dbc.NavItem(className="nav-item", children=[
                            dbc.NavLink(className="nav-link", href="./forms/regular.html", children=[
                                    html.Span(
                                        "Rf", className="sidebar-mini"),
                                    html.Span("Regular Forms",
                                              className="sidebar-normal")
                                    ],
                            )
                        ]),
                        dbc.NavItem(className="nav-item", children=[
                            dbc.NavLink(className="nav-link", href="./forms/extended.html", children=[
                                    html.Span(
                                        "Ef", className="sidebar-mini"),
                                    html.Span("Extended Forms",
                                              className="sidebar-normal")
                                    ],
                            )
                        ]),
                    ]),
                ]),
            ]),
        ]),
    ])
])

navbar = dbc.Navbar(className="navbar-expand-lg", color="light", dark=False,  children=[
    html.Div(className="container-fluid", children=[
        html.Div(className="navbar-wrapper",  children=[
            html.Div(className="navbar-minimize", children=[
                dbc.Button(className="btn btn-warning btn-fill btn-round btn-icon d-none d-lg-block", id="minimizeSidebar", children=[
                    html.I(
                        className="fa fa-ellipsis-v visible-on-sidebar-regular"),
                    html.I(
                        className="fa fa-navicon visible-on-sidebar-mini"),
                ]),
            ]),
            html.A("Dashboard PRO", className="navbar-brand", href="#pablo")
        ]),

        dbc.Button(
            className="navbar-toggler navbar-toggler-right", 
            # type="button" data-toggle="collapse"
            # aria-controls="navigation-index" aria-expanded="false" aria-label="Toggle navigation"
            children=[
                html.Span(className="navbar-toggler-bar burger-lines"),
                html.Span(className="navbar-toggler-bar burger-lines"),
                html.Span(className="navbar-toggler-bar burger-lines"),
            ]
        ),
        dbc.Collapse(navbar=True, children=[
            html.Div(className="collapse navbar-collapse justify-content-end", children=[
                html.Ul(className="nav navbar-nav mr-auto", children=[
                    # html.Form(className="navbar-form navbar-left navbar-search-form", role="search", children=[
                    #     html.Div(className="input-group", children=[
                    #         html.I(className="nc-icon nc-zoom-split"),
                    #         dbc.Input(className="form-control", type="text", placeholder="Search...")
                    #     ]),
                    # ]),
                ]),

                dbc.Nav(navbar=True, children=[
                    dbc.DropdownMenu(
                        label=html.I(className="nc-icon nc-planet"), 
                        nav=True, in_navbar=True, children=[
                            dbc.DropdownMenuItem("Create New Post", href="#"),
                            dbc.DropdownMenuItem("Manage Something", href="#"),
                            dbc.DropdownMenuItem("Do Nothing", href="#"),
                            dbc.DropdownMenuItem("Submit to live", href="#"),
                            dbc.DropdownMenuItem(divider=True),
                            dbc.DropdownMenuItem("Another action", href="#"),
                    ]),
                    dbc.DropdownMenu(
                        label=[
                            html.I(className="nc-icon nc-bell-55"),
                            html.Span("5", className="notification"),
                            html.Span("Notification", className="d-lg-none"),
                        ],
                        nav=True, in_navbar=True, children=[
                            dbc.DropdownMenuItem("Notification 1", href="#"),
                            dbc.DropdownMenuItem("Notification 2", href="#"),
                            dbc.DropdownMenuItem("Notification 3", href="#"),
                            dbc.DropdownMenuItem("Notification 4", href="#"),
                    ]),
                    dbc.DropdownMenu(
                        label=html.I(className="nc-icon nc-bullet-list-67"), 
                        nav=True, in_navbar=True, align_end=True, children=[
                        dbc.DropdownMenuItem(href="#", children=[
                            html.I(className="nc-icon nc-email-85"),
                            " Messages",
                        ]),
                        dbc.DropdownMenuItem(divider=True),
                        dbc.DropdownMenuItem(href="#", children=[
                            html.I(className="nc-icon nc-lock-circle-open"),
                            " Lock Screen",
                        ]),
                        dbc.DropdownMenuItem(className="text-danger", href="#", children=[
                            html.I(className="nc-icon nc-button-power"),
                            " Log out",
                        ]),
                    ]),
                ]),
            ]),
        ]),
    ]),
])


content = html.Div(className="content", children=[
    html.Div(className="container-fluid", children=[
        dbc.Row(className="row", children=[
            dbc.Col(lg=3, sm=6, children=[
                dbc.Card(className="card-stats", children=[
                    dbc.CardBody(children=[
                        html.Div(className="row", children=[
                            dbc.Col(width=5,  children=[
                                html.Div(className="icon-big text-center icon-warning",  children=[
                                    html.I(
                                        className="nc-icon nc-chart text-warning"),
                                ]),
                            ]),
                            dbc.Col(width=7, children=[
                                html.Div(className="numbers", children=[
                                    html.P(className="card-category",
                                           children="Number"),
                                    html.H4(className="card-title",
                                            children="150GB"),
                                ])
                            ]),
                        ]),
                    ]),
                    dbc.CardFooter(children=[
                        html.Hr(),
                        html.Div(className="stats", children=[
                            html.I(className="fa fa-refresh"),
                            " Update Now",
                        ],
                        ),
                    ]),
                ]),
            ]),
        ]),
    ]),
])

footer = html.Footer(className="footer", children=[
    html.Div(className="container", children=[
        html.Nav(children=[
            html.Ul(className="footer-menu", children=[
                html.Li(html.A("Home", href="#")),
                html.Li(html.A("Company", href="#")),
                html.Li(html.A("Portfolio", href="#")),
                html.Li(html.A("Blog", href="#")),
            ]),
            html.P(className="copyright text-center", children=[
                "©",
                html.Script(
                    children="document.write(new Date().getFullYear())"
                ),
                html.A("BECOM",
                       href="http://onesixx.com"),
                ", made with love for a better solution",
            ]),
        ]),
    ]),
])

main = html.Div(className="main-panel", children=[
    navbar,
    content,
    footer
])

app.layout = html.Div(className="wrapper", children=[
    sidebar,
    main
],)

if __name__ == "__main__":
    app.run_server(debug=True, port=8886)
