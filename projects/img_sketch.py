


##################################################
# Constants
##################################################
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output
import pandas as pd

import json
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
                btn,
                header
            ]
        )
        return body
keys = ['ta1', 'ta2', 'ta3', 'ta4', 'ta5', 'ta6', 'ta7', 'ta8']
def update_sketches(inpts):
     with open('C:/Users/nicor/OneDrive/Documents/Code/video-bop/assets/sketches.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
        for i in range(0, len(inpts)):
            if (inpts[i] in json_object[keys[i]]) or (inpts[i] == ""):
                pass # dont double update
            else:
                json_object[keys[i]].append(inpts[i])
    
     with open('C:/Users/nicor/OneDrive/Documents/Code/video-bop/assets/sketches.json', 'w') as f:
         json.dump(json_object, f)

# ##################################################
# # Page Specific Callbacks
# ##################################################    
inputs = txt_area_input_list + [btn_inpt]
def get_callbacks(app):
    @app.callback(
        Output('idea-sketch-share-btn', 'value'),
        inputs
    )
    def gen_hilbert_table(i1, i2, i3, i4, i5, i6, i7, i8, btn):
        
        if btn >= 1:
             update_sketches([i1, i2, i3, i4, i5, i6, i7, i8])

