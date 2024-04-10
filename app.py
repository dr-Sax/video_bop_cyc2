# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
# https://dash.plotly.com/deployment
# git status # view the changes
# git add .  # add all the changes
# git commit -m 'a description of the changes'
# git push heroku master
# heroku ps:scale web=1
#comment3
#comment

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import sys
from site_automations import project_dropdown, project_names


app = Dash(__name__, suppress_callback_exceptions = True)  #, external_stylesheets = [dbc.themes.QUARTZ])
server = app.server

#####################################
# loading names from projects tree  #
#####################################
pn = project_names()
pd = project_dropdown(pn)

###########################################################
# For Each page, there should be a loading stage by which 
# callbacks and page content are loaded in
###########################################################
navbar_headings = []

for name in pn:
    try:
        sys.path.append("projects")
        module =  __import__(f'{name}')
        module.page_content()
        try:
            module.get_callbacks(app)
        except:
            pass
        obj = dbc.NavItem(dbc.NavLink(f"{name}", href = f"/{name}", active = 'exact'))
        navbar_headings.append(obj)
    except:
        pass


############################################################
# navbar layout - could be moved to separate file          #
############################################################
navbar = dbc.NavbarSimple(
    children = navbar_headings,

    brand = "Video-Bop",
    brand_href="#",
    color="primary",
    dark = True,
    style={'width': 'auto'}
)

#############################################
# Storage for page details beneath nav bar
#############################################
content = html.Div(
    id = "page-content", 
    children = [], 
)


#############################################
# combining all elements of the app layout
#############################################
app.layout = dbc.Container(
    [
        dcc.Location(id = "url"),
        navbar,
        content
    ],
    fluid = True
)



#############################################
# callbacks to handle url page switching
#############################################
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)

def render_page_content(pathname):
    if pathname == '/':
        
        return [
            dbc.Container(html.H1('VideoBop')),
        ]
    
    elif pathname[1:] in pn:
        sys.path.append("projects")
        module =  __import__(f'{pathname[1:]}')
        body = module.page_content()
        
        return [
            dbc.Container(html.H1(pathname[1:])),
            body
        ]


#################################
# main running
#################################
if __name__ == '__main__':
    # https://qr.io/?gad_source=1&gclid=Cj0KCQjw2a6wBhCVARIsABPeH1uevjjkFM7Kp8s5KRyux7G4zqIPIkiu894iaQbMVrMqTyq0jFi8iagaApGjEALw_wcB
    # import socket
    # host = socket.gethostbyname(socket.gethostname())
    # app.run_server(debug=True, host=host, port = 8050)
    app.run_server(debug = True)