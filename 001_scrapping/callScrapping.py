import ludopediaListaJogos
import ludopediaDetalhes
import bggListaJogos
import bggDetalhes



print("--------------------------------------------")
print("Iniciando processo de extração dos jogos")
print("--------------------------------------------")
print("Extraindo listagem dos jogos do BGG")
bggListaJogos.geraListaJogos()
print("--------------------------------------------")
print("Extraindo detalhes dos Jogos do BGG")
bggDetalhes.geraDetalheJogos()
print("--------------------------------------------")
print("Extraindo listagem dos jogos da Ludopedia")
ludopediaListaJogos.geraListaJogos()
print("--------------------------------------------")
print("Extraindo detalhes dos Jogos do BGG")
ludopediaDetalhes.geraDetalheJogos()
print("--------------------------------------------")
print("Final do processo de extração dos jogos")
print("--------------------------------------------")