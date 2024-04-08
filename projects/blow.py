##################################################
# Constants
##################################################
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output
import pandas as pd

##################################################
# Constants
##################################################
    
header =  dbc.Row(
            children = [
                html.Div(
                    [
                        html.Hr(),
                        html.H4("The Jazz term for 'improvise.' It has a more mystical aura. Also, simply to play an instrument."),
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

