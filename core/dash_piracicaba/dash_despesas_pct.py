# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import os
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from pathlib import Path
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import dash_bootstrap_components as dbc


app = DjangoDash('Despesas_pct')

#Abre em um chrome com diferentes caminhos para cada sistema peracional

#*************MODIFICAR O path_download PARA A PASTA DE DOWNLOAD DO SEU PC*************
cwd = os.getcwd()
path_download = Path(cwd,"core/Bases/Prefeitura/Despesas/despesa_ano_pct.csv")

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#Abre em um chrome com diferentes caminhos para cada sistema peracional

df=pd.read_csv(path_download,',')

app.layout = html.Div([dbc.Row(
        [
            dbc.Col(dcc.Graph(id='graph-with-slider'),
                    width=12, lg={'size': 12,  "offset": 0, 'order': 'first'}
                    ),
        ]
    )
    ,
    dcc.Slider(
        id='time-slider',
        min=df['Data'].min(),
        max=df['Data'].max(),
        value=df['Data'].min(),
        marks={str(year): str(year) for year in df['Data'].unique()},
        step=None,
    )
])



@app.callback(
    Output('graph-with-slider','figure'),
    [Input('time-slider', 'value')])
def update_figure(tempo):

    df_parcial = df[df['Data']==int(tempo)]

    colors = ['gold', 'blue','green','darkorange', 'brown','red']

    fig2 = px.pie(df_parcial, names='Tipo Receita',values='%')
    fig2.update_layout(showlegend=False)
    fig2.update_traces(hoverinfo='label+percent', textinfo='label', textfont_size=20,
                      marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    return fig2
