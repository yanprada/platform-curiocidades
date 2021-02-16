# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
import pandas as pd
import pathlib
from pathlib import Path

def index(request):
    return render(request, 'index.html')


def modulo(x):
    if x > 0:
        return x
    else:
        return x*(-1)



# ----------------------------------------------------------PIRACICABA-----------------------------------------------------

# ---------------------------------------RESUMO-------------------------------------------------

@login_required(login_url="/login/")
def piraresumo(request):
    parente = pathlib.Path().absolute()
    path_download1 = Path(parente,"notebook/bases/piracicaba/receita_bimestres.csv")
    path_download3 = Path(parente,"notebook/bases/piracicaba/despesa_bimestres.csv")

    df=pd.read_csv(path_download3)  #Despesa Corrente
    df_final = pd.read_csv(path_download1)

# -------------Periodo--------------------------
    data_temp = df[df['Despesas Orçamentárias']=='DESPESAS CORRENTES']['Unnamed: 0'].tolist()
    data=[elem.split()[0][:3]+elem.split()[1][-2:] for elem in data_temp ]

    # -------------Receita corrente--------------------------

    dados_rec_corr = df_final[df_final['Receitas Orçamentárias']=='RECEITAS CORRENTES']['Receitas Realizadas no Bimestre (b)'].tolist()
    dados_rec_corr_round=['%.2f' % elem for elem in dados_rec_corr ]

# -------------Despesas Correntes-------------
    dados_des_corr_liq_temp = df[df['Despesas Orçamentárias']=='DESPESAS CORRENTES']['DESPESAS LIQUIDADAS NO BIMESTRE'].tolist()
    dados_des_corr_liq =['%.2f' % elem for elem in dados_des_corr_liq_temp ]



    context = {'data':data,'dados_rec_corr_round':dados_rec_corr_round,'dados_des_corr_liq':dados_des_corr_liq}
    context['segment'] = 'resumo'

    html_template = loader.get_template( 'piracicaba_resumo.html' )
    return HttpResponse(html_template.render(context, request))

# ---------------------------------------RECEITAS PREFEITURA-------------------------------------------------

@login_required(login_url="/login/")
def piraprefrec(request):

    parente = pathlib.Path().absolute()

    path_download1 = Path(parente,"notebook/bases/piracicaba/receita_funcao.csv")
    path_download2 = Path(parente,"notebook/bases/piracicaba/receita_bimestres.csv")

    df_final = pd.read_csv(path_download1)
    df = pd.read_csv(path_download2)
# -------------Periodo--------------------------
    data_temp = df_final[df_final['Receitas Orçamentárias']=='Impostos']['Unnamed: 0'].tolist()
    data=[elem.split()[0][:3]+elem.split()[1][-2:] for elem in data_temp ]

    data2_temp = df[df['Receitas Orçamentárias']=='Impostos']['Unnamed: 0'].tolist()
    data2=[elem.split()[0][:3]+elem.split()[1][-2:] for elem in data2_temp ]


# -------------Receita corrente--------------------------

    dados_rec_corr = df[df['Receitas Orçamentárias']=='RECEITAS CORRENTES']['Receitas Realizadas no Bimestre (b)'].tolist()
    dados_rec_corr_round=['%.2f' % elem for elem in dados_rec_corr ]

# -------------Top 3 receitas--------------------------

    dados_rec_imp = df[df['Receitas Orçamentárias']=='Impostos']['Receitas Realizadas no Bimestre (b)'].tolist()
    dados_rec_imp_round=['%.2f' % elem for elem in dados_rec_imp ]

    dados_rec_transf = df[df['Receitas Orçamentárias']=='TRANSFERÊNCIAS CORRENTES']['Receitas Realizadas no Bimestre (b)'].tolist()
    dados_rec_transf_round=['%.2f' % elem for elem in dados_rec_transf ]

    dados_rec_serv = df[df['Receitas Orçamentárias']=='RECEITA DE SERVIÇOS']['Receitas Realizadas no Bimestre (b)'].tolist()
    dados_rec_serv_round=['%.2f' % elem for elem in dados_rec_serv ]

