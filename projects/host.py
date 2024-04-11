##################################################
# Constants
##################################################
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output
import pandas as pd
from astradb import *
import astradb_2

##################################################
# Constants
##################################################
    
header =  dbc.Row(
            children = [
                html.Div(
                    [
                        html.Hr(),
                        html.H4("Controls for the Host"),
                        html.Hr(),
                        dbc.Col(
                        )
                    ]
                )
                
            ],

            style = {"width":"10", "textAlign":"left"}
        ) 

clear_user_data_btn = dbc.Button('clear idea thoughts', id='clear-usr-data-btn', n_clicks=0)
clear_user_data_btn_inpt = Input('clear-usr-data-btn', 'n_clicks')

btn1 =  dbc.Row(
            children = [
                html.Div(
                        clear_user_data_btn
                )
                
            ],

            style = {"width":"full", "textAlign":"center"}

)

clear_blow_data_btn = dbc.Button('clear blows', id='clear-blow-data-btn', n_clicks=0)
clear_blow_data_btn_inpt = Input('clear-blow-data-btn', 'n_clicks')

btn2 =  dbc.Row(
            children = [
                html.Div(
                        clear_blow_data_btn
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
                btn1, 
                btn2
            ]
        )
        return body

# ##################################################
# # Page Specific Callbacks
# ##################################################     
def get_callbacks(app):
    @app.callback(
        Output('clear-usr-data-btn', 'value'),
        clear_user_data_btn_inpt
    )
    def gen_hilbert_table(btn):
        audience = ['Alex', 'Sebastian', 'Orlando', 'Nathan', 'Jiara', 'Kiki', 'Afure']

        if btn >= 1:
            session = open_session()
            keyspace = "idea_sketches"
            for a in audience:
                delete_table_values(session, keyspace, a)

            close_session(session)

    @app.callback(
        Output('clear-blow-data-btn', 'value'),
        clear_blow_data_btn_inpt
    )
    def clear_blow_data(btn):
        haikus = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']

        if btn >= 1:
            session = open_session()
            keyspace = "blows"
            for a in haikus:
                astradb_2.delete_table_values(session, keyspace, a)

            close_session(session)

