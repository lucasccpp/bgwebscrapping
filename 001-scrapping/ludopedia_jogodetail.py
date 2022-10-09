from email.quoprimime import quote
import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep
import csv

def request(msg, slp=1):
    '''A wrapper to make robust https requests.'''
    status_code = 500  # Want to get a status-code of 200
    while status_code != 200:
        sleep(slp)  # Don't ping the server too often
        try:
            r = requests.get(msg)
            status_code = r.status_code
            if status_code != 200:
                print("Server Error! Response Code %i. Retrying..." % (r.status_code))
        except:
            print("An exception has occurred, probably a momentory loss of connection. Waiting one seconds...")
            sleep(10)
    return r

def getDadosJogo(linkJogo,idJogo):

    #urlBusca = 'https://www.ludopedia.com.br/jogo/'
    #nomeJogoBusca = str(nomeJogo).replace(' ','-')
    #urlBuscaPagina = urlBusca+nomeJogoBusca
    urlBuscaPagina = linkJogo
    r = request(urlBuscaPagina)
    columnsDF=["id",
            "jogoAno",
            "jogoIdade",
            "jogoTempJogo",
            "jogoQtJogadores",
            "jogoMiolosDesigner",
            "jogoMiolosArtista",
            "jogoMiolosEditora",
            "jogoStatTem",
            "jogoStatQuer",
            "jogoStatTeve",
            "jogoStatFavorito",
            "jogoResumoTexto"]
    #dfJogo = pd.DataFrame(columns=columnsDF,index=range(1))

    soup = BeautifulSoup(r.text, 'lxml')
    
    detalhes = soup.find_all("div", attrs={'class':'jogo-top-main'})
    jogoAnoFull = detalhes[0].find_all("span", attrs={'class':'text-xs'}) 
    
    jogoAno = jogoAnoFull[0].string.replace('(','').replace(')','')
    
    jogoDetalhesFull = detalhes[0].find_all("ul", attrs={'class':'list-inline'})
    jogoDetalhesLista = jogoDetalhesFull[0].find_all("li")
    jogoIdade = jogoDetalhesLista[0].text
    jogoTempJogo = jogoDetalhesLista[1].text
    jogoQtJogadores = jogoDetalhesLista[2].text

    jogoMiolos = detalhes[0].find_all("span", attrs={'class':'info-span text-sm'}) 
    jogoMiolosDesigner = jogoMiolos[0].find_next("a").text
    jogoMiolosArtista = jogoMiolos[1].find_next("a").text
    jogoMiolosEditora = jogoMiolos[2].find_next("a").text

    jogoStatsPossuem =  detalhes[0].find_all("button")
    for jogoStat in jogoStatsPossuem:
        if jogoStat.attrs.get("data-tipo") == "fl_tem":
            sTemp = jogoStat.string
            jogoStatTem = sTemp[sTemp.find('(')+1:sTemp.find(')')]
        if jogoStat.attrs.get("data-tipo") == "fl_quer":
            sTemp = jogoStat.string
            jogoStatQuer = sTemp[sTemp.find('(')+1:sTemp.find(')')]
        if jogoStat.attrs.get("data-tipo") == "fl_teve":
            sTemp = jogoStat.string
            jogoStatTeve = sTemp[sTemp.find('(')+1:sTemp.find(')')]
        if jogoStat.attrs.get("data-tipo") == "fl_favorito":
            sTemp = jogoStat.string
            jogoStatFavorito = sTemp[sTemp.find('(')+1:sTemp.find(')')]
    
    jogoResumo = soup.find_all("div", attrs={'class':'bloco-sm-content bloco-sm-content-open'})
    jogoResumoTexto = jogoResumo[0].text.replace("\n","").replace("\t",'').replace("\r",'')

    tempDataframe = pd.DataFrame([[idJogo,
                            jogoAno,
                            jogoIdade,
                            jogoTempJogo,
                            jogoQtJogadores,
                            jogoMiolosDesigner,
                            jogoMiolosArtista,
                            jogoMiolosEditora,
                            jogoStatTem,
                            jogoStatQuer,
                            jogoStatTeve,
                            jogoStatFavorito,
                            jogoResumoTexto]],columns=columnsDF)
    #dfJogo.iloc[1, :] = tempDataframe
    print(tempDataframe) 
    return tempDataframe


#----------------- lendo os jogos baixados
file = '003-storage/000-transient/ludopedia_listaJogos.csv'
csvDetalheJogos = '003-storage/000-transient/ludopedia_DetalhesJogos.csv'

df = pd.read_csv(file,sep=';',quoting=csv.QUOTE_NONNUMERIC)
linkJogo = df['url']
print('DF size :'+str(df.size))
print('DF shape :'+str(df.shape))

dfJogoAll = pd.DataFrame(columns=["id",
                            "jogoAno",
                            "jogoIdade",
                            "jogoTempJogo",
                            "jogoQtJogadores",
                            "jogoMiolosDesigner",
                            "jogoMiolosArtista",
                            "jogoMiolosEditora",
                            "jogoStatTem",
                            "jogoStatQuer",
                            "jogoStatTeve",
                            "jogoStatFavorito",
                            "jogoResumoTexto"])

#for idJogo in  idsJogos:
for i in range(len(df)):
    dfJogo = getDadosJogo(linkJogo[i],i+1)
    dfJogoAll = pd.concat([dfJogoAll,dfJogo],axis=0)
    if i == 0:
        #criando o arquivo inicial
        # com o header
        dfJogo.to_csv(csvDetalheJogos, sep=';',quoting=csv.QUOTE_NONNUMERIC)
    else:
        dfJogo.to_csv(csvDetalheJogos,mode='a', header=False, sep=';',quoting=csv.QUOTE_NONNUMERIC)

    
    