# -------------Top 10 receitas--------------------------
    df_fim = df_final[df_final['Unnamed: 0']=='dezembro 2020']
    df_fim.sort_values('Receitas Realizadas no Bimestre (b)',inplace=True,ascending=False)
    top10_value_temp = df_fim.iloc[:11]['Receitas Realizadas no Bimestre (b)'].tolist()

    top10_value_temp =['%.2f' % elem for elem in top10_value_temp ]
    top10_value=top10_value_temp[1:]
    top10_name_temp= df_fim.iloc[:11]['Receitas Orçamentárias'].tolist()
    top10_name = top10_name_temp[1:]



# -------------Contexto-------------------------

    context = {'data':data,'data2':data2,'dados_rec_imp_round':dados_rec_imp_round,'dados_rec_corr_round':dados_rec_corr_round,'dados_rec_transf_round':dados_rec_transf_round,
    'dados_rec_serv_round':dados_rec_serv_round,'top10_value':top10_value,'top10_name':top10_name}


    html_template = loader.get_template( 'piracicaba_pref_receitas.html' )
    return HttpResponse(html_template.render(context, request))

# ---------------------------------------DESPESAS PREFEITURA-------------------------------------------------

@login_required(login_url="/login/")
def piraprefdes(request):

    parente = pathlib.Path().absolute()

    path_download2 = Path(parente,"notebook/bases/piracicaba/despesa_bimestre_funcao.csv")
    path_download3 = Path(parente,"notebook/bases/piracicaba/despesa_bimestres.csv")

    path_topo= Path(parente,"notebook/bases/piracicaba/1.csv")
    path_adm= Path(parente,"notebook/bases/piracicaba/2.csv")
    path_seg = Path(parente,"notebook/bases/piracicaba/3.csv")
    path_ass = Path(parente,"notebook/bases/piracicaba/4.csv")
    path_saude = Path(parente,"notebook/bases/piracicaba/5.csv")
    path_edu= Path(parente,"notebook/bases/piracicaba/6.csv")
    path_trab = Path(parente,"notebook/bases/piracicaba/7.csv")
    path_cult = Path(parente,"notebook/bases/piracicaba/8.csv")
    path_urb= Path(parente,"notebook/bases/piracicaba/9.csv")
    path_san = Path(parente,"notebook/bases/piracicaba/10.csv")
    path_gest_amb = Path(parente,"notebook/bases/piracicaba/11.csv")
    path_agr = Path(parente,"notebook/bases/piracicaba/12.csv")
    path_desp = Path(parente,"notebook/bases/piracicaba/13.csv")



    df_final = pd.read_csv(path_download2) #Despesa por função
    df=pd.read_csv(path_download3)#Despesa Corrente
    df_data=pd.read_csv(path_topo)

# -------------Periodo--------------------------
    data_temp = df_data[df_data['Despesas Orçamentárias']=='Legislativa']['Unnamed: 0'].tolist()
    data=[elem.split()[0][:3]+elem.split()[1][-2:] for elem in data_temp ]

    data2_temp = df[df['Despesas Orçamentárias']=='DESPESAS CORRENTES']['Unnamed: 0'].tolist()
    data2=[elem.split()[0][:3]+elem.split()[1][-2:] for elem in data2_temp ]

