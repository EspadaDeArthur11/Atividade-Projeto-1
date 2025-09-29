# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023

@author: icalc
"""
INF = float("inf")

class GrafoRot:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n = TAM_MAX_DEFAULT):
        self.vertices = n # número de vértices
        self.arestas = 0 # número de arestas
        # matriz de adjacência
        self.adj = [[INF for i in range(n)] for j in range(n)]
        # lista de rótulos
        self.rot = [["", 0] for i in range(n)]

    # Insere um vértice no Grafo tal que
    # p é o peso no vértice e r é o rótulo do vértice
    def insereV(self, p, r):
        for i in range(self.vertices):
            # Adiciona o vértice em todas as linhas
            self.adj[i].append(INF)
        self.vertices += 1 # atualiza o número de vértices
        # Adiciona uma linha a mais
        self.adj.append([INF for i in range(self.vertices+1)])
        self.rot.append([r, p])

    # Remove um vértice v do grafo
    """ Explicação do algoritmo utilizado
    
      0 1 2
    0 A B C
    1 D E F
    2 G H I

    remover o 1:
    vértices removidos: B, D, E, F, H
      0 1 2
    0 A   C
    1 
    2 G   I
    (Espaços vazios para representar que seus valores não importam mais)

    movemos o G pra cima, o C pra esquerda e o I pra diagonal cima-esquerda na matriz
      0 1 2
    0 A C
    1 G I
    2

    fazemos o pop() para remover a linha/coluna 2
      0 1
    0 A C
    1 G I
    """
    # v é o índice do vértice que será removido
    def removeV(self, v):
        for i in range(self.vertices):
            if self.adj[v][i] != INF:
                self.arestas -= 1 # atualiza qtd arestas
        
        for i in range(self.vertices):
            if i != v:
                self.rot[i - (i > v)] = self.rot[i]
                for j in range(self.vertices):
                    # Copia os elementos para preencher as posições vagas do vértice removido na matriz
                    if j != v:
                        self.adj[i - (i > v)][j - (j > v)] = self.adj[i][j]

        # Atualiza o número de vértices, remove a última linha e as últimas posições de cada linha da matriz
        self.vertices -= 1
        self.adj.pop()
        self.rot.pop()
        for i in range(self.vertices):
            self.adj[i].pop()

	# Insere uma aresta no Grafo tal que
	# v é adjacente a w, com peso p
    def insereA(self, v, w, p):
        if self.adj[v][w] == INF:
            self.adj[v][w] = p
            self.adj[w][v] = p
            self.arestas += 1 # atualiza qtd arestas
    
    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        # testa se temos a aresta
        if self.adj[v][w] != INF:
            self.adj[v][w] = INF
            self.adj[w][v] = INF
            self.arestas -= 1 # atualiza qtd arestas

	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida	
    def show(self):
        print(f"\n n: {self.vertices:2d} ", end="")
        print(f"m: {self.arestas:2d}\n")

        for i in range(self.vertices):
            for w in range(self.vertices):
                if self.adj[i][w] == INF:
                    print(f"Adj[{i:2d},{w:2d}] = ∞ | ", end="") 
                else:
                    print(f"Adj[{i:2d},{w:2d}] = {self.adj[i][w]} | ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )


	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a matriz de adjacência obtida 
    # Apresentando apenas os valores 0 ou 1	
    def showMin(self):
        print(f"\n n: {self.vertices:2d} ", end="")
        print(f"m: {self.arestas:2d}\n")

        for i in range(self.vertices):
            for w in range(self.vertices):
                if self.adj[i][w] == INF:
                    print("∞ ", end="")
                else:
                    print(str(self.adj[i][w]) + " ", end="")
            print('\n')
        print("\nfim da impressao do grafo." )

    #### Métodos implementados para aula de Teoria dos Grafos

    # Retorna o grau do vértice v
    def degree(self, v):
        degree = 0
        for i in range(self.vertices):
            if self.adj[i][v] != INF:
                degree += 1
        return degree
    
    def makeFileFromGraph(self, arq):
        with open(arq, "w") as f:
            f.write(str(3) + "\n") # insere o tipo do grafo
            f.write(str(self.vertices) + "\n") # insere o núm de vértices
            for i in range(self.vertices): # insere os n vértices
                f.write(str(i) + " " + self.rot[i][0] + " " + str(self.rot[i][1]) + "\n")

            f.write(str(self.arestas) + "\n") # insere o núm de arestas
            for i in range(self.vertices): # insere todas as arestas caso existam
                for j in range(self.vertices):
                    if self.adj[i][j] != INF and i > j:
                        f.write(str(i) + " " + str(j) + " " + str(self.adj[i][j]) + "\n")

    # Lê um arquivo a e monta o grafo presente nele
    def makeGraphFromFile(self, arq):
        # abre o arquivo e o lê linha por linha
        with open(arq, "r") as f:

            # primeiro lemos as duas primeiras linhas para pegar o tipo e o número de vértices do grafo
            f.readline() # tipo (sempre será 3 nessa aplicação)
            line = f.readline() # número de vértices
            self.__init__(0) # inicia a matriz vazia para inserir os vértices depois

            for i in range(int(line)): # para as i linhas seguintes, insere os vértices
                line = f.readline().split() # [i, "rótulo", "peso"]
                rot = ""
                for i in range(len(line)-2):
                    rot += line[i+1] + " "
                rot = rot[:-1] # remove o espaço extra
                self.insereV(line[-1], rot)


            line = f.readline() # lê o número de arestas

            # Percorre o resto do arquivo, inserindo as arestas de cada par de vértices
            for i in range(int(line)):
                line = f.readline().split()
                v = int(line[0])
                w = int(line[1])
                p = int(line[2])
                self.insereA(v, w, p)

    # Verifica se o grafo é completo
    def isComplete(self):
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adj[i][j] == INF:
                    return 0 # Não é completo
        return 1 # É completo
    
    def Floyd(self):
        D = self.adj
        for i in range(self.vertices):
            D[i][i] = 0
        
        R = [[(j+1) for i in range(self.vertices)] for j in range(self.vertices)]
        for i in range(self.vertices):
            for j in range(self.vertices):
                if self.adj[i][j] < INF:
                    R[i][j] = (j+1)
                else:
                    R[i][j] = 0

        for k in range(self.vertices):
            for i in range(self.vertices):
                for j in range(self.vertices):
                    if i != j and D[i][k] + D[k][j] < D[i][j]:
                        D[i][j] = D[i][k] + D[k][j]
                        R[i][j] = R[i][k]
        
        print("D: ")
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(D[i][j], end=" ")
            print()

        print("R: ")
        for i in range(self.vertices):
            for j in range(self.vertices):
                print(R[i][j], end=" ")
            print()
    
    # Verifica se o gravo é conexo ou desconexo
    def eConexo(self):
        # Apenas precisamos ver se 1 vértice está conectado a todos os outros
        # Usamos o vértice 0 como inicial
        visitados = [0]

        for v in visitados:
            for i in range(self.vertices):
                if self.adj[v][i] != INF and i not in visitados:
                    visitados.append(i)
                        

        if len(visitados) != self.vertices:
            return 1
        return 0