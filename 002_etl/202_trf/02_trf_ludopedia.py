import pandas as pd
import csv

path_raw = '003_storage/001_raw/'
file_raw_list = 'ludopedia_listaJogos.csv'
file_raw_detalhe = 'ludopedia_DetalhesJogos.csv'

path_curated = '003_storage/002_curated/'
file_curated_all = 'ludopedia_all.csv'

file_curated_DimCategoria = 'ludopedia_DimCategoria.csv'
file_curated_DimMecanica = 'ludopedia_DimMecanica.csv'
file_curated_DimArtista = 'ludopedia_DimArtista.csv'
file_curated_DimEditora = 'ludopedia_DimEditora.csv'
file_curated_DimDesigner = 'ludopedia_DimDesigner.csv'
file_curated_DimBoardgame = 'ludopedia_DimBoardgame.csv'
file_curated_FactBoardGameRelease = 'ludopedia_FactBoardGameRelease.csv'


dfTempList = pd.read_csv(path_raw+file_raw_list,sep=';',header=0)
#dfTempList.rename(columns={"id":"bg_id", "nrate":"bg_nrate","pic_url":"bg_pic_url"}, inplace = True)
dfTempDetail = pd.read_csv(path_raw+file_raw_detalhe,sep=';',header=0)

print("unindo arquivos")
dfJoin = pd.merge(dfTempList,dfTempDetail,on=["id"])
dfJoin['bg_rank_pos'] = dfJoin['id']

print("tratamento de dimensoes")


#tratamento artista
#dfDimArtista = dfJoin[['bg_Artist']].drop_duplicates()
dfDimArtista = dfJoin[['jogoMiolosArtista']].copy()
#dfDimArtista['bg_Artist'].replace(regex=True,inplace=True, to_replace=r'[^0-9a-zA-Z, ]+', value=r'')
#dfDimArtista['jogoMiolosArtista'] = dfDimArtista['bg_Artist'].str.split(',')
#dfDimArtista = dfDimArtista.explode('bg_Artist')
dfDimArtista['jogoMiolosArtista'] = dfDimArtista['jogoMiolosArtista'].str.strip()
dfDimArtista = dfDimArtista.drop_duplicates()
dfDimArtista = dfDimArtista.reset_index()

#tratamento editora
#dfDimEditora = dfJoin[['bg_Editora']].drop_duplicates()
dfDimEditora = dfJoin[['jogoMiolosEditora']].copy()
#dfDimEditora['jogoMiolosEditora'].replace(regex=True,inplace=True, to_replace=r'[^0-9a-zA-Z, ]+', value=r'')
#dfDimEditora['jogoMiolosEditora'] = dfDimEditora['bg_Editora'].str.split(',')
#dfDimEditora = dfDimEditora.explode('bg_Editora')
dfDimEditora['jogoMiolosEditora'] = dfDimEditora['jogoMiolosEditora'].str.strip()
dfDimEditora = dfDimEditora.drop_duplicates()
dfDimEditora = dfDimEditora.reset_index()

#tratamento designer
#dfDimDesigner = dfJoin[['bg_designer']].drop_duplicates()
dfDimDesigner = dfJoin[['jogoMiolosDesigner']].copy()
#dfDimDesigner['bg_designer'].replace(regex=True,inplace=True, to_replace=r'[^0-9a-zA-Z, ]+', value=r'')
#dfDimDesigner['bg_designer'] = dfDimDesigner['bg_designer'].str.split(',')
#dfDimDesigner = dfDimDesigner.explode('bg_designer')
dfDimDesigner['jogoMiolosDesigner'] = dfDimDesigner['jogoMiolosDesigner'].str.strip()
dfDimDesigner = dfDimDesigner.drop_duplicates()
dfDimDesigner = dfDimDesigner.reset_index()

dfJoin['qt_jogadores_min'] = dfJoin['jogoQtJogadores'].str[0]
#necessario tratar o maximo de jogadores

dfDimBoardgame = dfJoin[["id",
                        "jogoResumoTexto",
                        "gameName",
                        "jogoAno",
                        "qt_jogadores_min",
                        "qt_jogadores_min",
                        "jogoTempJogo",
                        "jogoTempJogo",
                        "jogoTempJogo",
                        "jogoIdade",
                        "url"]].drop_duplicates()


#tratamento fato
print("tratamento da fato")
dfFactBoardGameRelease = dfJoin


#exportar para csv CURADO
print("gravação no arquivo texto curated")
dfJoin.to_csv(path_curated+file_curated_all,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
#dfDimCategoria.to_csv(path_curated+file_curated_DimCategoria,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
#dfDimMecanica.to_csv(path_curated+file_curated_DimMecanica,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
dfDimArtista.to_csv(path_curated+file_curated_DimArtista,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
dfDimEditora.to_csv(path_curated+file_curated_DimEditora,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
dfDimDesigner.to_csv(path_curated+file_curated_DimDesigner,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
dfDimBoardgame.to_csv(path_curated+file_curated_DimBoardgame,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
dfFactBoardGameRelease.to_csv(path_curated+file_curated_FactBoardGameRelease,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
