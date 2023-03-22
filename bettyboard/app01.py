

from dash.dependencies import Input, Output, State
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

import bettydash
import bettydash.dash_reusable_components as drc
# from bettydash.templates import get_layout
# from dash.dependencies import Input, Output
# =============================================================================
# Dash App and Flask Server
# =============================================================================

external_stylesheets = [
    # Collapsed
    'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
    # <!-- Fonts and icons - ->
    "https://fonts.googleapis.com/css?family=Montserrat:400,700,200",
    "https://maxcdn.bootstrapcdn.com/font-awesome/latest/css/font-awesome.min.css",

    "../assets/css/light-bootstrap-dashboard.css?v=2.0.1",
    # "light-bootstrap-dashboard.css",
    # # < link href=rel="stylesheet" / >
    # # <!-- CSS Just for demo purpose, don't include it in your project - ->
    # "demo.css",
    # # <!-- CSS Files - ->
    # "bootstrap.min.css",
]
external_scripts = [
    # collapse
    'https://code.jquery.com/jquery-3.3.1.slim.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js',
    'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js',
    # bootstrap
    '/assets/js/light-bootstrap-dashboard.js?v=2.0.1'
]


# external_scripts = [
#     "../assets/js/core/jquery.3.2.1.min.js",
#     "../assets/js/core/popper.min.js",
#     "../assets/js/core/bootstrap.min.js",
#     "../assets/js/plugins/bootstrap-switch.js",
#     # "https://maps.googleapis.com/maps/api/js?YOUR_KEY_HERE",
#     "../assets/js/plugins/chartist.min.js",
#     "../assets/js/plugins/bootstrap-notify.js",
#     "../assets/js/plugins/jquery-jvectormap.js",
#     "../assets/js/plugins/moment.min.js",
#     "../assets/js/plugins/bootstrap-datetimepicker.js",
#     "../assets/js/plugins/sweetalert2.min.js",
#     "../assets/js/plugins/bootstrap-tagsinput.js",
#     "../assets/js/plugins/bootstrap-selectpicker.js",
#     "../assets/js/plugins/jquery.validate.min.js",
#     "../assets/js/plugins/jquery.bootstrap-wizard.js",
#     "../assets/js/plugins/bootstrap-table.js",
#     "../assets/js/plugins/jquery.dataTables.min.js",
#     "../assets/js/plugins/fullcalendar.min.js",
#     "../assets/js/light-bootstrap-dashboard.js?v=2.0.1",
#     "../assets/js/demo.js",
# ]

app_dash = dash.Dash(
    __name__,
    meta_tags=[
        {"charset": "utf-8",
         "content": "width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0, shrink-to-fit=no",
         "name": "viewport"}
    ],

    #external_stylesheets=['dbc.themes.BOOTSTRAP',  external_stylesheets],
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
    # <head>
    # < link rel="apple-touch-icon" sizes="76x76" href="../assets/img/apple-icon.png" >
    # < link rel="icon" type="image/png"          href="../assets/img/favicon.png" >
    # < meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" / >
    # < /head >
)
app_dash.title = "Betty Dashboard from Light Bootstrap Dashboard"
#server = app_dash.server

# =============================================================================
# App Layout
# =============================================================================


leftitem = html.Div([
    # left top Logo
    html.Div(className='logo', children=[
        html.A(className='simple-text logo-mini',
               href='http://onesixx.com', children=html.Img(src='../assets/logo.png', height=22)),
        html.A(className='simple-text logo-normal',
               href='', children='BECOM')
    ]),
    html.Div(className='user', children=[
        html.Div(className='photo', children=[
            html.Img(src='../assets/img/default-avatar.png')
        ]),
        html.Div(className='info', children=[
            html.A(className='collapsed', href='#collapseExample',  # data_toggle='collapse',
                   children=[
                       html.Span(children=['Tania Andrew',
                                 html.B(className='caret')])
                   ]),
            html.Div(className='collapse', id='collapseExample', children=[
                html.Ul(className='nav', children=[
                    html.Li(children=[
                        html.A(className='profile-dropdown', href='#pablo', children=[
                            html.Span(className='sidebar-mini', children='MP'),
                            html.Span(className='sidebar-normal',
                                      children='My Profile')
                        ])
                    ]),
                    html.Li(children=[
                        html.A(className='profile-dropdown', href='#pablo', children=[
                            html.Span(className='sidebar-mini', children='EP'),
                            html.Span(className='sidebar-normal',
                                      children='Edit Profile')
                        ])
                    ]),
                    html.Li(children=[
                        html.A(className='profile-dropdown', href='#pablo', children=[
                            html.Span(className='sidebar-mini', children='S'),
                            html.Span(className='sidebar-normal',
                                      children='Settings')
                        ])
                    ])
                ])
            ])
        ])
    ])
])

