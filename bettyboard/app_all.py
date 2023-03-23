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


nav = html.Div(
    [
        dbc.Nav(
            [
                dbc.NavItem(
                    dbc.NavLink(
                        [
                            html.I(className="nc-icon nc-chart-pie-35"),
                            html.P("Dashboard"),
                        ],
                        href="./dashboard.html",
                    ),
                    className="nav-item ",
                ),
                dbc.NavItem(
                    [
                        dbc.NavLink(
                            [
                                html.I(className="nc-icon nc-app"),
                                html.P(
                                    [
                                        "Components",
                                        html.B(className="caret"),
                                    ]
                                ),
                            ],
                            href="#",
                            className="nav-link",
                            id="componentsExamples",
                            role="button",
                        ),
                        dbc.Collapse(
                            [
                                dbc.Nav(
                                    [
                                        dbc.NavItem(
                                            dbc.NavLink(
                                                [
                                                    html.Span(
                                                        "B",
                                                        className="sidebar-mini",
                                                    ),
                                                    html.Span(
                                                        "Buttons",
                                                        className="sidebar-normal",
                                                    ),
                                                ],
                                                href="./components/buttons.html",
                                            ),
                                            className="nav-item ",
                                        ),
                                        dbc.NavItem(
                                            dbc.NavLink(
                                                [
                                                    html.Span(
                                                        "GS",
                                                        className="sidebar-mini",
                                                    ),
                                                    html.Span(
                                                        "Grid System",
                                                        className="sidebar-normal",
                                                    ),
                                                ],
                                                href="./components/grid.html",
                                            ),
                                            className="nav-item ",
                                        ),
                                        dbc.NavItem(
                                            dbc.NavLink(
                                                [
                                                    html.Span(
                                                        "P",
                                                        className="sidebar-mini",
                                                    ),
                                                    html.Span(
                                                        "Panels",
                                                        className="sidebar-normal",
                                                    ),
                                                ],
                                                href="./components/panels.html",
                                            ),
                                            className="nav-item ",
                                        ),
                                        dbc.NavItem(
                                            dbc.NavLink(
                                                [
                                                    html.Span(
                                                        "SA",
                                                        className="sidebar-mini",
                                                    ),
                                                    html.Span(
                                                        "Sweet Alert",
                                                        className="sidebar-normal",
                                                    ),
                                                ],
                                                href="./components/sweet-alert.html",
                                            ),
                                            className="nav-item ",
                                        ),
                                        dbc.NavItem(
                                            dbc.NavLink(
                                                [
                                                    html.Span(
                                                        "N",
                                                        className="sidebar-mini",
                                                    ),
                                                    html.Span(
                                                        "Notifications",
                                                        className="sidebar-normal",
                                                    ),
                                                ],
                                                href="./components/notifications.html",
                                            ),
                                            className="nav-item ",
                                        ),
                                        dbc.NavItem(
                                            dbc.NavLink(
                                                [
                                                    html.Span(
                                                        "I",
                                                        className="sidebar-mini",
                                                    ),
                                                    html.Span(
                                                        "Icons",
                                                        className="sidebar-normal",
                                                    ),
                                                ],
                                                href="./components/icons.html",
                                            ),
                                            className="nav-item ",
                                        ),
                                        dbc.NavItem(
                                            dbc.NavLink(
                                                [
                                                    html.Span(
                                                        "T",
                                                        className="sidebar-mini",
                                                    ),
                                                    html.Span(
                                                        "Typography",
                                                        className="sidebar-normal",
                                                    ),
                                                ],
                                                href="./components/typography.html",
                                            ),
                                            className="nav-item ",
                                        ),
                                    ],
                                    navbar=True,
                                )
                            ],
                            id="componentsExamples",
                            is_open=False,
                        ),
                    ],
                    className="nav-item",
                ),
                dbc.NavItem(
                    dbc.NavLink(
                        [
                            html.I(className="nc-icon nc-puzzle-10"),
                            "Pages",
                            html.B(className="caret"),
                        ],
                        href="#",
                        id="page-examples-dropdown",
                    ),
                    className="nav-item",
                ),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavItem(
                                dbc.NavLink(
                                    [
                                        html.Span(
                                            "LP", className="sidebar-mini"),
                                        html.Span(
                                            "Login Page", className="sidebar-normal"),
                                    ],
                                    href="./pages/login.html",
                                ),
                                className="nav-item",
                            ),
                            dbc.NavItem(
                                dbc.NavLink(
                                    [
                                        html.Span(
                                            "RP", className="sidebar-mini"),
                                        html.Span(
                                            "Register Page", className="sidebar-normal"),
                                    ],
                                    href="./pages/register.html",
                                ),
                                className="nav-item",
                            ),
                            dbc.NavItem(
                                dbc.NavLink(
                                    [
                                        html.Span(
                                            "LSP", className="sidebar-mini"),
                                        html.Span(
                                            "Lock Screen Page", className="sidebar-normal"),
                                    ],
                                    href="./pages/lock.html",
                                ),
                                className="nav-item",
                            ),
                            dbc.NavItem(
                                dbc.NavLink(
                                    [
                                        html.Span(
                                            "UP", className="sidebar-mini"),
                                        html.Span(
                                            "User Page", className="sidebar-normal"),
                                    ],
                                    href="./pages/user.html",
                                ),
                                className="nav-item",
                            ),
                            dbc.NavItem(
                                dbc.NavLink(
                                    [
                                        html.Span(
                                            "MCS", className="sidebar-mini"),
                                        html.Span(
                                            "More coming soon...", className="sidebar-normal"),
                                    ],
                                    href="#lbd",
                                ),
                                className="nav-item",
                            ),
                        ],
                        className="navbar-nav",
                        navbar=True,
                    ),
                    id="pages-examples-dropdown",
                ),
            ],
            className="ml-auto",
            navbar=True,
        ),
        id="navbar-collapse",
        navbar=True,
    ),
],
className = "navbar navbar-expand-lg navbar-transparent navbar-absolute",
)



