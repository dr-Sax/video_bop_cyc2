r1 = 'Jack Kerouac, "Essentials of Spontaneous Prose"'
r2 = 'Set-up'
r3 = 'The object is set before the mind, either in reality. as in sketching (before a landscape or teacup or old face) or is set in the memory wherein it becomes the sketching from memory of a definite image-object.'
r4 = 'Procedure'
r5 = 'Time being of the essence in the purity of speech, sketching language is undisturbed flow from the mind of personal secret idea-words, blowing (as per jazz musician) on subject of image.'
r6 = 'Method'
r7 = 'No periods separating sentence-structures already arbitrarily riddled by false colons and timid usually needless commas-but the vigorous space dash separating rhetorical breathing (as jazz musician drawing breath between outblown phrases)--"measured pauses which are the essentials of our speech"--"divisions of the sounds we hear"-"time and how to note it down." (William Carlos Williams)'
r8 = 'Scoping'
r9 = 'Not "selectivity" of expression but following free deviation (association) of mind into limitless blow-on-subject seas of thought, swimming in sea of English with no discipline other than rhythms of rhetorical exhalation and expostulated statement, like a fist coming down on a table with each complete utterance, bang! (the space dash)-Blow as deep as you want-write as deeply, fish as far down as you want, satisfy yourself first, then reader cannot fail to receive telepathic shock and meaning-excitement by same laws operating in his own human mind.'
r10 = 'Lag in Procedure'
r11 = 'No pause to think of proper word but the infantile pileup of scatological buildup words till satisfaction is gained, which will turn out to be a great appending rhythm to a thought and be in accordance with Great Law of timing.'
r12 = 'Timing'
r13 = 'Nothing is muddy that runs in time and to laws of time-Shakespearian stress of dramatic need to speak now in own unalterable way or forever hold tongue-no revisions (except obvious rational mistakes, such as names or calculated insertions in act of not writing but inserting).'
r14 = 'Center of Interest'
r15 = 'Begin not from preconceived idea of what to say about image but from jewel center of interest in subject of image at moment of writing, and write outwards swimming in sea of language to peripheral release and exhaustion-Do not afterthink except for poetic or P. S. reasons. Never afterthink to "improve" or defray impressions, as, the best writing is always the most painful personal wrung-out tossed from cradle warm protective mind-tap from yourself the song of yourself, blow!-now!-your way is your only way-"good"-or "bad"-always honest ("ludi- crous"), spontaneous, "confessionals" interesting, because not "crafted." Craft is craft.'
r16 = 'Structure of Work'
r17 = 'Modern bizarre structures (science fiction, etc.) arise from language being dead, "different" themes give illusion of "new" life. Follow roughly outlines in outfanning movement over subject, as river rock, so mindflow over jewel-center need (run your mind over it, once) arriving at pivot, where what was dim-formed "beginning" becomes sharp-necessitating "ending" and language shortens in race to wire of time-race of work, following laws of Deep Form, to conclusion, last words, last trickle--Night is The End.'
r18 = 'Mental State'
r19 = 'If possible write "without consciousness" in semi-trance (as Yeats later "trance writing") allowing subconscious to admit in own uninhibited interesting necessary and so "modern" language what conscious art would censor, and write excitedly, swiftly, with writing-or-typing-cramps, in accordance (as from center to periphery) with laws of orgasm, Reichs "beclouding of consciousness." Come from within, out--to relaxed and said.'
rules_list = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19] 

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