navitem = html.Div([
    html.Ul(className='nav', children=[
        html.Li(className='nav-item', children=[
            html.A(className='nav-link', href='./dashboard.html', children=[
                html.I(className='nc-icon nc-chart-pie-35'),
                html.P('Dashboard')
            ])
        ]),
        html.Li(className='nav-item', children=[
            html.A(className='nav-link',  # data_toggle='collapse',
                   href='#componentsExamples', children=[
                       html.I(className='nc-icon nc-app'),
                       html.P([
                           'Components',
                           html.B(className='caret')
                       ])
                   ]),
            html.Div(className='collapse', id='componentsExamples', children=[
                html.Ul(className='nav', children=[
                    html.Li(className='nav-item', children=[
                        html.A(className='nav-link', href='./components/buttons.html', children=[
                            html.Span(className='sidebar-mini', children='B'),
                            html.Span(className='sidebar-normal',
                                      children='Buttons')
                        ])
                    ]),
                    html.Li(className='nav-item', children=[
                        html.A(className='nav-link', href='./components/grid.html', children=[
                            html.Span(className='sidebar-mini', children='GS'),
                            html.Span(className='sidebar-normal',
                                      children='Grid System')
                        ])
                    ]),
                    html.Li(className='nav-item', children=[
                        html.A(className='nav-link', href='./components/panels.html', children=[
                            html.Span(className='sidebar-mini', children='P'),
                            html.Span(className='sidebar-normal',
                                      children='Panels')
                        ])
                    ]),
                    html.Li(className='nav-item', children=[
                        html.A(className='nav-link', href='./components/sweet-alert.html', children=[
                            html.Span(className='sidebar-mini', children='SA'),
                            html.Span(className='sidebar-normal',
                                      children='Sweet Alert')
                        ])
                    ]),
                    html.Li(className='nav-item', children=[
                        html.A(className='nav-link', href='./components/notifications.html', children=[
                            html.Span(className='sidebar-mini', children='N'),
                            html.Span(className='sidebar-normal',
                                      children='Notifications')
                        ])
                    ]),
                    html.Li(className='nav-item', children=[
                        html.A(className='nav-link', href='./components/icons.html', children=[
                            html.Span(className='sidebar-mini', children='I'),
                            html.Span(className='sidebar-normal',
                                      children='Icons')
                        ])
                    ]),
                    html.Li(className='nav-item', children=[
                        html.A(className='nav-link', href='./components/typography.html', children=[
                            html.Span(className='sidebar-mini', children='T'),
                            html.Span(className='sidebar-normal',
                                      children='Typography')
                        ])
                    ])
                ])
            ])
        ]),

        html.Li(className='nav-item', children=[
            html.A(className='nav-link',  # data_toggle='collapse',
                   href='#formsExamples', children=[
                       html.I(className='nc-icon nc-notes'),
                       html.P([
                           'Forms',
                           html.B(className='caret')
                       ])
                   ]),
            html.Div(className='collapse', id='formsExamples', children=[
                html.Ul(className='nav', children=[
                    html.Li(className='nav-item', children=[
                        html.A(className='nav-link', href='./forms/regular.html', children=[
                            html.Span(className='sidebar-mini', children='Rf'),
                            html.Span(className='sidebar-normal',
                                      children='Regular Forms')
                        ])
                    ]),
                ])
            ]),
        ]),
        # html.Li(className='nav-item', children=[
        #     html.A(className='nav-link', id='formsExamples-toggle', href='#', children=[
        #         html.I(className='nc-icon nc-notes'),
        #         html.P([
        #             'Forms',
        #             html.B(className='caret')
        #         ])
        #     ]),
        #     html.Ul(className='nav', id='formsExamples', children=[
        #         html.Li(className='nav-item', children=[
        #             html.A(className='nav-link', href='./forms/regular.html', children=[
        #                 html.Span(className='sidebar-mini', children='Rf'),
        #                 html.Span(className='sidebar-normal',
        #                           children='Regular Forms')
        #             ])
        #         ]),
        #     ]),
        # ]),
        html.Li([
            html.A([
                html.I(className="nc-icon nc-paper-2"),
                html.P([
                    "Tables",
                    html.B(className="caret")
                ])
            ], className="nav-link", href="#",
                **{'data-toggle': 'collapse',
                   'aria-expanded': 'false',
                   'aria-controls': 'tablesExamples'
                   }
                # **{'data-toggle': 'collapse'},
                # **{'aria-expanded': 'false'},
                # **{'aria-controls': 'tablesExamples'}
            ),
            html.Div([
                html.Ul([
                    html.Li([
                        html.A([
                            html.Span("RT", className="sidebar-mini"),
                            html.Span("Regular Tables",
                                      className="sidebar-normal")
                        ], className="nav-link", href="./tables/regular.html")
                    ], className="nav-item "),
                    html.Li([
                        html.A([
                            html.Span("ET", className="sidebar-mini"),
                            html.Span("Extended Tables",
                                      className="sidebar-normal")
                        ], className="nav-link", href="./tables/extended.html")
                    ], className="nav-item "),
                    html.Li([
                        html.A([
                            html.Span("BT", className="sidebar-mini"),
                            html.Span("Bootstrap Table",
                                      className="sidebar-normal")
                        ], className="nav-link", href="./tables/bootstrap-table.html")
                    ], className="nav-item "),
                    html.Li([
                        html.A([
                            html.Span("DT", className="sidebar-mini"),
                            html.Span("DataTables.net",
                                      className="sidebar-normal")
                        ], className="nav-link", href="./tables/datatables.net.html")
                    ], className="nav-item "),
                ], className="nav")
            ], className="collapse", id="tablesExamples")
        ], className="nav-item"),

        html.Li([
            html.A([
                html.I(className="nc-icon nc-pin-3"),
                html.P([
                    "Maps",
                    html.B(className="caret")
                ])
            ], className="nav-link", href="#", **{'data-toggle': 'collapse'}, **{'aria-expanded': 'false'},
                **{'aria-controls': 'mapsExamples'}),
            html.Div([
                html.Ul([
                    html.Li([
                        html.A([
                            html.Span("GM", className="sidebar-mini"),
                            html.Span("Google Maps",
                                      className="sidebar-normal")
                        ], className="nav-link", href="./maps/google.html")
                    ], className="nav-item "),
                    html.Li([
                        html.A([
                            html.Span("VM", className="sidebar-mini"),
                            html.Span("Vector maps",
                                      className="sidebar-normal")
                        ], className="nav-link", href="./maps/vector.html")
                    ], className="nav-item "),
                    html.Li([
                        html.A([
                            html.Span("FSM", className="sidebar-mini"),
                            html.Span("Full Screen Map",
                                      className="sidebar-normal")
                        ], className="nav-link", href="./maps/fullscreen.html")
                    ], className="nav-item "),
                ], className="nav")
            ], className="collapse", id="mapsExamples")
        ], className="nav-item"),
        html.Li([
            html.A([
                html.I(className="nc-icon nc-chart-bar-32"),
                html.P("Charts")
            ], className="nav-link", href="./charts.html")
        ], className="nav-item "),
        html.Li([
            html.A([
                html.I(className="nc-icon nc-single-copy-04"),
                html.P("Calendar")
            ], className="nav-link", href="./calendar.html")
        ], className="nav-item "),
        html.Li(className='nav-item', children=[
            html.A(className='nav-link', href='#', children=[
                html.I(className='nc-icon nc-puzzle-10'),
                html.P(children=[
                    'Pages',
                    html.B(className='caret')
                ])
            ]),
            html.Div(className='collapse', id='pagesExamples', children=[
                html.Ul(className='nav', children=[
                    html.Li(className='nav-item', children=[
                        html.A(className='nav-link', href='./pages/login.html', children=[
                            html.Span(className='sidebar-mini',
                                      children=['LP']),
                            html.Span(className='sidebar-normal',
                                      children=['Login Page'])
                        ])
                    ]),
                    html.Li(className='nav-item', children=[
                        html.A(className='nav-link', href='./pages/register.html', children=[
                            html.Span(className='sidebar-mini',
                                      children=['RP']),
                            html.Span(className='sidebar-normal',
                                      children=['Register Page'])
                        ])
                    ]),
                    html.Li(className='nav-item', children=[
                        html.A(className='nav-link', href='./pages/lock.html', children=[
                            html.Span(className='sidebar-mini',
                                      children=['LSP']),
                            html.Span(className='sidebar-normal',
                                      children=['Lock Screen Page'])
                        ])
                    ]),
                    html.Li(className='nav-item', children=[
                        html.A(className='nav-link', href='./pages/user.html', children=[
                            html.Span(className='sidebar-mini',
                                      children=['UP']),
                            html.Span(className='sidebar-normal',
                                      children=['User Page'])
                        ])
                    ]),
                    html.Li(className='nav-item', children=[
                        html.A(className='nav-link', href='#lbd', children=[
                            html.Span(className='sidebar-mini',
                                      children=['MCS']),
                            html.Span(className='sidebar-normal',
                                      children=['More coming soon...'])
                        ])
                    ])
                ])
            ])
        ])
    ])
])