navbar = dbc.Navbar(
    [
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Row(
            [
                dbc.Col(
                    html.A(
                        dbc.Row(
                            [
                                dbc.Col(html.I(className="fa fa-ellipsis-v visible-on-sidebar-regular")),
                                dbc.Col(html.I(className="fa fa-navicon visible-on-sidebar-mini")),
                            ],
                            align="center",
                            no_gutters=True,
                        ),
                        href="#",
                        id="toggle-sidebar",
                    ),
                    width="auto",
                    lg={"size": 1},
                ),
                dbc.Col(html.A("Dashboard PRO", className="navbar-brand"), lg={"size": 3, "offset": 1}),
                dbc.Col(
                    dbc.Nav(
                        [
                            dbc.Form(
                                [
                                    dbc.Input(type="search", placeholder="Search...", className="form-control"),
                                    dbc.Button(
                                        html.I(className="nc-icon nc-zoom-split"),
                                        color="warning",
                                        className="btn-round btn-just-icon",
                                    ),
                                ],
                                inline=True,
                            ),
                        ],
                        navbar=True,
                    ),
                    width="auto",
                    lg={"size": 3},
                ),
                dbc.Col(
                    dbc.Nav(
                        [
                            dbc.DropdownMenu(
                                [
                                    dbc.DropdownMenuItem("Create New Post"),
                                    dbc.DropdownMenuItem("Manage Something"),
                                    dbc.DropdownMenuItem("Do Nothing"),
                                    dbc.DropdownMenuItem("Submit to live"),
                                    dbc.DropdownMenuItem(divider=True),
                                    dbc.DropdownMenuItem("Another action"),
                                ],
                                label=html.I(className="nc
                                             
# main-panel


#<!--=================== content =================================-->
content = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.I(
                                                        className="nc-icon nc-chart text-warning",
                                                    ),
                                                ],
                                                className="icon-big text-center icon-warning",
                                            ),
                                            html.Div(
                                                [
                                                    html.P(
                                                        "Number",
                                                        className="card-category",
                                                    ),
                                                    html.H4("150GB", className="card-title"),
                                                ],
                                                className="numbers",
                                            ),
                                        ],
                                        className="row",
                                    ),
                                ]
                            ),
                            dbc.CardFooter(
                                [
                                    html.Hr(),
                                    html.Div(
                                        [
                                            html.I(className="fa fa-refresh"),
                                            " Update Now",
                                        ],
                                        className="stats",
                                    ),
                                ]
                            ),
                            className="card-stats",
                        ),
                    ],
                    lg=3,
                    sm=6,
                ),
            ],
        ),
    ],
    fluid=True,
    className="content",
)




# Create the sidebar
sidebar = html.Div(
    [
        html.Div(
            [
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src="/assets/img/default-avatar.png", height="50px")),
                            dbc.Col(
                                html.Span("Tania Andrew", className="sidebar-user-name ml-2"),
                            ),
                        ],
                        align="center",
                    ),
                    href="#",
                ),
                html.Hr(),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavLink("My Profile", href="#", id="page-1-link"),
                            dbc.NavLink("Edit Profile", href="#", id="page-2-link"),
                            dbc.NavLink("Settings", href="#", id="page-3-link"),
                        ],
                        vertical=True,
                        pills=True,
                    ),
                    id="sidebar-collapse",
                ),
            ],
            className="sidebar",
        )
    ]
)

# Create the main content

