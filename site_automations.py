import os
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

def project_names():
    fnames = os.listdir('projects')
    for i in range(0, len(fnames)):
        fnames[i] = fnames[i][:-3]

    return fnames

def project_dropdown(fnames):
    dropdown_list = []
    for i in range(0, len(fnames)):
        if fnames[i][0] != '_':
            d = dbc.DropdownMenuItem(f"{fnames[i]}", href = f"/{fnames[i]}")
            dropdown_list.append(d)
    return dropdown_list
