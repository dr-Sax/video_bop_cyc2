##################################################
# Constants
##################################################
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output
import pandas as pd

import json
haiku_list = [] 
txt_area_list = []
collective_thoughts = []
keys = ['ta1', 'ta2', 'ta3', 'ta4', 'ta5', 'ta6', 'ta7', 'ta8']

with open('assets/bnh_transcript.json') as json_data:
    d = json.loads(json_data.read())
    segments = d['segments']
    for seg in segments:
        haiku_list.append(seg['text'])
    json_data.close()

with open('C:/Users/nicor/OneDrive/Documents/Code/video-bop/assets/sketches.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
        for i in range(0, len(keys)):
            val = json_object[keys[i]]
            temp = []
            for j in val:
                temp.append(html.H4(j))
            collective_thoughts.append(temp)
        json_data.close()
            

rule_fmt = []
for i in range(0, len(haiku_list)):
    tmp = [
    html.Hr(),
    html.H4(haiku_list[i])
    ]

    tmp2 = collective_thoughts[i]
    
    rule_fmt += tmp + tmp2

header =  dbc.Row(
            children = [
                html.Div(
                        rule_fmt
                )
                
            ],

            style = {"width":"10", "textAlign":"left"}
        ) 

refresh_pg = dbc.Button('Refresh Page', id='rfresh', n_clicks=0)
btn_inpt = Input('rfresh', 'n_clicks')

btn =  dbc.Row(
            children = [
                html.Div(
                        refresh_pg
                )
                
            ],

            style = {"width":"full", "textAlign":"center"}
        )    

##################################################
# Mapping Page Content
##################################################     
def page_content():
        body = dbc.Container(
            [
                refresh_pg,
                header 

            ]
        )
        return body

##################################################
# Page Specific Callbacks
##################################################    
def get_callbacks(app):
    @app.callback(
        Output('rfresh', 'value'),
        btn_inpt
        
    )
    def refresh(i1):
        
        if i1 >= 1:
             print('hi')
