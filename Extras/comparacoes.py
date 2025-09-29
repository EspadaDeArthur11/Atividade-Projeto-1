import jogos as jogosPy
from grafoMatriz import GrafoRot as grafo

jogos = list(vars(jogosPy).items())
comparacoes = grafo(0)

for i in range(8, len(jogos)):
    comparacoes.insereV(jogos[i][1][1], jogos[i][1][0])

for i in range(8, len(jogos)):
    for j in range(8, i):
        peso = len(jogos[i][1][2] & jogos[j][1][2]) # soma 1 pra cada gênero em comum
        peso += len(jogos[i][1][3] & jogos[j][1][3]) # soma 1 pra cada tema em comum
        peso += len(jogos[i][1][4] & jogos[j][1][4]) # soma 1 pra cada qtde de jogador em comum
        comparacoes.insereA(i-8, j-8, peso)

comparacoes.makeFileFromGraph("grafo.txt")