##################################################
# Constants
##################################################
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output
import json
from astradb import *

haiku_list = [] 
txt_area_list = []
txt_area_input_list = []

with open('assets/bnh_transcript.json') as json_data:
    d = json.loads(json_data.read())

    segments = d['segments']
    object_i = 1
    for seg in segments:
        haiku_list.append(seg['text'])
        ta = dbc.Textarea(id= f'ta{object_i}', value = '', style={'width': '100%', 'height': 50})
        txt_area_input_list.append(Input(f'ta{object_i}', 'value'))
        txt_area_list.append(ta)
        object_i += 1

    json_data.close()

rule_fmt = []
for i in range(0, len(haiku_list)):
    tmp = [
    html.Hr(),
    html.H4(haiku_list[i]),
    txt_area_list[i]
    ]
    
    rule_fmt += tmp

idea_sketch_share_btn = dbc.Button('Share Idea-Sketches', id='idea-sketch-share-btn', n_clicks=0)
btn_inpt = Input('idea-sketch-share-btn', 'n_clicks')

btn =  dbc.Row(
            children = [
                html.Div(
                        idea_sketch_share_btn
                )
                
            ],

            style = {"width":"full", "textAlign":"center"}
        ) 

user_select = dbc.Select(
    id="name-select",
    required=True,
    placeholder = "choose your name",
    options=[
            {'label': 'Alex', 'value': 'Alex'},
            {'label': 'Sebastian', 'value': 'Sebastian'},
            {'label': 'Orlando', 'value': 'Orlando'},
            {'label': 'Nathan', 'value': 'Nathan'},
            {'label': 'Jiara', 'value': 'Jiara'},
            {'label': 'Kiki', 'value': 'Kiki'},
            {'label': 'Afure', 'value': 'Afure'}],
)

u_slc =  dbc.Row(
            children = [
                html.Div(
                        user_select
                )     
            ],

            style = {"width":"full", "textAlign":"center"}
        ) 

u_slc_inpt = Input('name-select', 'value')

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
                u_slc,
                btn,
                header
            ]
        )
        return body


def update_sketches(table, inpts):
    session = open_session()
    keyspace = "idea_sketches"

    text_blocks = []

    for i in range(0, len(inpts)):
        text_blocks.append((i + 1, haiku_list[i], inpts[i]))

    write_to_table(session, keyspace, table, text_blocks)

    close_session(session)

# ##################################################
# # Page Specific Callbacks
# ##################################################    
inputs = txt_area_input_list + [btn_inpt, u_slc_inpt]
def get_callbacks(app):
    @app.callback(
        Output('idea-sketch-share-btn', 'value'),
        inputs
    )
    def gen_hilbert_table(i1, i2, i3, i4, i5, i6, i7, i8, btn, slc):
        
        if btn >= 1 and slc is not None:
             update_sketches(slc, [i1, i2, i3, i4, i5, i6, i7, i8])
             print('hi')