# -------------Elementos soltos do inicio-------------
    df_topo = pd.read_csv(path_topo)
    df_last_year = df_topo[df_topo['Unnamed: 0']==df_topo['Unnamed: 0'].iloc[-7]]
    df_now = df_topo[df_topo['Unnamed: 0']==df_topo['Unnamed: 0'].iloc[-1]]

    df_now.set_index('Despesas Orçamentárias',inplace=True)
    df_last_year.set_index('Despesas Orçamentárias',inplace=True)

    df_pct = pd.DataFrame()
    df_pct['Valor']= df_now['DESPESAS LIQUIDADAS NO BIMESTRE']
    df_pct['Diferença']  = df_now['DESPESAS LIQUIDADAS NO BIMESTRE'] - df_last_year['DESPESAS LIQUIDADAS NO BIMESTRE']
    df_pct['Diferença Absoluto'] = df_pct['Diferença'].apply(modulo)
    df_pct['Porcentagem']  = (100*(df_now['DESPESAS LIQUIDADAS NO BIMESTRE'] - df_last_year['DESPESAS LIQUIDADAS NO BIMESTRE']))/df_last_year['DESPESAS LIQUIDADAS NO BIMESTRE']
    df_pct['Porcentagem Absoluto'] = df_pct['Porcentagem'].apply(modulo)
    df_pct.sort_values('Diferença Absoluto',inplace=True,ascending=False)
    df_pct.drop(['Porcentagem Absoluto','Diferença Absoluto'],axis=1,inplace=True)

    df_valor_temp1 = df_pct.sort_values('Valor',ascending=False)
    df_valor_temp1['Valor_round'] = ['%.2f' % elem for elem in df_valor_temp1['Valor'] ]
    # -------------radius-------------
    lst_valor = df_valor_temp1[:10]['Valor_round'].tolist()
    lst_nome = df_valor_temp1[:10].index.tolist()
    # -------------------------
    nome_1 = df_pct.index.tolist()[0]

    pct_1 = round(df_pct['Porcentagem'].tolist()[0])
    valor_1 = round(df_pct['Diferença'].tolist()[0])

    nome_2 = df_pct.index.tolist()[1]

    pct_2= round(df_pct['Porcentagem'].tolist()[1])
    valor_2= round(df_pct['Diferença'].tolist()[1])

    nome_3 = df_pct.index.tolist()[2]

    pct_3= round(df_pct['Porcentagem'].tolist()[2])
    valor_3= round(df_pct['Diferença'].tolist()[2])

    nome_4 = df_pct.index.tolist()[3]

    pct_4 = round(df_pct['Porcentagem'].tolist()[3])
    valor_4 = round(df_pct['Diferença'].tolist()[3])

    nome_5 = df_pct.index.tolist()[4]

    pct_5 = round(df_pct['Porcentagem'].tolist()[4])
    valor_5 = round(df_pct['Diferença'].tolist()[4])

    nome_6 = df_pct.index.tolist()[5]

    pct_6 = round(df_pct['Porcentagem'].tolist()[5])
    valor_6 = round(df_pct['Diferença'].tolist()[5])


# -------------Despesas Correntes-------------
    dados_des_corr_liq_temp = df[df['Despesas Orçamentárias']=='DESPESAS CORRENTES']['DESPESAS LIQUIDADAS NO BIMESTRE'].tolist()
    dados_des_corr_liq =['%.2f' % elem for elem in dados_des_corr_liq_temp ]

    dados_des_corr_emp_temp = df[df['Despesas Orçamentárias']=='DESPESAS CORRENTES']['DESPESAS EMPENHADAS NO BIMESTRE'].tolist()
    dados_des_corr_emp =['%.2f' % elem for elem in dados_des_corr_emp_temp ]



# -------------Top 3 despesas-------------
    dados_des_sau_temp= df_final[df_final['Despesas Orçamentárias']=='Saúde']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    dados_des_sau =['%.2f' % elem for elem in dados_des_sau_temp ]

    dados_des_edu_temp = df_final[df_final['Despesas Orçamentárias']=='Educação']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    dados_des_edu =['%.2f' % elem for elem in dados_des_edu_temp ]

    dados_des_san_temp = df_final[df_final['Despesas Orçamentárias']=='Saneamento']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    dados_des_san =['%.2f' % elem for elem in dados_des_san_temp ]



# -----------Saúde---------------

    df_saude = pd.read_csv(path_saude)


    saude1_temp = df_saude[df_saude['Despesas Orçamentárias']=='Atenção Básica']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    saude1 =['%.2f' % elem for elem in saude1_temp ]

    saude2_temp= df_saude[df_saude['Despesas Orçamentárias']=='Assistência Hospitalar e Ambulatorial']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    saude2=['%.2f' % elem for elem in saude2_temp ]

    saude3_temp= df_saude[df_saude['Despesas Orçamentárias']=='FU10 - Administração Geral']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    saude3=['%.2f' % elem for elem in saude3_temp ]

# -----------Educação---------------

    df_edu = pd.read_csv(path_edu)

    edu1_temp = df_edu[df_edu['Despesas Orçamentárias']=='Ensino Fundamental']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    edu1 =['%.2f' % elem for elem in edu1_temp ]

    edu2_temp = df_edu[df_edu['Despesas Orçamentárias']=='Ensino Médio']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    edu2 =['%.2f' % elem for elem in edu2_temp ]

    edu3_temp = df_edu[df_edu['Despesas Orçamentárias']=='Ensino Profissional']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    edu3 =['%.2f' % elem for elem in edu3_temp ]

    edu4_temp = df_edu[df_edu['Despesas Orçamentárias']=='Ensino Superior']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    edu4 =['%.2f' % elem for elem in edu4_temp ]

    edu5_temp = df_edu[df_edu['Despesas Orçamentárias']=='Educação Infantil']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    edu5 =['%.2f' % elem for elem in edu5_temp ]




