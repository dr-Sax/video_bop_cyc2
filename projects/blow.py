##################################################
# Constants
##################################################
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output

import json
haiku_list = [] 
txt_area_list = []
haiku_slc_opts = []

note_rows = []

for i in range(1, 9):
    with open(f'assets/h{i}_transcript.json') as json_data:
        d = json.loads(json_data.read())
        segments = d['segments']

        for seg in segments:
            haiku_list.append(seg['text'])

        haiku_slc_opts.append({'label': f'{haiku_list[i - 1]}', 'value': i - 1})
        json_data.close()

haiku_select = dbc.Select(
    id="haiku-select",
    required=True,
    placeholder = "Which Haiku you Blowing Over?",
    options=haiku_slc_opts
)

##################################################
# Constants
##################################################
p1 = "The Jazz term for 'improvise.' It has a more mystical aura. Also, simply to play an instrument."


youtube = dcc.Link(children = 'Youtube', href = 'www.youtube.com')

header =  dbc.Row(
            children = [
                html.Div(
                    [
                        html.Hr(),
                        html.H4(p1),
                        html.Hr()
                    ]
                )
                
            ],

            style = {"width":"10", "textAlign":"left"}
        ) 

input_rows =  html.Div(
                id = 'input-rows',
                children = []
                )

##################################################
# Mapping Page Content
##################################################     
def page_content():
        body = dbc.Container(
            [
                header,
                haiku_select,
                youtube,
                input_rows
            ]
        )
        return body

# ##################################################
# # Page Specific Callbacks
# ##################################################     
def get_callbacks(app):
    @app.callback(
        Output(component_id = 'input-rows', component_property = 'children'),
        Input(component_id = 'haiku-select', component_property = 'value')
    )
    def gen_blow_inpts(haiku):
        if haiku is not None:
            phrase = haiku_list[int(haiku)]
            word_list = phrase.strip().split()

            input_rows_list = []
            word_opts_list = []
            for i in range(0, len(word_list)):
                 word_opts_list.append({'label': f'{word_list[i]}', 'value': f'{word_list[i]}'})

            for i in range(0, len(word_list)):
                 
                input = dbc.Row(
                            children = [
                                dbc.Col(
                                     dbc.Input(
                                          id = f"url-{i}",
                                          required=False,
                                          placeholder="Paste URL"
                                     )
                                     
                                ),
                                dbc.Col(
                                     dbc.Input(
                                          id = f"strt-time-{i}",
                                          required=False,
                                          placeholder="Paste Clip Start-time"
                                     )
                                     
                                ),
                                dbc.Col(
                                     dbc.Select(
                                        id=f"start-word-{i}",
                                        required=False,
                                        placeholder = "Start Word",
                                        options=word_opts_list
                                    )
                                ),

                                dbc.Col(
                                     dbc.Select(
                                        id="end-word-{i}",
                                        required=False,
                                        placeholder = "End Word",
                                        options=word_opts_list
                                    )
                                )

                        
                            ],

                            style = {"width":"10", "textAlign":"left"}
                        ) 
                input_rows_list.append(input)
            return input_rows_list


