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

app1 = DjangoDash('Pref_1')

#Abre em um chrome com diferentes caminhos para cada sistema peracional
cwd = os.getcwd()
path_download = Path(cwd,"core/Bases/Prefeitura/Eleicao/Mapa/1T")
path_download2 = Path(cwd,"core/static/assets/img/prefeitos")
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#Abre em um chrome com diferentes caminhos para cada sistema peracional




app1.layout = html.Div(children=[

    html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[
                    {'label': 'Carlito', 'value': 'Carlito'},
                    {'label': 'Coronel Adriana', 'value': 'Coronel Adriana'},
                    {'label': 'Zé Pedro', 'value': 'Zé Pedro'},
                    {'label': 'Luciano Almeida', 'value': 'Luciano Almeida'},
                    {'label': 'Nancy Thame', 'value': 'Nancy Thame'},
                    {'label': 'Barjas Negri', 'value': 'Barjas Negri'},
                    {'label': 'Érica Gorga', 'value': 'Érica Gorga'},
                    {'label': 'Francys Almeida', 'value': 'Francys Almeida'},
                    {'label': 'Edvaldo Brito', 'value': 'Edvaldo Brito'},
                    {'label': 'Carolina Angelelli', 'value': 'Carolina Angelelli'},
                    {'label': 'Professor Adelino', 'value': 'Professor Adelino'},
                    {'label': 'Mário Neto', 'value': 'Mário Neto'},



                ],
                value='Nancy Thame',
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
        votos='56.760 votos'
        partido='PSDB'
        coligacao='PP / PSC / SOLIDARIEDADE / PSDB / CIDADANIA / PODE / MDB / PSD / REPUBLICANOS / PTB'
        grau_instrucao='Superior Completo'
        ocupacao='Professor de Ensino Superior'
        idade=  '70 (08/12/1950)'
        cidade_nasc='São Paulo'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 1.094.185,00'

        return email, votos, partido, coligacao, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Carlito':
        email='carlitoteves2006@hotmail.com'
        votos='135 votos'
        partido='PTC'
        coligacao ='PTC'
        grau_instrucao='Ensino Médio Completo'
        ocupacao='Empresário'
        idade='42 (24/04/1978)'
        cidade_nasc='Piracicaba'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 13.000,00'

        return email, votos, partido, coligacao, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Carolina Angelelli':
        email='carolangelelli@hotmail.com'
        votos='3.776 votos'
        partido='PDT'
        coligacao ='PDT'
        grau_instrucao='Superior Completo'
        ocupacao='Jornalista E Redator'
        idade='68 (10/11/1952)'
        cidade_nasc='Piracicaba'
        estado_civil='Solteiro (a)'
        genero='Feminino'
        cor_raca='Branca'
        bens='R$ 4.300,00'

        return email, votos, partido, coligacao, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Coronel Adriana':
        email='pslpiracicaba17@gmail.com'
        votos='22.432 votos'
        partido='PSL'
        coligacao='PSL'
        grau_instrucao='Superior Completo'
        ocupacao='Vereadora'
        idade=' 53 (11/10/1967)'
        cidade_nasc='Piracicaba'
        estado_civil='Casado(a)'
        genero='Feminino'
        cor_raca='Branca'
        bens='R$ 535.000,00'

        return email, votos, partido, coligacao, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Edvaldo Brito':
        email='piracicabaviva@gmail.com'
        votos='10.543 votos'
        partido='AVANTE'
        coligacao='AVANTE'
        grau_instrucao='Superior Incompleto'
        ocupacao='Locutor E Comentarista de Rádio E Televisão'
        idade='51 (26/12/1969)'
        cidade_nasc='Ribeirópolis'
        estado_civil='Divorciado (a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='-'

        return email, votos, partido, coligacao, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Francys Almeida':
        email='sindicodiroma@outlook.comr'
        votos='1.098 votos'
        partido='PATRIOTA'
        grau_instrucao='Superior Completo'
        ocupacao='Administrador'
        idade='36 (04/12/1984)'
        cidade_nasc='Maceió'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Parda'
        bens='R$ 175.000,00'

        return email, votos, partido, coligacao, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Luciano Almeida':
        email='lstda65@gmail.com'
        votos='25.786 votos'
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
    elif selected_name =='Mário Neto':
        email='marioemineto@gmail.com'
        votos='2.245 votos'
        partido='PSB'
        coligacao='PSB'
        grau_instrucao='Superior Completo'
        ocupacao='Serventuário de Justiça'
        idade='55 (19/06/1965)'
        cidade_nasc='Piracicaba'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 648.000,00'

        return email, votos, partido, coligacao, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Nancy Thame':
        email='nancythame@gmail.com'
        votos='9.251 votos'
        partido='PV'
        coligacao='PV'
        grau_instrucao='Superior Completo'
        ocupacao='Agrônomo'
        idade='62 (17/11/1958)'
        cidade_nasc='Lucélia'
        estado_civil='Casado(a)'
        genero='Feminino'
        cor_raca='Branca'
        bens='R$ 2.542.119,00'

        return email, votos, partido,coligacao, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Professor Adelino':
        email='adelino.oliveira@terra.com.br '
        votos='12.340 votos'
        partido='PT'
        coligacao='PT / PSOL'
        grau_instrucao='Superior Completo'
        ocupacao='Professor de Ensino Superior'
        idade='47 (09/05/1973)'
        cidade_nasc='São Paulo'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Preta'
        bens='R$ 626.172,00'

        return email, votos, partido, coligacao, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Zé Pedro':
        email='plpiracicaba22@gmail.com'
        votos='6.477 votos'
        partido='PL'
        coligacao='PL'
        grau_instrucao='Superior Completo'
        ocupacao='Empresário'
        idade='68 (20/05/1952)'
        cidade_nasc='Piracicaba'
        estado_civil=' Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 2.612.000,00'

        return email, votos, partido, coligacao, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Érica Gorga':
        email='ericagorga@uol.com.brvv'
        votos='14.470 votos'
        partido='PATRIOTA'
        coligacao='PATRIOTA'
        grau_instrucao='Superior Completo'
        ocupacao='Advogada'
        idade='43 (01/08/1977)'
        cidade_nasc='Piracicaba'
        estado_civil=' Casado(a)'
        genero='Feminino'
        cor_raca='Branca'
        bens='R$ 3.663.737,00'

        return email, votos, partido, coligacao, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens

    return email, votos, partido, coligacao, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