navbar = html.Div(className="navbar-wrapper", children=[
    html.Div(className="navbar-minimize", children=[
        html.Button(id="minimizeSidebar", className="btn btn-warning btn-fill btn-round btn-icon d-none d-lg-block",
                    children=[
                        html.I(
                            className="fa fa-ellipsis-v visible-on-sidebar-regular"),
                        html.I(className="fa fa-navicon    visible-on-sidebar-mini")
                    ]),
    ]),
    html.A(className="navbar-brand",
           href="#pablo", children="언넝언넝 해보자")
])

btnbtn = html.Button([
    html.Span(className="navbar-toggler-bar burger-lines"),
    html.Span(className="navbar-toggler-bar burger-lines"),
    html.Span(className="navbar-toggler-bar burger-lines")
], className="navbar-toggler navbar-toggler-right", type="button",
    # aria-controls="navigation-index",
    # aria-expanded=False,
    # aria-label="Toggle navigation"
)

righttop_nav = html.Nav(
    className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top",
    children=[
        html.Div(
            className="container-fluid",
            children=[
                html.Div(
                    className="navbar-wrapper",
                    children=[
                        html.Button(
                            className="navbar-toggler navbar-toggler-right",
                            type="button",
                            **{
                                      "data-toggle": "collapse",
                                      "aria-controls": "navigation-index",
                                      "aria-expanded": "false",
                                      "aria-label": "Toggle navigation",
                            },
                            children=[
                                html.Span(
                                    className="navbar-toggler-bar burger-lines"),
                                html.Span(
                                    className="navbar-toggler-bar burger-lines"),
                                html.Span(
                                    className="navbar-toggler-bar burger-lines"),
                            ],
                        ),
                        html.A(
                            className="navbar-brand",
                            href="#pablo",
                            children="Dashboard PRO",
                        ),
                    ],
                ),
                # html.Div(
                #     className="collapse navbar-collapse justify-content-end",
                #     children=[
                #         html.Ul(
                #             className="nav navbar-nav mr-auto",
                #             children=[
                #                 html.Form(
                #                     className="navbar-form navbar-left navbar-search-form",
                #                     role="search",
                #                     children=[
                #                         html.Div(
                #                             className="input-group",
                #                             children=[
                #                                 html.I(
                #                                     className="nc-icon nc-zoom-split"
                #                                 ),
                #                                 # html.Input(
                #                                 #     type="text",
                #                                 #     value="",
                #                                 #     className="form-control",
                #                                 #     placeholder="Search...",
                #                                 # ),
                #                             ],
                #                         ),
                #                     ],
                #                 ),
                #             ],
                #         ),
                #         html.Ul(
                #             className="navbar-nav",
                #             children=[
                #                 html.Li(
                #                     className="dropdown nav-item",
                #                     children=[
                #                         html.A(
                #                             className="dropdown-toggle nav-link",
                #                             href="#",
                #                             **{"data-toggle": "dropdown"},
                #                             children=[
                #                                 html.I(
                #                                     className="nc-icon nc-planet"
                #                                 ),
                #                             ],
                #                         ),
                #                         html.Ul(
                #                             className="dropdown-menu",
                #                             children=[
                #                                 html.A(
                #                                     className="dropdown-item",
                #                                     href="#",
                #                                     children="Create New Post",
                #                                 ),
                #                                 html.A(
                #                                     className="dropdown-item",
                #                                     href="#",
                #                                     children="Manage Something",
                #                                 ),
                #                                 html.A(
                #                                     className="dropdown-item",
                #                                     href="#",
                #                                     children="Do Nothing",
                #                                 ),
                #                                 html.A(
                #                                     className="dropdown-item",
                #                                     href="#",
                #                                     children="Submit to live",
                #                                 ),
                #                                 html.Li(
                #                                     className="divider",
                #                                 ),
                #                                 html.A(
                #                                     className="dropdown-item",
                #                                     href="#",
                #                                     children="Another action",
                #                                 ),
                #                             ],
                #                         ),
                #                     ],
                #                 ),
                #                 html.Li(
                #                     className="dropdown nav-item",
                #                     children=[
                #                         html.A(
                #                             className="dropdown-toggle nav-link",
                #                             href="#",
                #                             **{"data-toggle": "dropdown"},
                #                             children=[
                #                                 html.I(
                #                                     className="nc-icon nc-bell-55"
                #                                 ),
                #                                 html.Span(
                #                                     className="notification",
                #                                     children="5",
                #                                 ),
                #                                 html.Span(
                #                                     className="d-lg-none",
                #                                     children="Notification",
                #                                 ),
                #                             ],
                #                         ),
                #                         html.Ul(
                #                             className="dropdown-menu",
                #                             children=[
                #                                 html.A(
                #                                     className="dropdown-item",
                #                                     href="#",
                #                                     children="Notification 1",
                #                                 ),
                #                                 html.A(
                #                                     className="dropdown-item",
                #                                     href="#",
                #                                     children="Notification 2",
                #                                 ),
                #                                 html.A(
                #                                     className="dropdown-item",
                #                                     href="#",
                #                                     children="Notification 3",
                #                                 ),
                #                                 html.A(
                #                                     className="dropdown-item",
                #                                     href="#",
                #                                     children="Notification 4",
                #                                 ),
                #                             ]
                #                         )
                #                     ]
                #                 )
                #             ]
                #         )
                #     ]
                # )
            ]
        )
    ]
)


