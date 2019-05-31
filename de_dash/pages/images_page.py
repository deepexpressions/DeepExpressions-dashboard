import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

from de_dash import utils
from de_dash.app import app


layout = [
    html.P("Esta é a página com as imagens"),

    # Upload section
    html.Div([
        html.Section([
            dcc.Upload([
                "Drag and Drop or ",
                html.A("Select an Image")
            ], style=utils.UP_STYLE, accept='images/*')
        ], style=utils.UP_SEC_STYLE)
    ], className="four columns"),
]