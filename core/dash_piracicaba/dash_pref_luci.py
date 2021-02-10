# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


import dash_core_components as dcc
import dash_html_components as html
import os
from pathlib import Path
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc
import base64

app1 = DjangoDash('Pref_luci')

#Abre em um chrome com diferentes caminhos para cada sistema peracional
cwd = os.getcwd()
path_download = Path(cwd,"core/Bases/Prefeitura/Eleicao/Mapa/")

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#Abre em um chrome com diferentes caminhos para cada sistema peracional




app1.layout =  html.Div([
            html.Div([
                    dcc.Dropdown(
                        id='yaxis-column',
                        options=[
                            {'label': 'Luciano Almeida - Primeiro Turno', 'value': 'Luciano Almeida'},
                            {'label': 'Luciano Almeida - Segundo Turno', 'value': 'LUCIANO SANTOS TAVARES DE ALMEIDA'},
                            ],
                        value='Luciano Almeida',
                        style={'height':'3em','width':'80%',})]),
            html.Br(),
            html.Br(),

            html.Iframe(id='map',width='90%',height='400')])

@app1.callback(
    Output('map','srcDoc'),
    [Input('yaxis-column', 'value')])
def update_figure(selected_name):
    path_download2 = Path(path_download,"mapa_pref_{}.html".format('Luciano Almeida'))
    return open(path_download2,'r').read()
