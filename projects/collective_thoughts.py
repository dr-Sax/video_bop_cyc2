##################################################
# Constants
##################################################
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output
import json
from astradb import *

haiku_list = [] 
txt_area_list = []
collective_thoughts = []

with open('assets/bnh_transcript.json') as json_data:
    d = json.loads(json_data.read())
    segments = d['segments']
    for seg in segments:
        haiku_list.append(seg['text'])
    json_data.close()

def refresh_thoughts():
    collective_thoughts = [[], [], [], [], [], [], [], []]
    
    session = open_session()
    keyspace = "idea_sketches"
    audience = ['Alex', 'Sebastian', 'Orlando', 'Nathan', 'Jiara', 'Kiki', 'Afure']
    
    for a in audience:
        try:
            usr_thoughts = read_from_table(session, keyspace, a)
        except:
            pass
        
        for thought in usr_thoughts:
            id = thought[0]
            haiku = thought[1]
            phrase = thought[2]
            try:
                collective_thoughts[id - 1].append(html.H4(phrase))
            except:
                pass

    close_session(session)
    return collective_thoughts

#     with open('assets/sketches.json', 'r') as openfile:
#             # Reading from json file
#             json_object = json.load(openfile)
#             for i in range(0, len(keys)):
#                 val = json_object[keys[i]]
#                 temp = []
#                 for j in val:
#                     temp.append(html.H4(j))
#                 collective_thoughts.append(temp)
#             json_data.close()
#     return collective_thoughts

collective_thoughts = refresh_thoughts()

def update_page(collective_thoughts):
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
    return header

header = update_page(collective_thoughts)

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
        header = update_page(refresh_thoughts())
        body = dbc.Container(
            [
                header 
            ]
        )
        return body

##################################################
# Page Specific Callbacks
##################################################    
# def get_callbacks(app):
#     @app.callback(
#         Output('rfresh', 'value'),
#         btn_inpt
        
#     )
#     def refresh(i1):
        
#         if i1 >= 1:
#              a = refresh_thoughts()
#              b = update_page(a)