content = html.Div(
    [
        html.Div(
            [
                html.A(
                    html.Img(src="/assets/img/default-avatar.png", height="50px"),
                    href="#",
                    className="photo",
                ),
                html.Div(
                    [
                        html.Span("Tania Andrew", className="user-name"),
                        html.A(html.I(className="fa fa-caret-down"), href="#collapseExample", className="collapsed", data_toggle="collapse"),
                    ],
                    className="info",
                ),
                html.Div(
                    [
                        html.Ul(
                            [
                                html.Li(html.A(html.Span("My Profile", className="sidebar-normal"), href="#")),
                                html.Li(html.A(html.Span("Edit Profile", className="sidebar-normal"), href="#")),
                                html.Li(html.A(html.Span("Settings", className="sidebar-normal"), href="#")),
                            ],
                            className="nav",
                        ),
                        html.Div("", className="clearfix"),
                    ],
                    id="collapseExample",
                    className="collapse",
                ),
            ],
            className="user",
        ),
    ]
)

footer = html.Footer(
    dbc.Container(
        html.Nav(
            [
                html.Ul(
                    [
                        html.Li(
                            html.A(
                                "Home",
                                href="#",
                            ),
                        ),
                        html.Li(
                            html.A(
                                "Company",
                                href="#",
                            ),
                        ),
                        html.Li(
                            html.A(
                                "Portfolio",
                                href="#",
                            ),
                        ),
                        html.Li(
                            html.A(
                                "Blog",
                                href="#",
                            ),
                        ),
                    ],
                    className="footer-menu",
                ),
                html.P(
                    [
                        "©",
                        html.Script(
                            f"document.write(new Date().getFullYear())"
                        ),
                        html.A(
                            "Creative Tim",
                            href="http://www.creative-tim.com",
                        ),
                        ", made with love for a better web",
                    ],
                    className="copyright",
                    style={"text-align": "center"},
                ),
            ],
        ),
    ),
    className="footer",
)

Body=html.Div([
    html.Body([
        html.Div([
            dbc.NavbarSimple(
                children=[
                    dbc.NavItem(dbc.NavLink(
                        "Home", href="#")),
                    dbc.NavItem(dbc.NavLink(
                        "Company", href="#")),
                    dbc.NavItem(dbc.NavLink(
                        "Portfolio", href="#")),
                    dbc.NavItem(
                        dbc.NavLink("Blog", href="#"))
                ],
                brand="Creative Tim",
                brand_href="http://www.creative-tim.com",
                color="orange",
                dark=True,
            ),
            html.Div([
                html.Div([
                    html.A(
                        html.Span(
                            "Ct", className="logo-mini"),
                        href="http://www.creative-tim.com",
                        className="simple-text logo-mini"
                    ),
                    html.A(
                        html.Span(
                            "Creative Tim", className="logo-normal"),
                        href="http://www.creative-tim.com",
                        className="simple-text logo-normal"
                    )
                ], className="logo")
            ], className="sidebar-wrapper")
        ], className="sidebar", **{'data-color': 'orange', 'data-image': 'assets/img/sidebar-5.jpg'}),
    ])
])

app.layout = html.Div([sidebar, content])



app_dash.layout = html.Div(className="wrapper", children=[
    html.Meta(charSet="utf-8"),
    html.Div(className="sidebar",
        **{"data-color": "orange",
        "data-image": "assets/img/sidebar-5.jpg"}, children=[
            html.Div(className="sidebar-wrapper", children=[
                html.Div(className="logo", children=[
                    html.A(href="http://onesixx.com", className="simple-text logo-mini", children=[
                        "Ct"
                    ])
                ])
            ])
        ]
    ),
    html.Div(className="main-panel", children=[
        html.Nav(className="navbar navbar-expand-lg", children=[
            html.Div(className="container-fluid", children=[
                html.Div(className="navbar-wrapper", children=[
                    html.Div(className="navbar-minimize", children=[
                        html.Button(
                            id="minimizeSidebar",
                            className="btn btn-warning btn-fill btn-round btn-icon d-none d-lg-block", children=[
                                html.I(
                                    className="fa fa-ellipsis-v visible-on-sidebar-regular"),
                                html.I(
                                    className="fa fa-navicon visible-on-sidebar-mini")
                            ]
                        )
                    ]),
                    html.A(className="navbar-brand", href="#pablo", children=[
                        "Dashboard PRO"
                    ])
                ])
            ])
        ]),
        html.Div(className="content", children=[
            html.Div(className="container-fluid", children=[
                html.Div(className="row", children=[
                    html.Div(
                        className="col-lg-3 col-sm-6")
                ])
            ])
        ]),
        html.Footer(className="footer", children=[
            html.Div(className="container", children=[
                html.Nav(children=[
                    html.Ul(className="footer-menu", children=[
                        html.Li(children=[
                            html.A(href="#", children=[
                                "Home"
                            ])
                        ])
                    ]),
                    html.P(className="copyright text-center", children=[
                        "\xa9",
                        html.Script(children=[
                            "document.write(new Date().getFullYear())"
                        ]),
                        html.A(href="http://www.creative-tim.com", children=[
                            "Creative Tim"
                        ]),
                        ", made with love for a better web"
                    ])
                ])
            ])
        ])
    ]),
])

if __name__ == "__main__":
    app_dash.run_server(debug=True, port=8887)
dcc.Lo
