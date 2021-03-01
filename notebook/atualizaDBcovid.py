cidade='piracicaba'
path_download15 = Path(parent,"bases/{}/covid.csv".format(cidade))

hoje = datetime.now()
dhoje = hoje.strftime('%d')
mes= hoje.strftime('%m')

covid = pd.read_csv(path_download15)
covid.drop('Unnamed: 0',axis=1,inplace=True)
here = pathlib.Path().absolute()
path_win = Path(here,"chromedriver_ln")
driver = webdriver.Chrome(path_win)

dias = ['{}'.format(dhoje)]
meses =['{}'.format(mes)]
for m in meses:
    for d in dias:
        link = 'http://www.piracicaba.sp.gov.br/plantao+coronavirus+{}+{}+2021.aspx'.format(d,m)
        print(link)
        driver.get(link)
        div = driver.find_element_by_id('imagenet-conteudo')
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
                        casos_suspeitos = div.text.split('\n')[i].split()[0][:6]
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
                        em_tratamento = div.text.split('\n')[i].split()[0][:6]
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
        covid = covid.append(dicionario, ignore_index=True)
        covid['Óbitos Diários'].iloc[-1]=covid['Total Óbitos'].iloc[-1]-covid['Total Óbitos'].iloc[-2]
        covid['Casos Diários'].iloc[-1]=covid['Total Casos Confirmados'].iloc[-1]-covid['Total Casos Confirmados'].iloc[-2]
driver.quit()
