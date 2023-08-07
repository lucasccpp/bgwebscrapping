import time
import shutil
import os
#caminho_origem = 'C:\\caminho\\para\\arquivo_origem.txt'
#caminho_destino = 'C:\\caminho\\para\\destino\\arquivo_destino.txt'

path_transient = '\\003_storage\\000_transient\\'
path_raw       = '\\003_storage\\001_raw\\'
path_raw_ver   = '\\003_storage\\001_raw\\001_history\\'
file_bgg_list = 'bgg_gamelist.csv'
file_bgg_detalhe = 'bgg_DetalhesJogos.csv' 
file_ludop_list = 'ludopedia_listaJogos.csv'
file_ludop_detalhe = 'ludopedia_DetalhesJogos.csv'
#print(os.getcwd()+)
sAnoMesDia = time.strftime("%Y%m%d_%H%M")+'_'
print("Processando e armazenando como dia {0}".format(sAnoMesDia))
print("Inicio da copia dos arquivos e versionamento")
#print(path_transient+file_bgg_list)
shutil.copy(os.getcwd()+path_transient+file_bgg_list, os.getcwd()+path_raw+file_bgg_list)
shutil.copy(os.getcwd()+path_raw+file_bgg_list,       os.getcwd()+path_raw_ver+sAnoMesDia+file_bgg_list)

shutil.copy(os.getcwd()+path_transient+file_bgg_detalhe, os.getcwd()+path_raw+file_bgg_detalhe)
shutil.copy(os.getcwd()+path_raw+file_bgg_detalhe, os.getcwd()+path_raw_ver+sAnoMesDia+file_bgg_detalhe)

shutil.copy(os.getcwd()+path_transient+file_ludop_list, os.getcwd()+path_raw+file_ludop_list)
shutil.copy(os.getcwd()+path_raw+file_ludop_list, os.getcwd()+path_raw_ver+sAnoMesDia+file_ludop_list)

shutil.copy(os.getcwd()+path_transient+file_ludop_detalhe, os.getcwd()+path_raw+file_ludop_detalhe)
shutil.copy(os.getcwd()+path_raw+file_ludop_detalhe, os.getcwd()+path_raw_ver+sAnoMesDia+file_ludop_detalhe)
print("Final da copia dos arquivos e versionamento")