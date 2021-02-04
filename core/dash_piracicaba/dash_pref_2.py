# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


import dash_core_components as dcc
import dash_html_components as html
import os
from pathlib import Path
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import base64
import dash_bootstrap_components as dbc
app1 = DjangoDash('Pref_2')

#Abre em um chrome com diferentes caminhos para cada sistema peracional
cwd = os.getcwd()
path_download = Path(cwd,"core/Bases/Prefeitura/Eleicao/Mapa/2T")

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#Abre em um chrome com diferentes caminhos para cada sistema peracional

app1.layout = html.Div(children=[

    html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[
                    {'label': 'Luciano Almeida', 'value': 'Luciano Almeida'},
                    {'label': 'Barjas Negri', 'value': 'Barjas Negri'},
                    {'label': 'Brancos', 'value': 'VOTO BRANCO'},
                    {'label': 'Nulos', 'value': 'VOTO NULO'},


                ],
                value='Luciano Almeida',
                style={'height':'3em','background-color':'rgba(252, 152, 3,0.2)',})]),
    html.Br(),
    html.Br(),





    html.Div(children=[
            html.Br(),

            html.H1(id='nome'),
            html.P(id='email'),
            html.P(id='votos'),
            html.Hr(),
            html.Br(),
            html.Div(
                    html.Img(id='photo',width='50%',height='50%')
            ),
            html.Br(),
            html.Div([
                    html.P('Partido: '),
                    html.P('Coligação: '),
                    html.P('Instrução: '),
                    html.P('Ocupação: '),
                    html.P('Idade: '),
                    html.P('Cidade de Nasc: '),
                    html.P('Estado Civil: '),
                    html.P('Gênero: '),
                    html.P('Cor/Raça: '),
                    html.P('Bens Declarados: '),
                    ],
                    style={ 'display': 'inline-block','padding':'0 2em 0 0'}
            ),

            html.Div([
                    html.P(id='partido'),
                    html.P(id='coligacao'),
                    html.P(id='grau_instrucao'),
                    html.P(id='ocupacao'),
                    html.P(id='idade'),
                    html.P(id='cidade_nasc'),
                    html.P(id='estado_civil'),
                    html.P(id='genero'),
                    html.P(id='cor_raca'),
                    html.P(id='bens')
                    ],
                    style={ 'display': 'inline-block'}
            )],

            style={ 'display': 'inline-block', 'padding':'0 1em 0 0'}
    ),

    html.Br(),
    html.Br(),
    html.Hr(),
    html.Br(),
    html.Br(),
    html.H2('Mapa das Sessões com maior votação do candidato:'),
    html.Br(),
    html.Br(),
    html.Div(
        html.Iframe(id='map',width='90%',height='400')
    )
    ])

@app1.callback(
    Output('map','srcDoc'),
    [Input('yaxis-column', 'value')])
def update_figure(selected_name):
    path_download2 = Path(path_download,"mapa_pref_{}.html".format(selected_name))
    return open(path_download2,'r').read()


@app1.callback(
    Output('photo','src'),
    [Input('yaxis-column', 'value')])
def update_figure2(selected_name):

    path_download3 = Path(path_download2,"{}.webp".format(selected_name))
    encoded_image = base64.b64encode(open(path_download3, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded_image.decode())


@app1.callback(
    Output('nome','children'),
    [Input('yaxis-column', 'value')])
def update_figure3(selected_name):
    return selected_name


@app1.callback([
    Output('email', 'children'),
    Output('votos', 'children'),
    Output('partido', 'children'),
    Output('coligacao', 'children'),
    Output('grau_instrucao', 'children'),
    Output('ocupacao', 'children'),
    Output('idade', 'children'),
    Output('cidade_nasc', 'children'),
    Output('estado_civil', 'children'),
    Output('genero', 'children'),
    Output('cor_raca', 'children'),
    Output('bens', 'children')],
    [Input('yaxis-column', 'value')])
def callback_a(selected_name):
    email=' '
    partido=' '
    coligacao=' '
    grau_instrucao=' '
    ocupacao=' '
    idade=' '
    cidade_nasc=' '
    estado_civil=' '
    genero=' '
    cor_raca=' '
    bens=' '

    if selected_name =='Barjas Negri':
        email='45.psdb.piracicaba@gmail.com'
        votos='71.897 votos'
        partido='PSDB'
        grau_instrucao='Superior Completo'
        ocupacao='Professor de Ensino Superior'
        idade=  '70 (08/12/1950)'
        cidade_nasc='São Paulo'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 1.094.185,00'

        return email, votos, partido, coligacao, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens

    elif selected_name =='Luciano Almeida':
        email='lstda65@gmail.com'
        votos='85.081 votos'
        partido='DEM'
        coligacao='DEM'
        grau_instrucao='Superior Completo'
        ocupacao='Empresário'
        idade='55 (04/10/1965)'
        cidade_nasc='São Paulo'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 34.097.488,00'


    return email, votos, partido, coligacao, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
