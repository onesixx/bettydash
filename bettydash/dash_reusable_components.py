from textwrap import dedent

from dash import dcc
from dash import html

def Row(children=None, **kwargs):
    return html.Div(children, className="row", **kwargs)

def Column(children=None, width=1, **kwargs):
    nb_map = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
        7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve'}
    return html.Div(children, 
        className=f"{nb_map[width]} columns", 
        **kwargs)

# html.Div(className='container', children=[
#     Row(html.P("Input Image URL:")),
#     Row([
#         Column(width=8, children=[
#             dcc.Input(id='input-url', style={'width': '100%'}, placeholder='Insert URL...'),
#         ]),
#         Column(html.Button("Run DETR", id='button-run', n_clicks=0), width=2),
#         Column(html.Button("Random Image", id='button-random', n_clicks=0), width=2)
#     ]),
# ])

# Display utility functions
def _merge(a, b):
    return dict(a, **b)

def _omit(omitted_keys, d):
    return {k: v for k, v in d.items() if k not in omitted_keys}

def sidebar_item(children, **kwargs):
    return html.Div(className="sidebar-wrapper", 
                    children=children, **_omit(["style"], kwargs))

def navbar():
    return None

# Custom Display Components
def Card(children, **kwargs):
    return html.Section(className="card", children=children, **_omit(["style"], kwargs))

def FormattedSlider(**kwargs):
    return html.Div(
        style=kwargs.get("style", {}), children=dcc.Slider(**_omit(["style"], kwargs))
    )

def NamedSlider(name, **kwargs):
    return html.Div(
        style={"padding": "20px 10px 25px 4px"},
        children=[
            html.P(f"{name}:"),
            html.Div(style={"margin-left": "6px"},
                     children=dcc.Slider(**kwargs)),
        ],
    )

def NamedDropdown(name, **kwargs):
    return html.Div(
        style={"margin": "10px 0px"},
        children=[
            html.P(children=f"{name}:", style={"margin-left": "3px"}),
            dcc.Dropdown(**kwargs),
        ],
    )

def NamedRadioItems(name, **kwargs):
    return html.Div(
        style={"padding": "20px 10px 25px 4px"},
        children=[html.P(children=f"{name}:"), dcc.RadioItems(**kwargs)],
    )

# Non-generic
def DemoDescription(filename, strip=False):
    with open(filename, "r") as file:
        text = file.read()

    if strip:
        text = text.split("<Start Description>")[-1]
        text = text.split("<End Description>")[0]

    return html.Div(
        className="row",
        style={
            "padding": "15px 30px 27px",
            "margin": "45px auto 45px",
            "width": "80%",
            "max-width": "1024px",
            "borderRadius": 5,
            "border": "thin lightgrey solid",
            "font-family": "Roboto, sans-serif",
        },
        children=dcc.Markdown(dedent(text)),
    )
