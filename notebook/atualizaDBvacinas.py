from selenium import webdriver
import requests
import time
import os
from pathlib import Path
import pandas as pd
from datetime import datetime

import pathlib
import shutil

def ontem(hoje):
    distD = int(hoje.strftime('%d'))-1
    distM = int(hoje.strftime('%m'))
    distA = 21
    if distD < 10:
        return '0{}/0{}/{}'.format(str(distD),str(distM),str(distA))
    return '{}/0{}/{}'.format(str(distD),str(distM),str(distA))

def dia_de_anteontem(hoje):
    dist = int(hoje.strftime('%d'))-2
    if dist < 10:
        return '0'+str(dist)
    else:
        return str(dist)

def dia_de_ontem(hoje):
    dist = int(hoje.strftime('%d'))-1
    if dist < 10:
        return '0'+str(dist)
    else:
        return str(dist)


def download_wait(directory, timeout, nfiles=None):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < timeout:
        time.sleep(1)
        dl_wait = False
        files = os.listdir(directory)
        if nfiles and len(files) != nfiles:
            dl_wait = True

        for fname in files:
            if fname.endswith('.crdownload'):
                dl_wait = True

        seconds += 1
    return seconds

def download_check(directory, file_name):
    seconds = 0
    no_dl = True
    files = os.listdir(directory)
    for fname in files:
        if fname.endswith('{}'.format(file_name)):
            return True
    raise ValueError("Nao está")

lista=['isolamento','vacinometro']
home = Path.home()
parent = pathlib.Path().absolute()
d = Path(home,'Downloads')
cidade='piracicaba'
t=Path(parent,"bases/{}/".format(cidade))
source_dir = d
target_dir = t
here = pathlib.Path().absolute()
path_win = Path(here,"chromedriver_ln")
path_download19 = Path(parent,"bases/{}/vacinas.csv".format(cidade))
path_download20 = Path(parent,"bases/{}/isolamento.csv".format(cidade))

