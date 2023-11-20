from sqlalchemy import create_engine
import pandas as pd
import sqlalchemy as sqlalchemy

path_database = '998-baseDados/databases/'
file_database = 'ludoDatabase.db'

path_curated = '003-storage/002-curated/'
file_curated_all = 'bgg_all.csv'

file_curated_DimCategoria = 'bgg_DimCategoria.csv'
file_curated_DimMecanica = 'bgg_DimMecanica.csv'
file_curated_DimArtista = 'bgg_DimArtista.csv'
file_curated_DimEditora = 'bgg_DimEditora.csv'
file_curated_DimDesigner = 'bgg_DimDesigner.csv'
file_curated_DimBoardgame = 'bgg_DimBoardgame.csv'
file_curated_FactBoardGameRelease = 'bgg_FactBoardGameRelease.csv'


engine = sqlalchemy.create_engine('sqlite:///'+path_database+file_database, echo=False)

dfDimCategoria = pd.read_csv(path_curated+file_curated_DimCategoria,sep=';')

dfDimCategoria['sk_categoria'] = dfDimCategoria.index
dfDimCategoria['pk_categoria'] = dfDimCategoria.index
dfDimCategoria.rename(columns={'bg_categoria':'s_nm_categoria'},inplace=True)


dfDimCategoria.to_sql('dim_categoria', con=engine, if_exists='append', index=False)

print("fim")