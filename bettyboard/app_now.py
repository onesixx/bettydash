import dash
from dash import Input, Output, State, dcc, html
import dash_bootstrap_components as dbc

# https://dash-bootstrap-components.opensource.faculty.ai/docs/
# https://dash.plotly.com/dash-core-components

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME,
        # 'assets/sixx.css'
    ],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

server = app.server

sidebar_header = html.Div(className="logo", style={'display': 'flex',  'align-items': "center", "justify-content": "center", }, children=[
    html.Img(src="assets/logo_small.png",
             style={'display': 'flex',  'align-items': "center", "justify-content": "center", 'padding': '15px 0'},),
    html.A(href="http://onesixx.com", style={},
           className="simple-text logo-normal", children="BECOM"),
])
sidebar_user = dbc.Nav(className="user", vertical=True, pills=True, children=[
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
        html.Div(className="collapse", id="collapseExample", children=[
            html.Ul(className="nav", children=[
                html.Li(
                    html.A(href="#pablo", children=[
                                html.Span("MP", className="sidebar-mini"),
                                html.Span("My Profile",
                                          className="sidebar-normal")
                    ])
                ),
                html.Li(
                    html.A(href="#pablo", children=[
                                html.Span("EP", className="sidebar-mini"),
                                html.Span("Edit Profile",
                                          className="sidebar-normal")
                    ])
                ),
                html.Li(
                    html.A(href="#pablo", children=[
                                html.Span("S", className="sidebar-mini"),
                                html.Span(
                                    "Settings", className="sidebar-normal")
                    ]),
                )
            ]),
        ])
    ])
])

sidebar = html.Div(className="sidebar", **{"data-color": "orange", "data-image": "assets/img/sidebar-5.jpg", }, children=[
    html.Div(className="sidebar-wrapper", children=[
        sidebar_header,
        # sidebar_user,
        ###### NAV ######
        dbc.Collapse(id="collapse",  className="nav", children=[
            # html.Div(className="nav", children=[
            ###### dashboard ######
            dbc.Nav(className="nav-item", vertical=True, pills=True, children=[
                dbc.NavLink(className="nav-link", active="exact", href="/",  # href="./dashboard.html",
                    children=[
                        html.I(className="nc-icon nc-chart-pie-35",
                               style={'margin-top': '0'}),
                        html.Span(children="Dashboard"),
                    ]),
                dbc.NavLink(href="/page-1", active="exact", children=[
                    html.I(className="fas fa-calendar-alt me-2"),
                    html.Span("Calendar"),
                ]),
                dbc.NavLink(href="/page-2", active="exact", children=[
                    html.I(className="fas fa-envelope-open-text me-2"),
                    html.Span("Messages"),
                ])
            ]),
            ###### Form ######
            # dbc.Nav(className="nav", vertical=True, pills=True, children=[
            #         dbc.NavItem(className="nav-item", children=[
            #             dbc.NavLink(className="nav-link", href="#", children=[
            #                 html.I(className="nc-icon nc-notes"),
            #                 "Forms",
            #                 html.B(className="caret")
            #             ],
            #                 id="formsExamples",
            #                 # data_toggle="collapse"
            #             )
            #         ]),
            #         dbc.Collapse(id="formsExamples_collapse", children=[
            #             dbc.Nav(className="nav", vertical=True, pills=True, children=[
            #                 dbc.NavItem(className="nav-item", children=[
            #                     dbc.NavLink(className="nav-link", href="./forms/regular.html", children=[
            #                         html.Span(
            #                             "Rf", className="sidebar-mini"),
            #                         html.Span("Regular Forms",
            #                                   className="sidebar-normal")
            #                     ],
            #                     )
            #                 ]),
            #                 dbc.NavItem(className="nav-item", children=[
            #                     dbc.NavLink(className="nav-link", href="./forms/extended.html", children=[
            #                         html.Span(
            #                             "Ef", className="sidebar-mini"),
            #                         html.Span("Extended Forms",
            #                                   className="sidebar-normal")
            #                     ],
            #                     )
            #                 ]),
            #             ]),
            #         ]),
            #         ]),

            # ])
        ])
    ])
])

navbar_right = dbc.Collapse(navbar=True, children=[
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
])


navbar = dbc.Navbar(className="navbar-expand-lg", color="light", dark=False,  children=[
    html.Div(className="container-fluid", children=[
        html.Div(className="navbar-wrapper",  children=[
            html.Div(className="navbar-minimize", children=[

                dbc.Button(className="btn btn-warning btn-fill btn-round btn-icon d-none d-lg-block", id="sidebar-toggle",  # id="minimizeSidebar",
                           children=[
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
        # navbar_right,
    ]),
])


content_home = dbc.Row(className="row", children=[
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
])

content = html.Div(className="content", children=[
    html.Div(id="page-content", className="container-fluid", children=[
        # content_home
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

app.layout = html.Div(className="sidebar-mini", id="mybody",  children=[
    html.Div(className="wrapper", children=[
        dcc.Location(id="urlpath"),
        sidebar,
        main
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
    Output("mybody", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("mybody", "className")],
)
def toggle_classname(n, classname):
    print(f"classname: {classname}")
    if n and classname == "":
        return "sidebar-mini"
    return ""  # removeClass('sidebar-mini')


# @app.callback(
#     Output("collapse", "is_open"),
#     [Input("navbar-toggle", "n_clicks")],
#     [State("collapse", "is_open")],
# )
# def toggle_collapse(n, is_open_yn):
#     if n:
#         return not is_open_yn
#     return is_open_yn


if __name__ == "__main__":
    app.run_server(debug=True, port=8881)
