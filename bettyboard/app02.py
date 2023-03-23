import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

external_stylesheets = [
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
    {'src': 'assets/js/core/jquery.3.2.1.min.js'},
    {'src': 'assets/js/core/popper.min.js'},
    {'src': 'assets/js/core/bootstrap.min.js'},
    {'src': 'assets/js/plugins/bootstrap-switch.js'},
    {'src': 'assets/js/plugins/chartist.min.js'},
    {'src': 'assets/js/plugins/bootstrap-notify.js'},
    {'src': 'assets/js/plugins/jquery-jvectormap.js'},
    {'src': 'assets/js/plugins/moment.min.js'},
    {'src': 'assets/js/plugins/bootstrap-datetimepicker.js'},
    {'src': 'assets/js/plugins/sweetalert2.min.js'},
    {'src': 'assets/js/plugins/bootstrap-tagsinput.js'},
    {'src': 'assets/js/plugins/nouislider.js'},
    {'src': 'assets/js/plugins/bootstrap-selectpicker.js'},
    {'src': 'assets/js/plugins/jquery.validate.min.js'},
    {'src': 'assets/js/plugins/jquery.bootstrap-wizard.js'},
    {'src': 'assets/js/plugins/bootstrap-table.js'},
    {'src': 'assets/js/plugins/jquery.dataTables.min.js'},
    {'src': 'assets/js/plugins/fullcalendar.min.js'},
    {'src': 'assets/js/light-bootstrap-dashboard.js?v=2.0.1'},
    {'src': 'assets/js/demo.js'}
]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
)

app.title = "Dashboard PRO"

app.layout = html.Div(className="wrapper", children=[
    html.Meta(charSet="utf-8"),
    html.Div(className="sidebar",
             **{"data-color": "orange",
                "data-image": "assets/img/sidebar-5.jpg"}, children=[
                 html.Div(className="sidebar-wrapper", children=[
                     html.Div(className="logo", children=[
                         html.A(href="http://www.creative-tim.com", className="simple-text logo-mini", children=[
                             "Ct"
                         ])
                     ])
                 ])
             ]),
    html.Div(className="main-panel", children=[
        html.Nav(className="navbar navbar-expand-lg", children=[
            html.Div(className="container-fluid", children=[
                html.Div(className="navbar-wrapper", children=[
                    html.Div(className="navbar-minimize", children=[
                        html.Button(id="minimizeSidebar",
                                    className="btn btn-warning btn-fill btn-round btn-icon d-none d-lg-block", children=[
                                        html.I(
                                            className="fa fa-ellipsis-v visible-on-sidebar-regular"),
                                        html.I(
                                            className="fa fa-navicon visible-on-sidebar-mini")
                                    ])
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
    html.Script(type="text/javascript", children='''
                $(document).ready(function () {
                    demo.initDashboardPageCharts();
                    demo.showNotification();
                    demo.initVectorMap();
                });
            ''')
])

if __name__ == "__main__":
    app.run_server(debug=True, port=8887)
dcc.Lo