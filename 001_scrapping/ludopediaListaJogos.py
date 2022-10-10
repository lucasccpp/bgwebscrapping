from os import sep
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import csv

def request(msg, slp=5):
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

def geraListaJogos():

    df_all = pd.DataFrame(columns=["id",
                                    "gameRank",
                                    "gameName",
                                    "notaRank",
                                    "notaMedia",
                                    "qtNotas",
                                    "url"])
    #nome do arquivo
    fileNameListaJogos = "003_storage/000_transient/ludopedia_listaJogos.csv"

    urlBusca = 'https://www.ludopedia.com.br/ranking'
    paramRank = '?pagina='
    urlBuscaPagina = urlBusca+paramRank

    #pegar a ultima pagina
    getUltimaPagina = request(urlBusca)
    #soup = BeautifulSoup(getUltimaPagina.text, 'html.parser')
    soup = BeautifulSoup(getUltimaPagina.text,'lxml')
    paginacao = soup.find_all("a",
                            attrs={'title':'Última Página'})
    for pagina in paginacao:
        if pagina.attrs.get('title') == 'Última Página':
            ultimaPagina = str(pagina.attrs.get('href')).split(sep='=')[1]
            print(ultimaPagina)

    for i in range (int(ultimaPagina)):
        urlBuscaPaginaNum = urlBuscaPagina+str(i+1)
        r = request(urlBuscaPaginaNum)
        soup = BeautifulSoup(r.text, 'html.parser')

        table = soup.find_all("div",
                                attrs={'class':'pad-top'})
        print(len(table))
        df = pd.DataFrame(columns=["id",
                                    "gameRank",
                                    "gameName",
                                    "notaRank",
                                    "notaMedia",
                                    "qtNotas",
                                    "url"],
                                    index=range(len(table)))
        for idx, row in enumerate(table):
            itemJogo = row.find_all("h4",
                                attrs={'class':'media-heading'})[0]
            #for detJogo in itemJogo:
            rankJogo = itemJogo.find_next("span")
            #gameRank = ((i)*50) + idx
            gameRank = rankJogo.string
            link = itemJogo.find_next("a")
            gameLink = link["href"]
            gameName = link.string
            infosNotaJogo = row.find_all("div",
                                        attrs={"class": "rank-info"})[0]
            tiposNotas = infosNotaJogo.find_all("span")
            notaRank = float(tiposNotas[0].text.split(':')[1])
            notaMedia = float(tiposNotas[1].text.split(':')[1])
            qtNotas = int(tiposNotas[2].text.split(':')[1])
                
            print("{0} : {1}".format(gameName, gameLink))
            #TODO: SUBSTITUIR GAME RANK POR ID DO JOGO
            #df.iloc[idx, :] = [str(gameRank).replace('º',''),
            df.iloc[idx, :] = [str(gameRank).replace('º',''),
                                gameRank,
                                gameName,
                                notaRank,
                                notaMedia,
                                qtNotas, 
                                gameLink]
        df_all = pd.concat([df_all,df],axis=0) 
        if i == 0:
            #criando o arquivo inicial
            # com o header
            df.to_csv(fileNameListaJogos,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
        else:
            df.to_csv(fileNameListaJogos,mode='a', header=False,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)

    print(df_all.head())

#geraListaJogos()