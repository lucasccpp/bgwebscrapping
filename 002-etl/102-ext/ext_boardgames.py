import time
import shutil

path_transient = '003-storage/000-transient/'
path_raw = '003-storage/001-raw/'
path_raw_ver = '003-storage/001-raw/001-history/'
file_bgg_list = 'bgg_gamelist.csv'
file_bgg_detalhe = 'bgg_DetalhesJogos.csv' 
file_ludop_list = 'ludopedia_listaJogos.csv'
file_ludop_detalhe = 'ludopedia_DetalhesJogos.csv'

sAnoMesDia = time.strftime("%Y%m%d_%H%M")+'_'
print("Processando e armazenando como dia {0}".format(sAnoMesDia))
print("Inicio da copia dos arquivos e versionamento")
shutil.copy(path_transient+file_bgg_list, path_raw+file_bgg_list)
shutil.copy(path_raw+file_bgg_list, path_raw_ver+sAnoMesDia+file_bgg_list)

shutil.copy(path_transient+file_bgg_detalhe, path_raw+file_bgg_detalhe)
shutil.copy(path_raw+file_bgg_detalhe, path_raw_ver+sAnoMesDia+file_bgg_detalhe)

shutil.copy(path_transient+file_ludop_list, path_raw+file_ludop_list)
shutil.copy(path_raw+file_ludop_list, path_raw_ver+sAnoMesDia+file_ludop_list)

shutil.copy(path_transient+file_ludop_detalhe, path_raw+file_ludop_detalhe)
shutil.copy(path_raw+file_ludop_detalhe, path_raw_ver+sAnoMesDia+file_ludop_detalhe)
print("Final da copia dos arquivos e versionamento")