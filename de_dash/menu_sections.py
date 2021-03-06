import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from PIL.ImageColor import colormap
from dash.exceptions import PreventUpdate
from dash.dependencies import Output, Input, State

from .app import app
from . import default_styles as stl


hyperparameters = [
    html.Div(dcc.Markdown("**__HYPERPARAMETERS:__**"), style=dict(color="#000000")),
    
    html.Div([
        dcc.Loading([
            dcc.Dropdown(
                id="model_dropdown", 
                placeholder="FER Model",
                value="vggface_ce",
                clearable=False,
                options=[
                    dict(label="VGGFACE CE (1-NN)", value="vggface_ce"),
                    dict(label="VGGFACE CE (3-NN)", value="vggface_ce_l3"),
                    dict(label="VGGFACE CK+ (1-NN)", value="vggface_ck"),
                    dict(label="VGGFACE CK+ (3-NN)", value="vggface_ck_l3"),
                    dict(label="VGGFACE KDEF (1-NN)", value="vggface_kdef"),
                    dict(label="VGGFACE KDEF (3-NN)", value="vggface_kdef_l3"),
                ]
            ),

            dcc.Store(id="store_collection", data=dict(model_name="vggface_ce")),
        ]),

        

        html.Div([
            html.Div([
                dcc.Markdown("FD confidence:", id="aiamfsd"),
                dbc.Tooltip(
                    "Confidence threshold from the Face Detector",
                    target="aiamfsd", placement="bottom-end",  
                    style=dict(borderRadius=5, marginLeft="15px", padding=3, color="#ffffff", backgroundColor="#66a3ff")
                ),
            ], className="three columns", style=dict(color="#000000")),

            html.Div([               
                dcc.Slider(
                    id="fd_threshold_slider",
                    min=10, max=90,
                    step=5, value=50,
                    updatemode="drag",
                    marks={i: dict(label=f'{i}%', style=dict(
                        color="#000000")) for i in range(10, 91, 10)},
                ),
            ], className="nine columns"),

        ], className="row", style=dict(marginTop="1.5%", marginBottom="1%")),
    ]),
]


colors = [
    html.Div(dcc.Markdown("**__BOUNDING BOXES COLORS:__**"), style=dict(color="#000000")),

    html.Div([
        html.Div([
            html.Div([
                dcc.Markdown("* Anger:"),
            ], className="two columns", style=dict(color="#000000", fontSize=12, **{'vertical-align': 'middle'})),

            html.Div([
                html.Div(id="anger_color_bar", className="one columns"),

                dcc.Dropdown(
                    id="anger_color_drop", 
                    clearable=False,
                    value="red",
                    options = [dict(label=c, value=c) for c in colormap],
                    style=stl.color_drop
                ),

            ], className="four columns", style=stl.color_drop_div),

            html.Div([
                dcc.Markdown("* Disgust:"),
            ], className="two columns", style=dict(color="#000000", fontSize=12, marginLeft="15px")),

            html.Div([
                html.Div(id="disgust_color_bar", className="one columns"),

                dcc.Dropdown(
                    id="disgust_color_drop", 
                    clearable=False,
                    value="goldenrod",
                    options = [dict(label=c, value=c) for c in colormap],
                    style=stl.color_drop
                ),
            ], className="four columns", style=stl.color_drop_div),
        ], className="row"),

        html.Div([
            html.Div([
                dcc.Markdown("* Fear:"),
            ], className="two columns", style=dict(color="#000000", fontSize=12)),

            html.Div([
                html.Div(id="fear_color_bar", className="one columns"),
                
                dcc.Dropdown(
                    id="fear_color_drop", 
                    clearable=False,
                    value="mediumpurple",
                    options = [dict(label=c, value=c) for c in colormap],
                    style=stl.color_drop
                ),
            ], className="four columns", style=stl.color_drop_div),

            html.Div([
                dcc.Markdown("* Happiness:"),
            ], className="two columns", style=dict(color="#000000", fontSize=12, marginLeft="15px")),

            html.Div([
                html.Div(id="happiness_color_bar", className="one columns"),
                
                dcc.Dropdown(
                    id="happiness_color_drop", 
                    clearable=False,
                    value="yellow",
                    options = [dict(label=c, value=c) for c in colormap],
                    style=stl.color_drop
                ),
            ], className="four columns", style=stl.color_drop_div),
        ], className="row", style=dict(marginTop="1%")),

        html.Div([               
            html.Div([
                dcc.Markdown("* Neutral:"),
            ], className="two columns", style=dict(color="#000000", fontSize=12)),

            html.Div([
                html.Div(id="neutral_color_bar", className="one columns"),
                
                dcc.Dropdown(
                    id="neutral_color_drop", 
                    clearable=False,
                    value="darkgrey",
                    options = [dict(label=c, value=c) for c in colormap],
                    style=stl.color_drop
                ),
            ], className="four columns", style=stl.color_drop_div),

            html.Div([               
                dcc.Markdown("* Sadness:"),
            ], className="two columns", style=dict(color="#000000", fontSize=12, marginLeft="15px")),

            html.Div([
                html.Div(id="sadness_color_bar", className="one columns"),
                
                dcc.Dropdown(
                    id="sadness_color_drop", 
                    clearable=False,
                    value="royalblue",
                    options = [dict(label=c, value=c) for c in colormap],
                    style=stl.color_drop
                ),
            ], className="four columns", style=stl.color_drop_div),
        ], className="row", style=dict(marginTop="1%")),

        html.Div([
            html.Div([
                dcc.Markdown("* Surprise:"),
            ], className="two columns", style=dict(color="#000000", fontSize=12)),

            html.Div([
                html.Div(id="surprise_color_bar", className="one columns"),
                
                dcc.Dropdown(
                    id="surprise_color_drop", 
                    clearable=False,
                    value="limegreen",
                    options = [dict(label=c, value=c) for c in colormap],
                    style=stl.color_drop
                ),
            ], className="four columns", style=stl.color_drop_div),
        ], className="row", style=dict(marginTop="1%")),
    ]),
]


