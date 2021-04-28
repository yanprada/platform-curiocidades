from selenium import webdriver
import requests
import time
import os
from pathlib import Path
import pandas as pd
from datetime import datetime

import pathlib
cidade='piracicaba'
parent = pathlib.Path().absolute()
path_download15 = Path(parent,"bases/{}/covid.csv".format(cidade))

def dia_de_ontem(hoje):
    dist = int(hoje.strftime('%d'))-1
    if dist < 10:
        return '0'+str(dist)
    else:
        return str(dist)

hoje = datetime.now()
dhoje = hoje.strftime('%d')
dontem = dia_de_ontem(hoje)
mes= hoje.strftime('%m')
hora = hoje.strftime('%H')

covid = pd.read_csv(path_download15)
covid.drop('Unnamed: 0',axis=1,inplace=True)
here = pathlib.Path().absolute()
path_win = Path(here,"chromedriver_ln")
driver = webdriver.Chrome(path_win)
if int(hora) >=18:
    dias = ['{}'.format(dhoje)]
    meses =['{}'.format(mes)]
else:
    dias = ['{}'.format(dontem)]
    meses =['{}'.format(mes)]
for m in meses:
    for d in dias:
        link = 'http://www.piracicaba.sp.gov.br/categoria/principais+noticias.aspx'
        print(link)
        driver.get(link)
        div_prim = driver.find_elements_by_class_name('imagenet-topico')
        for i in range(len(div_prim)):
            if div_prim[i].text=='› {}/{}/2021 - PLANTÃO CORONAVÍRUS- {}/{}/2021'.format(d,m,d,m):
                div_prim[i].click()
                break
            elif item.text=='› {}/{}/2021 - PLANTÃO CORONAVÍRUS - {}/{}/2021'.format(d,m,d,m):
                item.click()
                break
            else:
                continue
        div= driver.find_element_by_id('imagenet-conteudo')
        novos_obitos = 'NA'
        casos_confirmados = 'NA'
        casos_suspeitos = 'NA'
        casos_descartados = 'NA'
        casos_recuperados = 'NA'
        em_tratamento = 'NA'
        obitos = 'NA'
        homens = 'NA'
        mulheres = 'NA'
        for i in range(len(div.text.split('\n'))):
            if (len(div.text.split('\n')[i].split())<5)&(len(div.text.split('\n')[i].split())>1):
                if div.text.split('\n')[i].split()[-1] =='confirmados':
                    if len(div.text.split('\n')[i].split()[0])>5:
                        casos_confirmados = div.text.split('\n')[i].split()[0][:6]
                    else:
                        casos_confirmados = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[-1] =='suspeitos':
                    if len(div.text.split('\n')[i].split()[0])>5:
                        casos_suspeitos = div.text.split('\n')[i].split()[0][:4]
                    else:
                        casos_suspeitos = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[-1] =='descartados':
                    if len(div.text.split('\n')[i].split()[0])>5:
                        casos_descartados = div.text.split('\n')[i].split()[0][:6]
                    else:
                        casos_descartados = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[-1] =='recuperados':
                    if len(div.text.split('\n')[i].split()[0])>5:
                        casos_recuperados = div.text.split('\n')[i].split()[0][:6]
                    else:
                        casos_recuperados = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[-1] =='tratamento':
                    if len(div.text.split('\n')[i].split()[0])>5:
                        em_tratamento = div.text.split('\n')[i].split()[0][:4]
                    else:
                        em_tratamento = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[-1] =='óbitos':
                    if len(div.text.split('\n')[i].split()[0])>5:
                        obitos = div.text.split('\n')[i].split()[0][:3]
                    else:
                        obitos = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[-1] =='óbito':
                    if len(div.text.split('\n')[i].split()[0])>5:
                        obitos = div.text.split('\n')[i].split()[0][:3]
                    else:
                        obitos = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[0] =='Óbitos-':
                    if len(div.text.split('\n')[i].split()[0])>5:
                        obitos = div.text.split('\n')[i].split()[-1]
                    else:
                        obitos = div.text.split('\n')[i].split()[-1]
                elif div.text.split('\n')[i].split()[0] =='Óbitos':
                    if len(div.text.split('\n')[i].split()[0])>5:
                        obitos = div.text.split('\n')[i].split()[-1]
                    else:
                        obitos = div.text.split('\n')[i].split()[-1]
            elif len(div.text.split('\n')[i].split())>1:
                if div.text.split('\n')[i].split()[1] =='homens:':
                    homens = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[1] =='Homens:':
                    homens = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[1] =='homem:':
                    homens = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[1] =='Homens':
                    homens = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[1] =='homens':
                    homens = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[1] =='homem:':
                    homens = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[1] =='mulheres:':
                    mulheres = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[1] =='Mulheres:':
                    mulheres = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[1] =='mulher:':
                    mulheres = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[1] =='mulheres':
                    mulheres = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[1] =='Mulheres':
                    mulheres = div.text.split('\n')[i].split()[0]
                elif div.text.split('\n')[i].split()[1] =='mulher':
                    mulheres = div.text.split('\n')[i].split()[0]
        dicionario ={'Total Casos Confirmados': int(casos_confirmados.replace('.','')),
                     'Total Casos Suspeitos':int(casos_suspeitos.replace('.','')),
                    'Total Casos Descartados':int(casos_descartados.replace('.','')),
                    'Total Casos Recuperados':int(casos_recuperados.replace('.','')),
                    'Total Casos em Tratamento':int(em_tratamento.replace('.','')),
                     'Total Óbitos':int(obitos.replace('.','')),
                     'Homens':int(homens.replace('.','')),
                     'Mulheres':int(mulheres.replace('.','')),'Data':'{}/{}/2021'.format(d,m)}
        if covid['Data'].iloc[-1]!=dicionario['Data']:
            covid = covid.append(dicionario, ignore_index=True)
            covid['Óbitos Diários'].iloc[-1]=covid['Total Óbitos'].iloc[-1]-covid['Total Óbitos'].iloc[-2]
            covid['Casos Diários'].iloc[-1]=covid['Total Casos Confirmados'].iloc[-1]-covid['Total Casos Confirmados'].iloc[-2]

        covid['Média Móvel Casos'] = covid['Casos Diários'].rolling(7).mean()
        covid['Média Móvel Óbitos'] = covid['Óbitos Diários'].rolling(7).mean()
        covid['Média Móvel Tratamento'] = covid['Total Casos em Tratamento'].rolling(7).mean()
        covid['Média Móvel Suspeitos'] = covid['Total Casos Suspeitos'].rolling(7).mean()

covid.to_csv(path_download15)
driver.quit()
