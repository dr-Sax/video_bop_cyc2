r1 = '1. Scribbled secret notebooks, and wild typewritten pages, for yr own joy'
r2 = '2. Submissive to everything, open, listening'
r3 = '3. Try never get drunk outside yr own house'
r4 = '4. Be in love with yr life'
r5 = '5. Something that you feel will find its own form'
r6 = '6. Be crazy dumbsaint of the mind'
r7 = '7. Blow as deep as you want to blow'
r8 = '8. Write what you want bottomless from bottom of the mind'
r9 = '9. The unspeakable visions of the individual'
r10 = '10. No time for poetry but exactly what is'
r11 = '11. Visionary tics shivering in the chest'
r12 = '12. In tranced fixation dreaming upon object before you'
r13 = '13. Remove literary, grammatical and syntactical inhibition'
r14 = '14. Like Proust be an old teahead of time'
r15 = '15. Telling the true story of the world in interior monolog'
r16 = '16. The jewel center of interest is the eye within the eye'
r17 = '17. Write in recollection and amazement for yourself'
r18 = '18. Work from pithy middle eye out, swimming in language sea'
r19 = '19. Accept loss forever'
r20 = '20. Believe in the holy contour of life'
r21 = '21. Struggle to sketch the flow that already exists intact in mind'
r22 = '22. Dont think of words when you stop but to see picture better'
r23 = '23. Keep track of every day the date emblazoned in yr morning'
r24 = '24. No fear or shame in the dignity of yr experience, language & knowledge'
r25 = '25. Write for the world to read and see yr exact pictures of it'
r26 = '26. Bookmovie is the movie in words, the visual American form'
r27 = '27. In praise of Character in the Bleak inhuman Loneliness'
r28 = '28. Composing wild, undisciplined, pure, coming in from under, crazier the better'
r29 = '29. You’re a Genius all the time'
r30 = '30. Writer-Director of Earthly movies Sponsored & Angeled in Heaven'
rules_list = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10,r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27, r28, r29, r30] 

##################################################
# Constants
##################################################
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc, Input, Output
import pandas as pd

rule_fmt = []
for rule in rules_list:
    tmp = [
    html.Hr(),
    html.H4(rule)  
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

