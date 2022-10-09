import pandas as pd

path_raw = '003-storage/001-raw/'
file_raw_list = 'bgg_gamelist.csv'
file_raw_detalhe = 'bgg_DetalhesJogos.csv'

dfTempList = pd.read_csv(path_raw+file_raw_list,sep=',')
dfTempList.rename(columns={"id":"bg_id", "nrate":"bg_nrate","pic_url":"bg_pic_url"}, inplace = True)
dfTempDetail = pd.read_csv(path_raw+file_raw_detalhe,sep=';')

dfJoin = pd.merge(dfTempList,dfTempDetail,on=["bg_id"])
dfJoin['bg_rank_pos'] = dfJoin.index+1

qtLinhasDFJoin=dfJoin.shape[0]

dfBGG = pd.DataFrame(columns=["bg_id"
                            "bg_desc"
                            "bg_name"
                            "bg_year"
                            "bg_max_player"
                            "bg_min_player"
                            "bg_temp"
                            "bg_temp_min"
                            "bg_temp_max"
                            "bg_idade"
                            "bg_categoria"
                            "bg_mecanica"
                            "bg_designer"
                            "bg_Artist"
                            "bg_Editora"
                            "bg_num_ratings"
                            "bg_avg_rating"
                            "bg_num_owning"
                            "bg_num_trading"
                            "bg_num_wanting"
                            "bg_num_wishing"
                            "bg_num_weights"
                            "bg_avg_weight"
                            "bg_nrate"
                            "bg_pic_url"
                            "bg_rank_pos"])
dfBGGAll = dfBGG.copy()
for index,row in dfJoin.iterrows():
    #for row.col
    dfBGG['bg_rank_pos'] = int(index)
    
