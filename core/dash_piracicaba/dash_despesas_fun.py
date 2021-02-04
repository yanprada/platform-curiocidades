# -*- coding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import os
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd
from pathlib import Path
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc


app1 = DjangoDash('Despesas_fun')

#Abre em um chrome com diferentes caminhos para cada sistema peracional
cwd = os.getcwd()
path_download = Path(cwd,"core/Bases/Prefeitura/Despesas/despesa_bimestre_funcao.csv")
#path_download = Path(home,"Yan/Yan/Bases/Prefeitura/Despesas/despesa_bimestre_funcao.csv")

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#Abre em um chrome com diferentes caminhos para cada sistema peracional

df=pd.read_csv(path_download)
df.set_index('Unnamed: 0',inplace=True)

# Função que arruma os numeros do df para formato float:


app1.layout = html.Div(children=[
    html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[
                    {'label': 'Legislativa', 'value': 'Legislativa'},
                    {'label': 'Essencial à Justiça', 'value': 'Essencial à Justiça'},
                    {'label': 'Administração', 'value': 'Administração'},
                    {'label': 'Segurança Pública', 'value': 'Segurança Pública'},
                    {'label': 'Assistência Social', 'value': 'Assistência Social'},
                    {'label': 'Previdência Social', 'value': 'Previdência Social'},
                    {'label': 'Saúde', 'value': 'Saúde'},
                    {'label': 'Educação', 'value': 'Educação'},
                    {'label': 'Trabalho', 'value': 'Trabalho'},
                    {'label': 'Cultura', 'value': 'Cultura'},
                    {'label': 'Direitos da Cidadania', 'value': 'Direitos da Cidadania'},
                    {'label': 'Urbanismo', 'value': 'Urbanismo'},
                    {'label': 'Habitação', 'value': 'Habitação'},
                    {'label': 'Saneamento', 'value': 'Saneamento'},
                    {'label': 'Gestão Ambiental', 'value': 'Gestão Ambiental'},
                    {'label': 'Ciência e Tecnologia', 'value': 'Ciência e Tecnologia'},
                    {'label': 'Agricultura', 'value': 'Agricultura'},
                    {'label': 'Turismo', 'value': 'Turismo'},
                    {'label': 'Transporte', 'value': 'Transporte'},
                    {'label': 'Desporto e Lazer', 'value': 'Desporto e Lazer'},
                    {'label': 'Encargos Especiais', 'value': 'Encargos Especiais'},

                ],
                value='Saúde', style={'height':'3em','background-color':'rgba(252, 152, 3,0.2)','color':'black','font-weight':'bold','position':'center','margin':'10px'}
                )]),

    html.Div([
        dcc.Graph(
            id='despesa')],
        style={'padding': '0 10'})
])

@app1.callback(
    Output('despesa','figure'),
    [Input('yaxis-column', 'value')])
def update_figure(selected_income):
    filtered_df=df[df['Despesas Orçamentárias']==str(selected_income)]


    fig = go.Figure()

    fig.add_trace(go.Scatter(name="Media Móvel",visible='legendonly', x=filtered_df['tempo'],y=filtered_df['DESPESAS LIQUIDADAS NO BIMESTRE'].rolling(6).mean(),
                         line=dict(color='red', width=2)))
    fig.add_trace(go.Scatter(name ="Despesas Realizadas",x=filtered_df['tempo'],y=filtered_df['DESPESAS LIQUIDADAS NO BIMESTRE'],
                         line=dict(color='green', width=2)))
    fig.update_layout(template='plotly_white', xaxis_title='Data',
                   yaxis_title='MILHÕES DE REAIS*',
                   legend=dict(
                               orientation="h",
                               yanchor="bottom",
                               y=1.02,
                               xanchor="right",
                               x=1
                               ))
    fig.add_annotation(text="* A preços de nov/2020 <br>",
                  xref="paper", yref="paper",
                  x=0.03, y=-0.25, showarrow=False)
    fig.update_xaxes( showgrid=True, gridwidth=1, gridcolor='lightgray',showline=True, linewidth=1, linecolor='black')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray',showline=True, linewidth=1, linecolor='black')

    return fig