upload = [
    html.Div([

        html.Div([
            dcc.Input(id="input_url", type="text", placeholder="Image URL", style=stl.inputs),
        ], className="four columns"),

        html.Div([
            html.Div([

                html.Div([
                    html.Button("SUBMIT", id="submit_url", type="submit", n_clicks=0, style=stl.button),
                ], className="four columns"),

                html.Div([
                    dcc.Upload(html.Button("BROWSE", type="submit", style=stl.button), id="upload_image"),
                ], className="four columns"),

                html.Div([
                    html.A(
                        html.Button("DOWNLOAD", style=stl.download_button), 
                        id="download_image", download="image.png", href="", target="_blank"),
                ], className="four columns"),

            ], className="row", style=dict(marginLeft="10px")),
        ], className="eight columns"),

    ], className="row", style=dict(marginLeft="2.5%"))
]


@app.callback(Output("anger_color_bar", "style"), [
    Input("anger_color_drop", "value")])
def update_anger_color_bar(c):
    return dict(height="2px", width="100%", backgroundColor=colormap[c]) 


@app.callback(Output("disgust_color_bar", "style"), [
    Input("disgust_color_drop", "value")])
def update_disgust_color_bar(c):
    return dict(height="2px", width="100%", backgroundColor=colormap[c]) 


@app.callback(Output("fear_color_bar", "style"), [
    Input("fear_color_drop", "value")])
def update_fear_color_bar(c):
    return dict(height="2px", width="100%", backgroundColor=colormap[c]) 


@app.callback(Output("happiness_color_bar", "style"), [
    Input("happiness_color_drop", "value")])
def update_happiness_color_bar(c):
    return dict(height="2px", width="100%", backgroundColor=colormap[c]) 


@app.callback(Output("neutral_color_bar", "style"), [
    Input("neutral_color_drop", "value")])
def update_neutral_color_bar(c):
    return dict(height="2px", width="100%", backgroundColor=colormap[c]) 


@app.callback(Output("sadness_color_bar", "style"), [
    Input("sadness_color_drop", "value")])
def update_sadness_color_bar(c):
    return dict(height="2px", width="100%", backgroundColor=colormap[c]) 


@app.callback(Output("surprise_color_bar", "style"), [
    Input("surprise_color_drop", "value")])
def update_surprise_color_bar(c):
    return dict(height="2px", width="100%", backgroundColor=colormap[c]) 