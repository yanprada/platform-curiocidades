from selenium import webdriver
import requests
import time
import os
from pathlib import Path
import pandas as pd
from datetime import datetime

import pathlib
import shutil


def dia_de_anteontem(hoje):
    dist = int(hoje.strftime('%d'))-2
    if dist < 10:
        return 'O'+str(dist)
    else:
        return str(dist)

def dia_de_ontem(hoje):
    dist = int(hoje.strftime('%d'))-1
    if dist < 10:
        return 'O'+str(dist)
    else:
        return str(dist)


def download_wait(path_to_downloads):
    seconds = 0
    dl_wait = True
    while dl_wait and seconds < 10:
        time.sleep(0.2)
        dl_wait = False
        for fname in os.listdir(path_to_downloads):
            if fname.endswith('.xlsx'):
                dl_wait = True
        seconds += 1
    return seconds

home = Path.home()
parent = pathlib.Path().absolute()
cidade='piracicaba'
path_download = Path(parent,"bases/{}/vacinometro.csv".format(cidade))
d = Path(home,'Downloads')
t=Path(parent,"bases/{}/".format(cidade))
source_dir = d
target_dir = t

here = pathlib.Path().absolute()

path_win = Path(here,"chromedriver_ln")
driver = webdriver.Chrome(path_win)


hoje = datetime.now()
data = hoje.strftime('%d/%m/%y')
dhoje = hoje.strftime('%d')
dontem = dia_de_ontem(hoje)
danteontem = dia_de_anteontem(hoje)
mes= hoje.strftime('%m')
hora = hoje.strftime('%H')
noite=False

if int(hora)<18:
    link= "https://www.saopaulo.sp.gov.br/wp-content/uploads/2021/{}/2021{}{}_vacinometro.csv".format(mes,mes,dontem)
else:
    noite=True
    link = "https://www.saopaulo.sp.gov.br/wp-content/uploads/2021/{}/2021{}{}_vacinometro.csv".format(mes,mes,dhoje)





t1=Path(parent,"bases/{}/2021{}{}_vacinometro.csv".format(cidade,mes,dhoje))
t2=Path(parent,"bases/{}/2021{}{}_vacinometro.csv".format(cidade,mes,dontem))
t3=Path(parent,"bases/{}/2021{}{}_vacinometro.csv".format(cidade,mes,danteontem))

d1=Path(d,"2021{}{}_vacinometro.csv".format(mes,dhoje))
d11=Path(d,"2021{}{}_vacinometro(1).csv".format(mes,dhoje))
d2=Path(d,"2021{}{}_vacinometro.csv".format(mes,dontem))
d21=Path(d,"2021{}{}_vacinometro(1).csv".format(mes,dontem))
d3=Path(d,"2021{}{}_vacinometro.csv".format(mes,danteontem))
d31=Path(d,"2021{}{}_vacinometro(1).csv".format(mes,danteontem))


arq1 = "2021{}{}_vacinometro.csv".format(mes,dhoje)
arq2 = "2021{}{}_vacinometro.csv".format(mes,dontem)
arq3 = "2021{}{}_vacinometro.csv".format(mes,danteontem)


driver.get(link)
driver.implicitly_wait(10)
download_wait(d)
driver.quit()


vacinas=pd.read_csv(path_download,',')
file_names = os.listdir(source_dir)
for file_name in file_names:
    if noite:
        if (file_name==arq1) and not(t1.is_file()):
            shutil.move(os.path.join(source_dir, file_name), target_dir)
    else:
        if file_name==arq2:
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

df = pd.read_csv(t1,';')
df = df[df['Municipio'] == 'PIRACICABA']
df['Data'] = data
if vacinas['Data'].iloc[0]!= data:
    vacinas = vacinas.append(df,ignore_index=True)
vacinas.to_csv(path_download,index=False)
