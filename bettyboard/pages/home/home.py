import dash
from dash import dcc, html
#import dash_admin_components as dac
#import dash_bootstrap_components as dbc

# dash.register_page(__name__)


# layout = html.P(
#     'home sweet home'
# )
#from pages.home.model import dataframe
# content = dac.TabItem(
#     id='content_home',
#     children=[
#         layout
#     ],
# )
# home_layout = html.Div(
layout = html.Div(
    [
        html.H1("Welcome to the Home Page"),
        html.P("Use the sidebar to navigate to other pages."),
    ]
)
content = layout