my_contents = html.Div(children=[
    html.Div(className="row", children=[
        html.Div(className="col-lg-3 col-sm-6", children=[
            html.Div(className="card card-stats", children=[
                html.Div(className="card-body", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col-5", children=[
                            html.Div(className="icon-big text-center icon-warning", children=[
                                html.I(className="nc-icon nc-chart text-warning")
                            ])
                        ]),
                        html.Div(className="col-7", children=[
                            html.Div(className="numbers", children=[
                                html.P(className="card-category",
                                       children="Number"),
                                html.H4(className="card-title",
                                        children="150GB")
                            ])
                        ])
                    ])
                ]),
                html.Div(className="card-footer", children=[
                    html.Hr(),
                    html.Div(className="stats", children=[
                        html.I(className="fa fa-refresh"),
                        " Update Now"
                    ])
                ])
            ])
        ]),
        html.Div(className="col-lg-3 col-sm-6", children=[
            html.Div(className="card card-stats", children=[
                html.Div(className="card-body", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col-5", children=[
                            html.Div(className="icon-big text-center icon-warning", children=[
                                html.I(
                                    className="nc-icon nc-light-3 text-success")
                            ])
                        ]),
                        html.Div(className="col-7", children=[
                            html.Div(className="numbers", children=[
                                html.P(className="card-category",
                                       children="Revenue"),
                                html.H4(className="card-title",
                                        children="$ 1,345")
                            ])
                        ])
                    ])
                ]),
                html.Div(className="card-footer", children=[
                    html.Hr(),
                    html.Div(className="stats", children=[
                        html.I(className="fa fa-calendar-o"),
                        " Last day"
                    ])
                ])
            ])
        ]),
        html.Div(className="col-lg-3 col-sm-6", children=[
            html.Div(className="card card-stats", children=[
                html.Div(className="card-body", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col-5", children=[
                            html.Div(className="icon-big text-center icon-warning", children=[
                                html.I(className="nc-icon nc-vector text-danger")
                            ])
                        ]),
                        html.Div(className="col-7", children=[
                            html.Div(className="numbers", children=[
                                html.P(className="card-category",
                                       children="Errors"),
                                html.H4(className="card-title", children="23")
                            ])
                        ])
                    ])
                ]),
                html.Div(className="card-footer", children=[
                    html.Hr(),
                    html.Div(className="stats", children=[
                        html.I(className="fa fa-clock-o"),
                        " In the last hour"
                    ])
                ])
            ])
        ]),
        html.Div(className="col-lg-3 col-sm-6", children=[
            html.Div(className="card card-stats", children=[
                html.Div(className="card-body", children=[
                    html.Div(className="row", children=[
                        html.Div(className="col-5", children=[
                            html.Div(className="icon-big text-center icon-warning", children=[
                                html.I(
                                    className="nc-icon nc-favourite-28 text-primary")
                            ])
                        ]),
                        html.Div(className="col-7", children=[
                            html.Div(className="numbers", children=[
                                html.P(className="card-category",
                                       children="Followers"),
                                html.H4(className="card-title",
                                        children="+45K")
                            ])
                        ])
                    ])
                ])
            ])
        ]),
    ])
])