# -----------Saneamento---------------

    df_san = pd.read_csv(path_san)

    san1_temp = df_san[df_san['Despesas Orçamentárias']=='Saneamento Básico Urbano']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    san1 =['%.2f' % elem for elem in san1_temp ]

    san2_temp = df_san[df_san['Despesas Orçamentárias']=='FU17 - Administração Geral']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    san2 =['%.2f' % elem for elem in san2_temp ]


# -----------Assistencia Social--------------


    df_ass = pd.read_csv(path_ass)

    ass1_temp = df_ass[df_ass['Despesas Orçamentárias']=='Assistência à Criança e ao Adolescente']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    ass1 =['%.2f' % elem for elem in ass1_temp ]

    ass2_temp = df_ass[df_ass['Despesas Orçamentárias']=='Assistência Comunitária']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    ass2 =['%.2f' % elem for elem in ass2_temp ]


# -----------Gestão Ambiental--------------


    df_gest_amb = pd.read_csv(path_gest_amb)

    gest_amb1_temp = df_gest_amb[df_gest_amb['Despesas Orçamentárias']=='Preservação e Conservação Ambiental']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    gest_amb1 =['%.2f' % elem for elem in gest_amb1_temp ]

    gest_amb2_temp = df_gest_amb[df_gest_amb['Despesas Orçamentárias']=='Controle Ambiental']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    gest_amb2 =['%.2f' % elem for elem in gest_amb2_temp ]

    gest_amb3_temp = df_gest_amb[df_gest_amb['Despesas Orçamentárias']=='FU18 - Administração Geral']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    gest_amb3 =['%.2f' % elem for elem in gest_amb3_temp ]


# -----------Urbanismo--------------


    df_urb = pd.read_csv(path_urb)

    urb1_temp = df_urb[df_urb['Despesas Orçamentárias']=='Infra-Estrutura Urbana']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    urb1 =['%.2f' % elem for elem in urb1_temp ]

    urb2_temp = df_urb[df_urb['Despesas Orçamentárias']=='Serviços Urbanos']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    urb2 =['%.2f' % elem for elem in urb2_temp ]

    urb3_temp = df_urb[df_urb['Despesas Orçamentárias']=='Transportes Coletivos Urbanos']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    urb3 =['%.2f' % elem for elem in urb3_temp ]

# ----------Administração-------------


    df_adm = pd.read_csv(path_adm)

    adm1_temp = df_adm[df_adm['Despesas Orçamentárias']=='Administração Financeira']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    adm1 =['%.2f' % elem for elem in adm1_temp ]

    adm2_temp = df_adm[df_adm['Despesas Orçamentárias']=='Normatização e Fiscalização']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    adm2 =['%.2f' % elem for elem in adm2_temp ]

    adm3_temp = df_adm[df_adm['Despesas Orçamentárias']=='Tecnologia da Informação']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    adm3 =['%.2f' % elem for elem in adm3_temp ]

    adm4_temp = df_adm[df_adm['Despesas Orçamentárias']=='Comunicação Social']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    adm4=['%.2f' % elem for elem in adm4_temp ]

    adm5_temp = df_adm[df_adm['Despesas Orçamentárias']=='FU04 - Administração Geral']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    adm5=['%.2f' % elem for elem in adm5_temp ]

# ----------Segurança Publica-------------
    listSeg = ['Policiamento','Defesa Civil', 'Informação e Inteligência']

    df_seg = pd.read_csv(path_seg)

    seg1_temp = df_seg[df_seg['Despesas Orçamentárias']=='Policiamento']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    seg1 =['%.2f' % elem for elem in seg1_temp ]

    seg2_temp = df_seg[df_seg['Despesas Orçamentárias']=='Defesa Civil']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    seg2 =['%.2f' % elem for elem in seg2_temp ]

    seg3_temp = df_seg[df_seg['Despesas Orçamentárias']=='Informação e Inteligência']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    seg3 =['%.2f' % elem for elem in seg3_temp ]


# ----------Trabalho-------------

    df_trab = pd.read_csv(path_trab)

    trab1_temp = df_trab[df_trab['Despesas Orçamentárias']=='Proteção e Benefícios ao Trabalhador']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    trab1 =['%.2f' % elem for elem in trab1_temp ]

    trab2_temp = df_trab[df_trab['Despesas Orçamentárias']=='Relações de Trabalho']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    trab2 =['%.2f' % elem for elem in trab2_temp ]