hoje = datetime.now()
dhoje = hoje.strftime('%d')
dontem = dia_de_ontem(hoje)
danteontem = dia_de_anteontem(hoje)
mes= hoje.strftime('%m')
hora = hoje.strftime('%H')
noite=False
for item in lista:
    driver = webdriver.Chrome(path_win)


    link1 = "https://www.saopaulo.sp.gov.br/wp-content/uploads/2021/{}/2021{}{}_{}.csv".format(mes,mes,dhoje,item)
    link2= "https://www.saopaulo.sp.gov.br/wp-content/uploads/2021/{}/2021{}{}_{}.csv".format(mes,mes,dontem,item)


    t1=Path(parent,"bases/{}/2021{}{}_{}.csv".format(cidade,mes,dhoje,item))
    t2=Path(parent,"bases/{}/2021{}{}_{}.csv".format(cidade,mes,dontem,item))
    t3=Path(parent,"bases/{}/2021{}{}_{}.csv".format(cidade,mes,danteontem,item))

    d1=Path(d,"2021{}{}_{}.csv".format(mes,dhoje,item))
    d11=Path(d,"2021{}{}_{} (1).csv".format(mes,dhoje,item))
    d2=Path(d,"2021{}{}_{}.csv".format(mes,dontem,item))
    d21=Path(d,"2021{}{}_{} (1).csv".format(mes,dontem,item))
    d3=Path(d,"2021{}{}_{}.csv".format(mes,danteontem,item))
    d31=Path(d,"2021{}{}_{} (1).csv".format(mes,danteontem,item))


    arq1 = "2021{}{}_{}.csv".format(mes,dhoje,item)
    arq2 = "2021{}{}_{}.csv".format(mes,dontem,item)
    arq3 = "2021{}{}_{}.csv".format(mes,danteontem,item)

    try:
        noite=True
        data_str = hoje.strftime('%y-%m-%d')
        data= datetime.strptime(data_str, '%y-%m-%d')
        data = '{}-0{}-{}'.format(data.year, data.month, data.day)
        if (item == 'isolamento'):
            driver.get(link1)
            driver.implicitly_wait(10)
            download_wait(d,130)
            download_check(d,'isolamento.csv')
            driver.quit()
        elif (item == 'vacinometro'):
            driver.get(link1)
            driver.implicitly_wait(10)
            download_wait(d,130)
            download_check(d,'vacinometro.csv')
            driver.quit()
        elif (item == 'leitos_ocupados_por_unidade_hospitalar'):
            driver.get(link1)
            driver.implicitly_wait(10)
            download_wait(d,130)
            download_check(d,'leitos_ocupados_por_unidade_hospitalar.csv')
            driver.quit()
        else:
            raise ValueError("Nao está")

    except:
        noite=False
        data = ontem(hoje)
        data= datetime.strptime(data, '%d/%m/%y')
        data = '{}-0{}-{}'.format(data.year, data.month, data.day)
        if (item == 'isolamento'):
            driver.get(link2)
            driver.implicitly_wait(10)
            download_wait(d,130)
            driver.quit()
        else:
            driver.get(link2)
            driver.implicitly_wait(10)
            download_wait(d,30)
            driver.quit()


    file_names = os.listdir(source_dir)

    for file_name in file_names:
        if noite:
            if (file_name==arq1) and not(t1.is_file()):
                shutil.move(os.path.join(source_dir, file_name), target_dir)
        else:
            if file_name==arq2 and not(t2.is_file()):
                shutil.move(os.path.join(source_dir, file_name), target_dir)
            continue

    if (t2.is_file())&(t1.is_file())& noite :
        os.remove(t2)

    elif (t3.is_file()) & (t2.is_file()):
        os.remove(t3)

    if d1.is_file():
        os.remove(d1)
    if d2.is_file():
        os.remove(d2)
    if d3.is_file():
        os.remove(d3)
    if d11.is_file():
        os.remove(d11)
    if d21.is_file():
        os.remove(d21)
    if d31.is_file():
        os.remove(d31)

    if noite:
        try:
            df = pd.read_csv(t1,';')
        except FileNotFoundError:
            df = pd.read_csv(t2,';')
    else:
        df = pd.read_csv(t2,';')

    if item=='isolamento':
        vacinas =pd.DataFrame()
        try:
            df = df[df['Município1'] == 'PIRACICABA']
        except:
            df = df[df.iloc[:,0] == 'PIRACICABA']

        vacinas = vacinas.append(df,ignore_index=True)
        vacinas.to_csv(path_download20,index=False)
    elif item=='vacinometro':
        vacinas = pd.read_csv(path_download19)
        try:
            df = df[df['Municipio'] == 'PIRACICABA']
            df['Data'] = data
        except:
            df = df[df.iloc[:,0] == 'PIRACICABA']
            df['Data'] = data
        if vacinas['Data'].iloc[-1]!= data:
            if len(df)<2:
                    if df.Dose.iloc[0]=='1° Dose':
                        linha=df[df.Dose=='1° Dose']
                        linha['Dose']='2° Dose'
                        linha['Contagem de Id Vacinacao']=vacinas['Contagem de Id Vacinacao'].iloc[-2]
                        vacinas = vacinas.append(linha,ignore_index=True)
                        vacinas = vacinas.append(df,ignore_index=True)
                    else:
                        vacinas = vacinas.append(df,ignore_index=True)
                        linha=df[df.Dose=='2° Dose']
                        linha['Dose']='1° Dose'
                        linha['Contagem de Id Vacinacao']=vacinas['Contagem de Id Vacinacao'].iloc[-1]
                        vacinas = vacinas.append(linha,ignore_index=True)
            else:
                vacinas = vacinas.append(df,ignore_index=True)
        else:
            continue
        vacinas.to_csv(path_download19,index=False)
    else:
        continue
