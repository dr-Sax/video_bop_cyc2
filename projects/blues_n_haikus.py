


##################################################
# Constants
##################################################
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output
import pandas as pd

import json
haiku_list = [] 
txt_area_list = []

with open('assets/bnh_transcript.json') as json_data:
    d = json.loads(json_data.read())

    segments = d['segments']
    for seg in segments:
        haiku_list.append(seg['text'])
        ta = dcc.Textarea(id= f'{seg["text"]}',value = '', style={'width': '100%', 'height': 50})
        txt_area_list.append(ta)

    json_data.close()

print(txt_area_list)

rule_fmt = []
for i in range(0, len(haiku_list)):
    tmp = [
    html.Hr(),
    html.H4(haiku_list[i]),
    txt_area_list[i]
    ]
    
    rule_fmt += tmp
  
header =  dbc.Row(
            children = [
                html.Div(
                    rule_fmt
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