# ----------Cultura-------------

    df_cult = pd.read_csv(path_cult)

    cult1_temp = df_cult[df_cult['Despesas Orçamentárias']=='Patrimônio Histórico Artístico e Arqueológico']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    cult1 =['%.2f' % elem for elem in cult1_temp ]

    cult2_temp = df_cult[df_cult['Despesas Orçamentárias']=='Difusão Cultural']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    cult2 =['%.2f' % elem for elem in cult2_temp ]


# ----------Agricultura-------------

    df_agr = pd.read_csv(path_agr)

    listaAgr=['Abastecimento', 'Extensão Rural', 'Irrigação',
        'Promoção da Produção Agropecuária', 'Defesa Agropecuária','FU20 - Administração Geral']

    agr1_temp = df_agr[df_agr['Despesas Orçamentárias']=='Abastecimento']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    agr1 =['%.2f' % elem for elem in agr1_temp ]

    agr2_temp = df_agr[df_agr['Despesas Orçamentárias']=='Extensão Rural']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    agr2 =['%.2f' % elem for elem in agr2_temp ]

    agr3_temp = df_agr[df_agr['Despesas Orçamentárias']=='FU20 - Administração Geral']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    agr3 =['%.2f' % elem for elem in agr3_temp ]

# ----------Desporto------------

    df_desp = pd.read_csv(path_desp)

    listaDesp=['Desporto de Rendimento', 'Desporto Comunitário', 'Lazer','FU27 - Administração Geral']

    desp1_temp = df_desp[df_desp['Despesas Orçamentárias']=='Desporto de Rendimento']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    desp1 =['%.2f' % elem for elem in desp1_temp ]

    desp2_temp = df_desp[df_desp['Despesas Orçamentárias']=='Desporto Comunitário']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    desp2 =['%.2f' % elem for elem in desp2_temp ]

    desp3_temp = df_desp[df_desp['Despesas Orçamentárias']=='Lazer']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    desp3 =['%.2f' % elem for elem in desp3_temp ]

    desp4_temp = df_desp[df_desp['Despesas Orçamentárias']=='FU27 - Administração Geral']['DESPESAS LIQUIDADAS NO BIMESTRE'].values.tolist()
    desp4 =['%.2f' % elem for elem in desp4_temp ]




    context = {'data':data, 'data2':data2,'nome_1':nome_1 ,'nome_2':nome_2 ,'nome_3':nome_3 ,'nome_4':nome_4 ,'nome_5':nome_5 ,'nome_6':nome_6,
    'pct_1':pct_1 ,'pct_2':pct_2 ,'pct_3':pct_3 ,'pct_4':pct_4 ,'pct_5':pct_5,'pct_6':pct_6,
    'valor_1':valor_1 ,'valor_2':valor_2 ,'valor_3':valor_3 ,'valor_4':valor_4 ,'valor_5':valor_5,'valor_6':valor_6,
    'lst_valor':lst_valor,'lst_nome':lst_nome,
    'dados_des_sau':dados_des_sau, 'dados_des_edu':dados_des_edu, 'dados_des_san':dados_des_san, 'dados_des_corr_liq':dados_des_corr_liq,'dados_des_corr_emp':dados_des_corr_emp,
    'saude1':saude1,'saude2':saude2,'saude3':saude3,'edu1':edu1,'edu2':edu2,'edu3':edu3,'edu4':edu4,'edu5':edu5,'san1':san1,'san2':san2,'ass1':ass1,'ass2':ass2,'gest_amb1':gest_amb1,
    'gest_amb2':gest_amb2,'gest_amb3':gest_amb3,
    'urb1':urb1,'urb2':urb2,'urb3':urb3,'adm1':adm1,'adm2':adm2,'adm3':adm3,'adm4':adm4,'adm5':adm5,'seg1':seg1,'seg2':seg2,'seg3':seg3,
    'trab1':trab1,'trab2':trab2,'cult1':cult1,'cult2':cult2,'agr1':agr1,'agr2':agr2,'agr3':agr3,
    'desp1':desp1,'desp2':desp2,'desp3':desp3,'desp4':desp4,}


    html_template = loader.get_template( 'piracicaba_pref_despesas.html' )
    return HttpResponse(html_template.render(context, request))

# --------------------------------------DEMAIS PÁGINAS---------------------------------------------------------
@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
