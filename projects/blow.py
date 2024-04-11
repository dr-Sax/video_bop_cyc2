##################################################
# Constants
##################################################
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, ALL, Input, Patch, Output
import json
from astradb_2 import *

haiku_list = [] 
txt_area_list = []
haiku_slc_opts = []

note_rows = []
form_inpts = []

patched_urls = Patch()
patched_str_times = Patch()
patched_str_words = Patch()
patched_end_words = Patch()

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

blow_btn = dbc.Button('Blow', id='blow-btn', n_clicks=0)
blow_btn_inpt = Input('blow-btn', 'n_clicks')

btn =  dbc.Row(
            children = [
                html.Div(
                        blow_btn
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
                header,
                btn,
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
                url_i = dbc.Input(
                            id = {"type": "url-inpt", "index": f'{i}'},
                            required=False,
                            placeholder="Paste URL"
                        )
                patched_urls.append(url_i)

                start_time_i = dbc.Input(
                                id = {"type": "str-time-inpt", "index": f'{i}'},
                                required=False,
                                placeholder="Clip Starttime"
                                )
                patched_str_times.append(start_time_i)

                start_word_i = dbc.Select(
                                id={"type": f"start-word-inpt", "index":f'{i}'},
                                required=False,
                                placeholder = "Start Word",
                                options=word_opts_list
                                )   
                patched_str_words.append(start_word_i)

                end_word_i = dbc.Select(
                                id={"type": f"end-word-inpt", "index":f'{i}'},
                                required=False,
                                placeholder = "End Word",
                                options=word_opts_list
                                )   
                patched_end_words.append(end_word_i)
                 
                input = dbc.Row(
                            children = [
                                dbc.Col(
                                     url_i 
                                ),
                                dbc.Col(
                                     start_time_i
                                ),
                                dbc.Col(
                                     start_word_i
                                ),
                                dbc.Col(
                                     end_word_i
                                )
                            ],

                            style = {"width":"10", "textAlign":"left"}
                        )
                 

                input_rows_list.append(input)
            return input_rows_list
        
    @app.callback(
        Output('blow-btn', 'value'),
        [
        Input({"type": "url-inpt", "index": ALL}, "value"),
        Input({"type": "str-time-inpt", "index": ALL}, "value"),
        Input({"type": "start-word-inpt", "index": ALL}, "value"),
        Input({"type": "end-word-inpt", "index": ALL}, "value"),
        Input(component_id = 'haiku-select', component_property = 'value'),
        blow_btn_inpt
        ]
    )
    def read_form(url_inpts, strt_time_inpts, strt_word_inpts, end_word_inpts, haiku_slc, btn):
        
        if btn >= 1:
            session = open_session()
            keyspace = 'blows'
            table = f'h{int(haiku_slc)+1}'

            text_blocks = []

            for i in range(0, len(url_inpts)):
                text_blocks.append((i + 1, url_inpts[i], strt_time_inpts[i], strt_word_inpts[i], end_word_inpts[i]))

            write_to_table(session, keyspace, table, text_blocks)
            
            vals = read_from_table(session, keyspace, table)
            print(vals)
            close_session(session)
             


