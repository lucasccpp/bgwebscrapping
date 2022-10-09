import csv
import time
import xml.etree.ElementTree as etree
from time import sleep

import pandas as pd
import requests
from bs4 import BeautifulSoup

def getDadosJogo(idJogo,slp=2):
    columnsDF=["bg_id",
            "bg_desc",
            "bg_name",
            "bg_year",
            "bg_max_player",
            "bg_min_player",
            "bg_temp",
            "bg_temp_min",
            "bg_temp_max",
            "bg_idade",
            "bg_categoria",
            "bg_mecanica",
            "bg_designer",
            "bg_Artist",
            "bg_Editora",
            "bg_num_ratings",
            "bg_avg_rating",
            "bg_num_owning",
            "bg_num_trading",
            "bg_num_wanting",
            "bg_num_wishing",
            "bg_num_weights",
            "bg_avg_weight"]

    url = 'https://www.boardgamegeek.com/xmlapi2/'
    typeSearch = 'thing?'
    idSearch = 'id='+str(idJogo)
    statsSearch = 'stats=1'
    urlSearch = url+typeSearch+idSearch+'&'+statsSearch
    sleep(slp)
    r = requests.get(urlSearch)
    root = etree.fromstring(r.text)
    bg_id = idJogo
    for item_root in root:
        bg_id = int(item_root.get("id"))
        bg_desc = item_root.find("description").text
        names = item_root.findall("name")
        for name in names:
            if name.get("type") == "primary":
                bg_name = name.get("value")
        bg_year = int(item_root.find("yearpublished").get("value"))
        bg_max_player = int(item_root.find("maxplayers").get("value"))
        bg_min_player = int(item_root.find("minplayers").get("value"))
        bg_temp = int(item_root.find("playingtime").get("value"))
        bg_temp_min = int(item_root.find("minplaytime").get("value"))
        bg_temp_max = int(item_root.find("maxplaytime").get("value"))
        bg_idade = int(item_root.find("minage").get("value"))
        #bg categoria é uma lista
        links_list = item_root.findall("link")
        bg_categorialist = []
        for link in links_list:
            if link.get("type") == "boardgamecategory":
                bg_categoriaitem = link.get("value")
                bg_categorialist.append(bg_categoriaitem)
        bg_categoria = bg_categorialist

        bg_mecanicalist = []
        for link in links_list:
            if link.get("type") == "boardgamemechanic":
                bg_mecanicaItem = link.get("value")
                bg_mecanicalist.append(bg_mecanicaItem)
        bg_mecanica = bg_mecanicalist

        bg_designerlist = []
        for link in links_list:
            if link.get("type") == "boardgamedesigner":
                bg_designerItem = link.get("value")
                bg_designerlist.append(bg_designerItem)
        bg_designer = bg_designerlist

        bg_Artistlist = []
        for link in links_list:
            if link.get("type") == "boardgameartist":
                bg_ArtistItem = link.get("value")
                bg_Artistlist.append(bg_ArtistItem)
        bg_Artist = bg_Artistlist

        bg_Editoralist = []
        for link in links_list:
            if link.get("type") == "boardgamepublisher":
                bg_EditoraItem = link.get("value")
                bg_Editoralist.append(bg_EditoraItem)
        bg_Editora = bg_Editoralist

        #statisticas
        bg_statsAll = item_root.find("statistics").find("ratings")
        bg_num_ratings = int(bg_statsAll.find("usersrated").get("value"))
        bg_avg_rating = float(bg_statsAll.find("average").get("value"))
        bg_num_owning = int(bg_statsAll.find("owned").get("value"))
        bg_num_trading = int(bg_statsAll.find("trading").get("value"))
        bg_num_wanting = int(bg_statsAll.find("wanting").get("value"))
        bg_num_wishing = int(bg_statsAll.find("wishing").get("value"))
        bg_num_weights = int(bg_statsAll.find("numweights").get("value"))
        bg_avg_weight = float(bg_statsAll.find("averageweight").get("value"))

    tempDataFrame = pd.DataFrame([[bg_id,
                                bg_desc,
                                bg_name,
                                bg_year,
                                bg_max_player,
                                bg_min_player,
                                bg_temp,
                                bg_temp_min,
                                bg_temp_max,
                                bg_idade,
                                bg_categoria,
                                bg_mecanica,
                                bg_designer,
                                bg_Artist,
                                bg_Editora,
                                bg_num_ratings,
                                bg_avg_rating,
                                bg_num_owning,
                                bg_num_trading,
                                bg_num_wanting,
                                bg_num_wishing,
                                bg_num_weights,
                                bg_avg_weight]],columns=columnsDF)

    #print(bg_name)
    return tempDataFrame




file = '003-storage/000-transient/bgg_gamelist.csv'
csvDetalheJogos = '003-storage/000-transient/bgg_DetalhesJogos.csv'

df = pd.read_csv(file)
idsJogos = df['id']
print(df.size)
print('DF size :'+str(df.size))
print('DF shape :'+str(df.shape))

dfJogoAll = pd.DataFrame(columns=["bg_id",
                                    "bg_desc",
                                    "bg_name",
                                    "bg_year",
                                    "bg_max_player",
                                    "bg_min_player",
                                    "bg_temp",
                                    "bg_temp_min",
                                    "bg_temp_max",
                                    "bg_idade",
                                    "bg_categoria"
                                    "bg_mecanica",
                                    "bg_designer",
                                    "bg_Artist",
                                    "bg_Editora",
                                    "bg_num_ratings",
                                    "bg_avg_rating",
                                    "bg_num_owning",
                                    "bg_num_trading",
                                    "bg_num_wanting",
                                    "bg_num_wishing",
                                    "bg_num_weights",
                                    "bg_avg_weight"])

#for idJogo in  idsJogos:
#start = time.time()
#print("iniciando a extração {0}".format(start))
total = len(idsJogos)
for i in range(len(idsJogos)):
    dfJogo = getDadosJogo(idsJogos[i],2)
    print("extraindo {0} de {1} => {2}".format(str(i),str(total),dfJogo['bg_name'].values))
    dfJogoAll = pd.concat([dfJogoAll,dfJogo],axis=0)
    if i == 0:
        #criando o arquivo inicial
        # com o header
        dfJogo.to_csv(csvDetalheJogos, sep=';',quoting=csv.QUOTE_NONNUMERIC)
    else:
        dfJogo.to_csv(csvDetalheJogos,mode='a', header=False, sep=';',quoting=csv.QUOTE_NONNUMERIC)
#end = time.time()
#print("final da extração {0}".format(end))
#print("total de tempo em execução: {0}".format(str(end - start)))
