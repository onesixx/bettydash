import importlib
from dash import html, dcc
import dash_bootstrap_components as dbc

#import dash_admin_components as dac
from bettydash.consts import MENU_ITEMS


def load_module(module_nm):
    rlt = importlib.import_module(f"pages.{module_nm}.{module_nm}")
    return rlt


# # basic_cards = load_module('basic_cards')
# for m in MENU_ITEMS:
#     locals()[m] = load_module(m)

# # =============================================================================
# # Dash Admin Components
# # =============================================================================
# tmp_menu_content = [eval(f'{m}.content') for m in MENU_ITEMS]

# # -------------------------------------------------------------------------------
# # Navbar
# navbar = dbc.NavbarSimple(
#     children=[
#         dbc.NavItem(dbc.NavLink("Home", href="/")),
#         dbc.NavItem(dbc.NavLink("Page 1", href="/page-1")),
#         dbc.NavItem(dbc.NavLink("Page 2", href="/page-2")),
#     ],
#     brand="My Dashboard",
#     brand_href="/",
#     color="primary",
#     dark=True,
# )

# # Sidebar
# sidebar = html.Div(
#     [
#         html.H2("Sidebar", className="display-4"),
#         html.Hr(),
#         html.P(
#             "A simple sidebar menu for navigation", className="lead"
#         ),
#         dbc.Nav(
#             [
#                 dbc.NavLink("Home",   href="/",       active="exact"),
#                 dbc.NavLink("Page 1", href="/page-1", active="exact"),
#                 dbc.NavLink("Page 2", href="/page-2", active="exact"),
#             ],
#             vertical=True,
#             pills=True,
#         ),
#     ],
#     style={
#         "position": "fixed",
#         "top": 0,
#         "left": 0,
#         "bottom": 0,
#         "width": "16rem",
#         "padding": "2rem 1rem",
#         "background-color": "#f8f9fa",
#     },
# )

# # Page content
# content = html.Div(
#     id="page-content",
#     style={"margin-left": "18rem", "margin-right": "2rem"}
# )

# # Home page

# # Page 1
# page1_layout = html.Div(
#     [
#         html.H1("Page 1"),
#         html.P("This is the content of Page 1."),
#     ]
# )

# # Page 2
# page2_layout = html.Div(
#     [
#         html.H1("Page 2"),
#         html.P("This is the content of Page 2."),
#     ]
# )

# # Callback to update page content based on URL


# # App layout
# layout = html.Div([dcc.Location(id="url"), navbar, sidebar, content])

###
# =========================================================
# 원본 Light Bootstrap Dashboard PRO - v2.0.1
# =========================================================
# Product Page: https://www.creative-tim.com/product/light-bootstrap-dashboard-pro
# Copyright 2019 Creative Tim (https://www.creative-tim.com)
# Coded by Creative Tim
# =========================================================
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
##
# def get_layout(app_dash):
#     layout = 
#     return layout

# # -------------------------------------------------------------------------------
# body = dac.Body(
#     dac.TabItems(tmp_menu_content)
# )

# # ---------- Sidebar
# subitems = [
#     dac.SidebarMenuSubItem(id='sideMenu_gallery_1',
#                            label='Gallery 1',
#                            icon='arrow-circle-right',
#                            badge_label='Soon',
#                            badge_color='success'),
#     dac.SidebarMenuSubItem(id='sideMenu_gallery_2',
#                            label='Gallery 2',
#                            icon='arrow-circle-right',
#                            badge_label='Soon',
#                            badge_color='success')
# ]

# sidebar = dac.Sidebar(
#     dac.SidebarMenu(
#         children=[
#             dac.SidebarMenuItem(id='sideMenu_home',
#                                 label='HOME', icon='box'),
#             # dac.SidebarHeader(
#             #     children="Cards"),  # ------------------------------
#             # dac.SidebarMenuItem(id='sideMenu_basic_cards',
#             #                     label='Basic cards', icon='box'),
#             # dac.SidebarMenuItem(id='sideMenu_social_cards',
#             #                     label='Social cards', icon='id-card'),
#             # dac.SidebarMenuItem(id='sideMenu_tab_cards',
#             #                     label='Tab cards', icon='image'),
#             # dac.SidebarHeader(
#             #     children="Boxes"),  # ------------------------------
#             # dac.SidebarMenuItem(id='sideMenu_basic_boxes',
#             #                     label='Basic boxes', icon='desktop'),
#             # dac.SidebarMenuItem(id='sideMenu_value_boxes',
#             #                     label='Value/Info boxes', icon='suitcase'),
#             # dac.SidebarHeader(
#             #     children="Gallery"),  # ----------------------------
#             # dac.SidebarMenuItem(
#             #     label='Galleries', icon='cubes',
#             #     children=subitems),
#         ]
#     ),
#     title='Alyx Dashboard',
#     skin="Dark",
#     color="primary",
#     brand_color="primary",
#     url="https://onesixx.com",
#     # https://adminlte.io/themes/AdminLTE/dist/img/user2-160x160.jpg",
#     src="/assets/user-01.jpg",
#     elevation=3,
#     opacity=0.8
# )

# # ---------- Footer
# footer = dac.Footer(
#     html.A("sixx",
#            href="https://onesixx.com",
#            target="_blank",
#            ),
#     right_text="2019 "
# )

# # ---------- Navbar
# top_right_ui = dac.NavbarDropdown(
#     badge_label="!",
#     badge_color="danger",
#     src="https://quantee.ai",
#         header_text="2 Items",
#     children=[
#         dac.NavbarDropdownItem(
#             children="message 1",
#             date="today"
#         ),
#         dac.NavbarDropdownItem(
#             children="message 2",
#             date="yesterday"
#         ),
#     ]
# )

# navbar = dac.Navbar(
#     id="nav_bread",
#     color="white",
#     text="I can write text in the navbar!",  # os.environ.get("WELCOME"),
#     children=top_right_ui
# )

# # ---------- Controlbar
# controlbar = dac.Controlbar(

#     children=[
#         html.Br(),
#         html.P("Slide to change graph in Basic Boxes"),
#         dcc.Slider(
#             id='controlbar-slider',
#             min=10, max=50, step=1, value=20
#         )
#     ],
#     title="My right sidebar",
#     skin="light"
# )


# layout = dac.Page([navbar, sidebar, body, controlbar, footer])
