# ------------IMPORTS-------------
from selenium import webdriver
import requests
import time
import os
from pathlib import Path
import pandas as pd
from datetime import datetime
import pathlib
import camelot
# -----------FUNCTIONS------------

def dia_de_ontem(hoje):
    dist = int(hoje.strftime('%d'))-1
    if dist < 10:
        return '0'+str(dist)
    else:
        return str(dist)

# -------------PATHS-----------------

cidade='piracicaba'
parent = pathlib.Path().absolute()
path_download15 = Path(parent,"bases/{}/sessoes.csv".format(cidade))
here = pathlib.Path().absolute()
path_win = Path(here,"chromedriver_ln")
driver = webdriver.Chrome(path_win)
base_df = pd.read_csv(path_download15)

# --------------TIME (HOURS,DAYS,MONTHS)-------------------
hoje = datetime.now()
dhoje = hoje.strftime('%d')
dontem = dia_de_ontem(hoje)
mes= hoje.strftime('%m')
hora = hoje.strftime('%H')


# --------------LOGIC-------------------


# -----------set dias and meses------------------
dias = ['{}'.format(dontem)]
meses =['{}'.format(mes)]


# -----------run in selected dias e meses
for m in meses:
    for d in dias:
        data='2021-{}-{}'.format(m,d)
        link = 'https://siave.camarapiracicaba.sp.gov.br/sessoes'  # fixed link
        print(link)
        driver.get(link)
        div_prim = driver.find_elements_by_xpath("//table/tbody/tr")
        achou=False
        endereco=False
        for i in range(len(div_prim)): #run trought the list of news of Prefeitura
            if (len(div_prim[i].text.split()) >= 6) and (div_prim[i].text.split()[-2]=='{}/{}/2021'.format(d,m)):  #select the dia and mes
                j=i+1
                item = driver.find_elements_by_xpath("//table/tbody/tr[{}]/td".format(j))
                link = driver.find_element_by_link_text('{}'.format(item[0].text))
                link.click()
                achou=True
                break
            else:
                continue
        if achou:
            link = driver.find_element_by_link_text('RELATÓRIO DE VOTAÇÃO')
            link.click()
            pdf= driver.find_elements_by_xpath("//table/tbody/tr[1]/td[2]")
            pdf[0].click()
            url = driver.current_url
            endereco=True
        if achou==False:
            driver.quit()
            break

        if endereco:
            file = '{}'.format(url)
            todo = camelot.read_pdf(file,pages='all')
            for i in range(len(todo)):
                print('{}/{}'.format(j,i))
                if todo[i].df.iloc[0,0].split('\n')[6]!='0':
                    vereador = todo[i].df.iloc[0,0].split('\n')[15]
                    if len(todo[i].df.iloc[0,0].split('\n'))<=29:
                        ementa = todo[i].df.iloc[0,0].split('\n')[17]+todo[i].df.iloc[0,0].split('\n')[18]
                    elif len(todo[i].df.iloc[0,0].split('\n'))==30:
                        ementa = todo[i].df.iloc[0,0].split('\n')[17]+todo[i].df.iloc[0,0].split('\n')[18]+ todo[i].df.iloc[0,0].split('\n')[19]
                    elif len(todo[i].df.iloc[0,0].split('\n'))==31:
                        ementa = todo[i].df.iloc[0,0].split('\n')[17]+todo[i].df.iloc[0,0].split('\n')[18]+ todo[i].df.iloc[0,0].split('\n')[19]+ todo[i].df.iloc[0,0].split('\n')[20]
                    elif len(todo[i].df.iloc[0,0].split('\n'))==32:
                        ementa = todo[i].df.iloc[0,0].split('\n')[17]+todo[i].df.iloc[0,0].split('\n')[18]+ todo[i].df.iloc[0,0].split('\n')[19]+ todo[i].df.iloc[0,0].split('\n')[20]+ todo[i].df.iloc[0,0].split('\n')[21]
                    elif len(todo[i].df.iloc[0,0].split('\n'))==33:
                        ementa = todo[i].df.iloc[0,0].split('\n')[17]+todo[i].df.iloc[0,0].split('\n')[18]+ todo[i].df.iloc[0,0].split('\n')[19]+ todo[i].df.iloc[0,0].split('\n')[20]+ todo[i].df.iloc[0,0].split('\n')[21]+ todo[i].df.iloc[0,0].split('\n')[22]
                    presentes = int(todo[i].df.iloc[0,1].split('\n')[0])
                    ausentes = int(todo[i].df.iloc[0,1].split('\n')[2])
                    if len(todo[i].df.iloc[1,1].split('\n')[0])<3:
                        sim = int(todo[i].df.iloc[1,1].split('\n')[0])
                        nao = int(todo[i].df.iloc[1,1].split('\n')[2])
                        abst= int(todo[i].df.iloc[1,1].split('\n')[4])
                    else:
                        sim = int(todo[i].df.iloc[1,1].split('\n')[1])
                        nao = int(todo[i].df.iloc[1,1].split('\n')[0].split()[0])
                        abst= int(todo[i].df.iloc[1,1].split('\n')[0].split()[1])
                    status=todo[i].df.iloc[2,1]
                    tempo_vot = todo[i].df.iloc[0,0].split('\n')[-3]
                    dicionario = {'Data':data,'Propositor':vereador,'Ementa':ementa,'Presentes':presentes,
                                'Votos a Favor':sim,'Votos Contrários':nao, 'Status':status,'Tempo de Votação':tempo_vot}
                    base_df=base_df.append(dicionario,ignore_index=True)
                    driver.quit()
                else:
                    continue
base_df.to_csv(path_download15,index=False)
