# -*- coding: utf-8 -*-
"""
"""
from grafoMatriz import GrafoRot


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
        print("Menu")
        print("0: Ler dados do arquivo grafo.txt")
        print("1: Gravar dados no arquivo grafo.txt")
        print("2: Inserir vértice")
        print("3: Inserir aresta")
        print("4: Remover vértice")
        print("5: Remover aresta")
        print("6: Mostrar conteúdo do arquivo")
        print("7: Mostrar grafo")
        print("8: Apresentar conexidade do grafo")
        print("9: Encerrar o programa")

        try:
            inp = int(input("Escolha uma opção: ").strip())
        except ValueError:
            print("Opção inválida.\n")
            continue

        match inp:
            case 0:
                try:
                    grafo.makeGraphFromFile("grafo.txt")
                    print("grafo.txt lido e grafo montado.\n")
                except FileNotFoundError:
                    print("Arquivo grafo.txt não encontrado.\n")

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
                terminar = True

            case _:
                print("Opção inexistente.\n")

    print("Fim")

if __name__ == "__main__":
    main()
