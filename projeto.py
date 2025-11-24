# -*- coding: utf-8 -*-
"""
"""
from grafoMatriz import GrafoRot
import api_igdb

def main():
    grafo = GrafoRot(1)
    terminar = False

    print("**** Recomendação de Jogos com Grafos ****")
    try:
        grafo.makeGraphFromFile("grafo.txt")
        print("grafo.txt carregado com sucesso.\n")
    except Exception:
        print("Opção 0 para ler ou construa manualmente.\n")

    while not terminar:
        print("LudoRadar - Menu de Opções:")
        print("0: Ler dados do arquivo grafo.txt")
        print("1: Gravar dados no arquivo grafo.txt")
        print("2: Inserir vértice")
        print("3: Inserir aresta")
        print("4: Remover vértice")
        print("5: Remover aresta")
        print("6: Mostrar conteúdo do arquivo")
        print("7: Mostrar grafo")
        print("8: Apresentar conexidade do grafo")
        print("9: Montar árvore geradora máxima do grafo")
        print("10: Mostrar todos os caminhos mínimos do grafo")
        print("11: Verificar se o grafo é euleriano")
        print("12: Recomendar jogos com base em um jogo específico")
        print("13: Encerrar o programa")

        try:
            inp = int(input("Escolha uma opção: ").strip())
        except ValueError:
            print("Opção inválida.\n")
            continue

        match inp:
            case 0:
                try:
                    grafo.makeGraphFromFile("grafo.txt")
                    print("grafo.txt carregado com sucesso.\n")
                except Exception:
                    print("Opção 0 para ler ou construa manualmente.\n")

            case 1:
                grafo.makeFileFromGraph("grafo.txt")
                print("grafo gravado em grafo.txt.\n")

            case 2:
                try:
                    peso = int(input("Insira a nota do jogo (peso do vértice): ").strip())
                    rotulo = input("Insira o nome do jogo (rótulo do vértice): ").strip()
                    grafo.insereV(peso, rotulo)
                    print("vértice inserido.\n")
                except ValueError:
                    print("Entrada inválida.\n")

            case 3:
                try:
                    jogo1 = int(input("Insira o primeiro vértice: ").strip())
                    jogo2 = int(input("Insira o segundo vértice: ").strip())
                    peso = int(input("Insira o peso da aresta: ").strip())
                    grafo.insereA(jogo1, jogo2, peso)
                    print("aresta inserida.\n")
                except ValueError:
                    print("Entrada inválida.\n")

            case 4:
                try:
                    jogo = int(input("Insira o índice do vértice a remover: ").strip())
                    grafo.removeV(jogo)
                    print("vértice removido.\n")
                except ValueError:
                    print("Entrada inválida.\n")

            case 5:
                try:
                    jogo1 = int(input("Insira o primeiro vértice: ").strip())
                    jogo2 = int(input("Insira o segundo vértice: ").strip())
                    grafo.removeA(jogo1, jogo2)
                    print("aresta removida.\n")
                except ValueError:
                    print("Entrada inválida.\n")

            case 6:
                try:
                    with open("grafo.txt", "r", encoding="utf-8") as f:
                        print("\n--- Conteúdo de grafo.txt ---")
                        for line in f:
                            print(line.rstrip("\n"))
                        print("--- fim ---\n")
                except FileNotFoundError:
                    print("Arquivo grafo.txt não encontrado.\n")

            case 7:
                try:
                    modo = int(input("Qual modo do grafo deseja (0 - Completo, 1 - Simples): ").strip())
                except ValueError:
                    print("Entrada inválida.\n")
                    continue

                if modo == 0:
                    grafo.show()
                else:
                    grafo.showMin()
                print()

            case 8:
                print("Conexidade do grafo: ", end="")
                if grafo.eConexo() == 1:
                    print("Desconexo")
                else:
                    print("Conexo")

            case 9:
                agm = grafo.prim()
                print("Custo máximo: ", agm[0])
                grafo2 = GrafoRot(grafo.vertices)
                for i in agm[1]:
                    grafo2.insereA(i[0], i[1], i[2])
                grafo2.show(omitir_infinito=True)

            case 10:
                grafo.Floyd()

            case 11:
                if grafo.caminhoEuleriano():
                    print("O grafo é euleriano.")
                else:
                    print("O grafo não é euleriano.")

            case 12:
                print("Insira o nome do jogo para recomendação:")
                nome_jogo = input().lower()
                for i in grafo.rot:
                    jogo = i[0].lower()
                    for simb in [".", ",", ":", ";", "!", "?", "\"", "'", " ", "-", "_"]:
                        jogo = jogo.replace(simb, "")
                        nome_jogo = nome_jogo.replace(simb, "")
                    if nome_jogo == jogo:
                        indice_jogo = grafo.rot.index(i)
                        #print(indice_jogo)
                        print(f"Recomendações para '{i[0]}':")
                        for v in range(grafo.vertices):
                            if grafo.adj[indice_jogo][v] >= 5 and indice_jogo != v:
                                print(f"- {grafo.rot[v][0]} (Peso da aresta: {grafo.adj[indice_jogo][v]})")
                        break
                
            case 13:
                terminar = True

            case _:
                print("Opção inexistente.\n")

    print("Fim")

if __name__ == "__main__":
    main()
