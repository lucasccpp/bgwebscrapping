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


print(dfTempList.describe())

#teste
