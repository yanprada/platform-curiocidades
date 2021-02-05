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

app1 = DjangoDash('Vereadores',add_bootstrap_links=True)

#Abre em um chrome com diferentes caminhos para cada sistema peracional
#Abre em um chrome com diferentes caminhos para cada sistema peracional

cwd = os.getcwd()
path_download = Path(cwd,"core/Bases/Camara/Vereadores/Mapa")
path_download2 = Path(cwd,"core/static/assets/img/vereador")


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#Abre em um chrome com diferentes caminhos para cada sistema peracional




app1.layout = html.Div(children=[


    html.Div([

            dcc.Dropdown(
                id='yaxis-column',
                options=[
                    {'label': 'Acácio Godoy', 'value': 'Acácio Godoy'},#infos
                    {'label': 'Paraná', 'value': 'Paraná'},
                    {'label': 'Alessandra Bellucci', 'value': 'Alessandra Protetora Animais'},
                    {'label': 'Ana Lúcia Pavão', 'value': 'Ana Lúcia Pavão'},
                    {'label': 'André Bandeira', 'value': 'André Bandeira'},
                    {'label': 'Anilton Rissato', 'value': 'Anilton Rissato'},
                    {'label': 'Dr. Ary Pedroso', 'value': 'Ary Pedroso Jr'},
                    {'label': 'Cassio Luiz', 'value': 'Cássio Luiz Fala Pira'},
                    {'label': 'Fabrício Polezi', 'value': 'Fabricio Polezi'},#foto
                    {'label': 'Gilmar Rotta', 'value': 'Gilmar Rotta'},
                    {'label': 'Gustavo Pompeo', 'value': 'Gustavo Pompeo'},
                    {'label': 'Josef Borges', 'value': 'Josef Borges'},#foto
                    {'label': 'Laercio Trevisan Jr', 'value': 'Laércio Trevisan Jr'},
                    {'label': 'Paulo Camolesi', 'value': 'Paulo Camolesi'},
                    {'label': 'Paulo Roberto de Campos', 'value': 'Paulo Roberto de Campos'},
                    {'label': 'Paulo Henrique Ribeiro', 'value': 'Paulo Henrique Ribeiro'},
                    {'label': 'Pedro Kawai', 'value': 'Pedro Kawai'},
                    {'label': 'Rai de Almeida', 'value': 'Rai de Almeida'},
                    {'label': 'Relinho', 'value': 'Relinho'},
                    {'label': 'Silvia Mandato Coletivo', 'value': 'Silvia Mandato Coletivo'},
                    {'label': 'Thiago Augusto Ribeiro', 'value': 'Thiago Augusto Ribeiro'},
                    {'label': 'Wagnão', 'value': 'Wagnão'},
                    {'label': 'Zezinho Pereira', 'value': 'Zezinho Pereira'},

                ],
                value='André Bandeira',
                style={'height':'3em','background-color':'rgba(252, 152, 3,0.2)','color':'black'}
                )]),
    html.Br(),
    html.Br(),
    dbc.Row(
            [
                dbc.Col([
                html.Br(),

                html.H1(id='nome'),
                html.P(id='email'),
                html.P(id='votos'),
                html.Hr(),
                html.Br(),
                html.Div(
                        html.Img(id='photo',width='50%',height='50%'),style = {'padding':'2em 2em 2em 2em'}
                ),
                html.Br(),
                html.Div([
                        html.P('Partido: '),
                        html.P('Instrução: '),
                        html.P('Ocupação: '),
                        html.P('Idade: '),
                        html.P('Cidade de Nasc: '),
                        html.P('Estado Civil: '),
                        html.P('Gênero: '),
                        html.P('Cor/Raça: '),
                        html.P('Bens Declarados: '),
                        ],
                        style={ 'display': 'inline-block','padding':'0 1em 0 1em'}
                ),

                html.Div([
                        html.P(id='partido'),
                        html.P(id='grau_instrucao'),
                        html.P(id='ocupacao'),
                        html.P(id='idade'),
                        html.P(id='cidade_nasc'),
                        html.P(id='estado_civil'),
                        html.P(id='genero'),
                        html.P(id='cor_raca'),
                        html.P(id='bens')
                        ],
                        style={ 'display': 'inline-block'})], md=4)
                ,


                dbc.Col([
                html.Br(),
                html.Br(),html.H3('Sessões com maior votação do candidato:'),
                html.Br(),
                html.Br(),
                html.Div(

                    html.Iframe(id='map',width='100%',height='500px'),style = {'margin': 'auto',  'width': '90%'}
                    )],md=8)
        ])
    ])

