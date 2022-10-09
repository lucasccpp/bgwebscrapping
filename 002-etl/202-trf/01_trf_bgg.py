import pandas as pd
import csv

path_raw = '003-storage/001-raw/'
file_raw_list = 'bgg_gamelist.csv'
file_raw_detalhe = 'bgg_DetalhesJogos.csv'

path_curated = '003-storage/002-curated/'
file_curated_all = 'bgg_all.csv'

file_curated_DimCategoria = 'bgg_DimCategoria.csv'
file_curated_DimMecanica = 'bgg_DimMecanica.csv'
file_curated_DimArtista = 'bgg_DimArtista.csv'
file_curated_DimEditora = 'bgg_DimEditora.csv'
file_curated_DimDesigner = 'bgg_DimDesigner.csv'
file_curated_DimBoardgame = 'bgg_DimBoardgame.csv'
file_curated_FactBoardGameRelease = 'bgg_FactBoardGameRelease.csv'


dfTempList = pd.read_csv(path_raw+file_raw_list,sep=',')
dfTempList.rename(columns={"id":"bg_id", "nrate":"bg_nrate","pic_url":"bg_pic_url"}, inplace = True)
dfTempDetail = pd.read_csv(path_raw+file_raw_detalhe,sep=';')
print("unindo arquivos")
dfJoin = pd.merge(dfTempList,dfTempDetail,on=["bg_id"])
dfJoin['bg_rank_pos'] = dfJoin.index+1

print("tratamento de dimensoes")

#tratamento de categoria
dfDimCategoria = dfJoin[['bg_categoria']].copy()
dfDimCategoria['bg_categoria'].replace(regex=True,inplace=True, to_replace=r'[^0-9a-zA-Z, ]+', value=r'')
dfDimCategoria['bg_categoria'] = dfDimCategoria['bg_categoria'].str.split(',')
dfDimCategoria = dfDimCategoria.explode('bg_categoria')
dfDimCategoria['bg_categoria'] = dfDimCategoria['bg_categoria'].str.strip()
dfDimCategoria = dfDimCategoria.drop_duplicates()
dfDimCategoria = dfDimCategoria.reset_index()


#tratamento mecanica
#dfDimMecanica = dfJoin[['bg_mecanica']].drop_duplicates()
dfDimMecanica = dfJoin[['bg_mecanica']].copy()
dfDimMecanica['bg_mecanica'].replace(regex=True,inplace=True, to_replace=r'[^0-9a-zA-Z, ]+', value=r'')
dfDimMecanica['bg_mecanica'] = dfDimMecanica['bg_mecanica'].str.split(',')
dfDimMecanica = dfDimMecanica.explode('bg_mecanica')
dfDimMecanica['bg_mecanica'] = dfDimMecanica['bg_mecanica'].str.strip()
dfDimMecanica = dfDimMecanica.drop_duplicates()
dfDimMecanica = dfDimMecanica.reset_index()


#tratamento artista
#dfDimArtista = dfJoin[['bg_Artist']].drop_duplicates()
dfDimArtista = dfJoin[['bg_Artist']].copy()
dfDimArtista['bg_Artist'].replace(regex=True,inplace=True, to_replace=r'[^0-9a-zA-Z, ]+', value=r'')
dfDimArtista['bg_Artist'] = dfDimArtista['bg_Artist'].str.split(',')
dfDimArtista = dfDimArtista.explode('bg_Artist')
dfDimArtista['bg_Artist'] = dfDimArtista['bg_Artist'].str.strip()
dfDimArtista = dfDimArtista.drop_duplicates()
dfDimArtista = dfDimArtista.reset_index()

#tratamento editora
#dfDimEditora = dfJoin[['bg_Editora']].drop_duplicates()
dfDimEditora = dfJoin[['bg_Editora']].copy()
dfDimEditora['bg_Editora'].replace(regex=True,inplace=True, to_replace=r'[^0-9a-zA-Z, ]+', value=r'')
dfDimEditora['bg_Editora'] = dfDimEditora['bg_Editora'].str.split(',')
dfDimEditora = dfDimEditora.explode('bg_Editora')
dfDimEditora['bg_Editora'] = dfDimEditora['bg_Editora'].str.strip()
dfDimEditora = dfDimEditora.drop_duplicates()
dfDimEditora = dfDimEditora.reset_index()

#tratamento designer
#dfDimDesigner = dfJoin[['bg_designer']].drop_duplicates()
dfDimDesigner = dfJoin[['bg_designer']].copy()
dfDimDesigner['bg_designer'].replace(regex=True,inplace=True, to_replace=r'[^0-9a-zA-Z, ]+', value=r'')
dfDimDesigner['bg_designer'] = dfDimDesigner['bg_designer'].str.split(',')
dfDimDesigner = dfDimDesigner.explode('bg_designer')
dfDimDesigner['bg_designer'] = dfDimDesigner['bg_designer'].str.strip()
dfDimDesigner = dfDimDesigner.drop_duplicates()
dfDimDesigner = dfDimDesigner.reset_index()


dfDimBoardgame = dfJoin[["bg_id",
                        "bg_desc",
                        "bg_name",
                        "bg_year",
                        "bg_max_player",
                        "bg_min_player",
                        "bg_temp",
                        "bg_temp_min",
                        "bg_temp_max",
                        "bg_idade",
                        "bg_pic_url"]].drop_duplicates()


#tratamento fato
print("tratamento da fato")
dfFactBoardGameRelease = dfJoin


#exportar para csv CURADO
print("gravação no arquivo texto curated")
dfJoin.to_csv(path_curated+file_curated_all,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
dfDimCategoria.to_csv(path_curated+file_curated_DimCategoria,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
dfDimMecanica.to_csv(path_curated+file_curated_DimMecanica,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
dfDimArtista.to_csv(path_curated+file_curated_DimArtista,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
dfDimEditora.to_csv(path_curated+file_curated_DimEditora,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
dfDimDesigner.to_csv(path_curated+file_curated_DimDesigner,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
dfDimBoardgame.to_csv(path_curated+file_curated_DimBoardgame,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
dfFactBoardGameRelease.to_csv(path_curated+file_curated_FactBoardGameRelease,sep=';',index=False,quoting=csv.QUOTE_NONNUMERIC)   