sixx = None

#app_dash.layout = get_layout(app_dash)
app_dash.layout = html.Div([
    html.Div(className='wrapper', children=[
        html.Div(className='sidebar', style={'background-color': 'orange'}, children=[
            html.Div(className='sidebar-wrapper', children=[
                # leftitem,
                # navitem,
            ])
        ]),
        html.Div(
            className='sidebar-background',
            style={
                # app_dash.get_asset_url("../assets/img/sidebar-5.jpg")
                'background-image': html.Img(src='../assets/img/sidebar-5.jpg')
            }
            #     background-image: url(../assets/img/sidebar-5.jpg);
        ),
        html.Div(className='main-panel', children=[
            html.Nav(className='navbar navbar-expand-lg', children=[
                html.Div(className='container-fluid', children=[
                    navbar,
                    # btnbtn,
                    # righttop_nav
                ])
            ]),
            #     html.Div(className='content', children=[
            #         html.Div(className='container-fluid', children=[
            #             my_contents
            #         ])
            #     ]),
            #     html.Footer(className='footer', children=[
            #         html.Div(className='container')
            #     ])
        ])
    ])
])

bettydash.callbacks.get_callbacks(app_dash)

# Add callback to toggle collapse on click
# app_dash.callback(
#     Output('formsExamples', 'className'),
#     Input('formsExamples-toggle', 'n_clicks'),
#     prevent_initial_call=True
# )(lambda n: 'nav collapse show' if n else 'nav collapse')


@app_dash.callback(Output('minimizeSidebar', 'children'),
                   [Input('minimizeSidebar', 'n_clicks')])
def on_button_click(n_clicks):
    if n_clicks:
        script = """
        var script = document.createElement('script');
        script.src = 'bettyboard/assets/js/light-bootstrap-dashboard.js';
        document.head.appendChild(script);
        """
        return html.Script(script)
    else:
        return ""


if __name__ == "__main__":
    app_dash.run_server(debug=True, port=8887)
