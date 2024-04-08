##################################################
# Constants
##################################################
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output
import pandas as pd

##################################################
# Constants
##################################################
p1 = "Active imagination refers to a process or technique of engaging with the ideas or imaginings \
    of one's mind. It is used as a mental strategy to communicate with the subconscious mind. \
    In Jungian psychology, it is a method for bridging the conscious and unconscious minds. \
    Instead of being linked to the Jungian process, the word 'active imagination' in modern psychology\
    is most frequently used to describe a propensity to have a very creative and present imagination.\
    It is thought to be a crucial aid in the process of individuation."

WIDTH = 1100
HEIGHT = 1000
size = 2

youtube = html.Embed(
        src = "https://www.youtube.com",
        width = WIDTH,
        height = HEIGHT
)

header =  dbc.Row(
            children = [
                html.Div(
                    [
                        html.Hr(),
                        html.H4(p1),
                        html.Hr(),
                        dbc.Col(
                        )
                    ]
                )
                
            ],

            style = {"width":"10", "textAlign":"left"}
        ) 

##################################################
# Mapping Page Content
##################################################     
def page_content():
        body = dbc.Container(
            [
                header
            ]
        )
        return body

# ##################################################
# # Page Specific Callbacks
# ##################################################     
# def get_callbacks(app):
#     @app.callback(
#         Output(component_id = 'index_tables', component_property = 'children'),
#         Input(component_id = 'index_select', component_property = 'value')
#     )
#     def gen_hilbert_table(order_n):
#         df = pd.read_csv(f'assets/hilbert/hilbert_index_table_{order_n}.csv')
#         table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
#         return table