@app1.callback(
    Output('map','srcDoc'),
    [Input('yaxis-column', 'value')])
def update_figure(selected_name):
    path_download3 = Path(path_download,"mapa_ver_{}.html".format(selected_name))
    return open(path_download3,'r').read()

@app1.callback(
    Output('photo','src'),
    [Input('yaxis-column', 'value')])
def update_figure2(selected_name):

    path_download3 = Path(path_download2,"{}.png".format(selected_name))
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
    grau_instrucao=' '
    ocupacao=' '
    idade=' '
    cidade_nasc=' '
    estado_civil=' '
    genero=' '
    cor_raca=' '
    bens=' '

    if selected_name =='André Bandeira':
        email='bandeira.andre@gmail.com'
        votos='2.484 votos'
        partido='PSDB'
        grau_instrucao='Superior Completo'
        ocupacao='Vereador'
        idade=  '45 (06/01/1975)'
        cidade_nasc='Piracicaba'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 352.535,00'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Alessandra Protetora Animais':
        email='republicanos10.piracicaba@gmail.com'
        votos='1.459 votos'
        partido='REPUBLICANOS'
        grau_instrucao='Superior Completo'
        ocupacao='Empresária'
        idade='46 (31/03/1974)'
        cidade_nasc='São Paulo'
        estado_civil='Solteiro(A)'
        genero='Feminino'
        cor_raca='Branca'
        bens='-'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Paulo Camolesi':
        email='pauloscamolesi@gmail.com'
        votos='1.390 votos'
        partido='PDT'
        grau_instrucao='Ensino Fundamental Incompleto'
        ocupacao='Aposentado'
        idade='68 (10/11/1952)'
        cidade_nasc='Piracicaba'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 417.022,00'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Ana Lúcia Pavão':
        email='plpiracicaba22@gmail.com'
        votos='1.348 votos'
        partido='PL'
        grau_instrucao='Superior Completo'
        ocupacao='Assistente Social'
        idade='42 (19/03/1978)'
        cidade_nasc='Piracicaba'
        estado_civil='Casado(a)'
        genero='Feminino'
        cor_raca='Branca'
        bens='R$ 145.000,00 '

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Paraná':
        email='cidadania23piracicaba@gmail.com'
        votos='1.886 votos'
        partido='CIDADANIA'
        grau_instrucao='Ensino Médio Completo'
        ocupacao='Vereador'
        idade='53 (27/05/1967)'
        cidade_nasc='Inajá'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Parda'
        bens='R$ 83.006,00'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Anilton Rissato':
        email='aniltonrissato@yahoo.com.br'
        votos='1.027 votos'
        partido='PATRIOTA'
        grau_instrucao='Superior Completo'
        ocupacao='Outros'
        idade='53 (14/06/1967)'
        cidade_nasc='Charqueada'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 140.968,00'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Ary Pedroso Jr':
        email='arypedroso@terra.com.br'
        votos='3.063 votos'
        partido='SOLIDARIEDADE'
        grau_instrucao='Superior Completo'
        ocupacao='Médico'
        idade='57 (02/08/1963)'
        cidade_nasc='Piracicaba'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 1.008.804,00'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Cássio Luiz Fala Pira':
        email='plpiracicaba22@gmail.com'
        votos='3.814 votos'
        partido='PL'
        grau_instrucao='Ensino Médio Completo'
        ocupacao='Comerciante'
        idade='42 (26/09/1978)'
        cidade_nasc='Belo Horizonte'
        estado_civil='Solteiro(a)'
        genero='Masculino'
        cor_raca='Preta'
        bens='-'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Fabricio Polezi':
        email='patriotapiracicaba@gmail.com'
        votos='1.023 votos'
        partido='PATRIOTA'
        grau_instrucao='Ensino Médio Completo'
        ocupacao='Torneiro Mecânico'
        idade='41 (15/08/1979)'
        cidade_nasc='Piracicaba'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 310.000,00'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Acácio Godoy':
        email='heliovilani@yahoo.com'
        votos='1.395 votos'
        partido='Progressistas'
        grau_instrucao='Superior Incompleto'
        ocupacao='Comerciante'
        idade='43 (05/08/1977)'
        cidade_nasc='Piracicaba'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Preta'
        bens='R$ 28.435,00'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Gilmar Rotta':
        email='cidadania23piracicaba@gmail.com'
        votos='1.893 votos'
        partido='CIDADANIA'
        grau_instrucao='Superior Completo'
        ocupacao='Vereador'
        idade='54 (29/07/1966)'
        cidade_nasc='Piracicaba'
        estado_civil=' Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 60.667,00'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Gustavo Pompeo':
        email='gustavo-pompeo94@hotmail.com'
        votos='1.055 votos'
        partido='AVANTE'
        grau_instrucao='Ensino Médio Completo'
        ocupacao='Motoboy'
        idade='26 (12/04/1994)'
        cidade_nasc='Piracicaba'
        estado_civil='Solteiro(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 9.800,00'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Paulo Roberto de Campos':
        email='podemospiracicaba@gmail.com'
        votos='3.627 votos'
        partido='PODEMOS'
        grau_instrucao='Superior Completo'
        ocupacao='Advogado'
        idade='40 (27/03/1980)'
        cidade_nasc='Piracicaba'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 19.300,00 '

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Paulo Henrique Ribeiro':
        email='republicanos10.piracicaba@gmail.com'
        votos='2.987 votos'
        partido='REPUBLICANOS'
        grau_instrucao='Superior Completo'
        ocupacao='Jornalista E Redator'
        idade='Jornalista E Redator'
        cidade_nasc='São Paulo'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 274.093,00'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name == 'Pedro Kawai':
        email='pedro.kawai@camarapiracicaba.sp.gov.br'
        votos='1.480 votos'
        partido='PSDB'
        grau_instrucao='Superior Completo'
        ocupacao='Vereador'
        idade='49 (05/03/1971)'
        cidade_nasc='Piracicaba'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='-'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Rai de Almeida':
        email='raidealmeida13@gmail.com'
        votos='1.028 votos'
        partido='PT'
        grau_instrucao='Superior Completo'
        ocupacao='Advogado'
        idade='65 (21/01/1955)'
        cidade_nasc='Sousa'
        estado_civil='Viúvo(a)'
        genero='Feminino'
        cor_raca='Branca'
        bens='R$ 112.457,00'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Relinho':
        email='rerlison@hotmail.com'
        votos='1.477 votos'
        partido='PSDB'
        grau_instrucao='Ensino Fundamental Completo'
        ocupacao='Outros'
        idade='43 (20/06/1977)'
        cidade_nasc='Piracicaba'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 307.800,00'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Silvia Mandato Coletivo':
        email='silviammorales24@gmail.com'
        votos='941 votos'
        partido='PV'
        grau_instrucao='Superior Completo'
        ocupacao='Engenheiro'
        idade='51 (14/07/1969)'
        cidade_nasc='Mauá'
        estado_civil='Divorciado(a)'
        genero='Feminino'
        cor_raca='Branca'
        bens='R$ 847.241,00'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Thiago Augusto Ribeiro':
        email='joel.psc20@gmail.com'
        votos='1.234 votos'
        partido='PSC'
        grau_instrucao='Superior Completo'
        ocupacao='Outros'
        idade='33 (01/09/1987)'
        cidade_nasc='Piracicaba'
        estado_civil='Solteiro(a)'
        genero='Masculino'
        cor_raca='Parda'
        bens='R$ 20.000,00'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Wagnão':
        email='cidadania23piracicaba@gmail.com'
        votos='2.039 votos'
        partido='CIDADANIA'
        grau_instrucao='Ensino Médio Completo'
        ocupacao='Vereador'
        idade='49 (18/04/1971)'
        cidade_nasc='Piracicaba'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Parda'
        bens='R$ 199.500,00'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Laércio Trevisan Jr':
        email='plpiracicaba22@gmail.com'
        votos='2.375 votos'
        partido='PL'
        grau_instrucao='Superior Completo'
        ocupacao = 'Servidor Público Estadual'
        idade='56 (26/02/1964)'
        cidade_nasc='Piracicaba'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='R$ 1.215.947,00'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Zezinho Pereira':
        email='zezinhosedema@gmail.com'
        votos='1.075 votos'
        partido='DEM'
        grau_instrucao='Ensino Fundamental Completo'
        ocupacao='Servidor Público Municipal'
        idade='56 (16/11/1964)'
        cidade_nasc='Piracicaba'
        estado_civil='Solteiro(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='-'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
    elif selected_name =='Josef Borges':
        email='josefborges@yahoo.com.br'
        votos='1.259 votos'
        partido='SOLIDARIEDADE'
        grau_instrucao='Superior Incompleto'
        ocupacao='Empresário'
        idade='50 (27/07/1970)'
        cidade_nasc='Mogi Guaçu'
        estado_civil='Casado(a)'
        genero='Masculino'
        cor_raca='Branca'
        bens='-'

        return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens

    return email, votos, partido, grau_instrucao, ocupacao, idade, cidade_nasc, estado_civil, genero, cor_raca, bens
