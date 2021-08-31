from os import system


# ------------------------------------------------------------------------------------------------------------------------------------------
# Classe que constroi a arvore minima

class ArvoreMinima:

    def __init__(self):
        self.nos = 0
        self.buff = []

    def adiciona_no(self, vertice, peso):
        self.buff.append([vertice, peso])
        self.nos += 1

        noFilho = self.nos

        while True:
            if noFilho == 1:
                break
            noPai = noFilho // 2
            if self.buff[noPai - 1][0] <= self.buff[noFilho - 1][0]:
                break
            else:
                self.buff[noPai - 1], self.buff[noFilho - 1] = self.buff[noFilho -
                                                                         1], self.buff[noPai - 1]
                noFilho = noPai

    def remove_no(self):
        primeiroElemento = self.buff[0]
        self.buff[0] = self.buff[self.nos - 1]

        self.buff.pop()
        self.nos -= 1

        noPai = 1
        while True:
            noFilho = 2 * noPai          # Filho a esquerda
            if noFilho > self.nos:
                break
            if noFilho + 1 <= self.nos:  # Filho a direita
                if self.buff[noFilho][0] < self.buff[noFilho - 1][0]:
                    noFilho += 1
            if self.buff[noPai - 1][0] <= self.buff[noFilho - 1][0]:
                break
            else:
                self.buff[noPai - 1], self.buff[noFilho - 1] = self.buff[noFilho -
                                                                         1], self.buff[noPai - 1]
                noPai = noFilho

        return primeiroElemento

    def mostra_no(self):
        print(self.buff)

    def tamanho_buff(self):
        return self.nos


# ------------------------------------------------------------------------------------------------------------------------------------------
# Classe que constroi o grafo por matriz de adjacencia


class GrafoMatriz:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[None] * self.vertices for i in range(self.vertices)]

    def add_aresta(self, vertice1, vertice2, peso):
        self.grafo[vertice1 - 1][vertice2 - 1] = peso
        self.grafo[vertice2 - 1][vertice1 - 1] = peso

    def print_matriz_adjacencia(self):
        contador1, contador2 = 1, 1

        print("Matriz de Adjacencia:\n")
        for i in range(self.vertices):
            if i == 0:
                while contador1 <= self.vertices:
                    print(f"\t{contador1}", end="")
                    contador1 += 1
            for j in range(self.vertices):
                if j == 0:
                    print(f"\n{contador2}", end="")
                    contador2 += 1
                print(f"\t{self.grafo[i][j]}", end="")
            print()

    def dijkstra(self, origem):
        caminhoMinimo = [["Origem", "Infinito"] for _ in range(self.vertices)]
        caminhoMinimo[origem - 1] = [origem, 0]

        lista = ArvoreMinima()
        lista.adiciona_no(origem, 0)

        while lista.tamanho_buff() > 0:
            vertice, peso = lista.remove_no()
            for i in range(self.vertices):
                if self.grafo[vertice - 1][i] != None:
                    if caminhoMinimo[i][1] == "Infinito" or caminhoMinimo[i][1] > peso + self.grafo[vertice - 1][i]:
                        caminhoMinimo[i] = [
                            vertice, peso + self.grafo[vertice - 1][i]]
                        lista.adiciona_no(
                            i + 1, peso + self.grafo[vertice - 1][i])

        return caminhoMinimo


# ------------------------------------------------------------------------------------------------------------------------------------------
# Função que pausa o sistema


def pause():
    getc = input("\n[ Aperte qualquer botao para continuar ]\n")
# ------------------------------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------------------------------
def main():

    num_de_vertices = 0
    while(num_de_vertices <= 0 or num_de_vertices > 20):
        num_de_vertices = int(
            input("Digite um numero válido de vértices(1-20): "))
        print()

    meuGrafo = GrafoMatriz(num_de_vertices)

    escolha = 0

    while(True):
        system("clear" or "cls")
        print("\t [Menu Principal]")
        print("1. Inserir as arestas e seus respectivos pesos")
        print("2. Imprimir o menor caminho entre os vertices")
        print("3. Imprimir a matriz de adjacencia")
        print("4. Sair")
        escolha = int(input("Opcao: "))

        if escolha == 1:
            system("clear" or "cls")

            vertice1 = int(
                input(f"Qual o ponto de partida?(1 - {num_de_vertices})\nR: "))
            while(vertice1 < 1 or vertice1 > num_de_vertices):
                print("\n\t [ Valor invalido - Tente Novamente ]")
                vertice1 = int(
                    input(f"\nQual o ponto de partida?(1 - {num_de_vertices})\nR: "))

            vertice2 = int(
                input(f"\nQual o ponto de chegada?(1 - {num_de_vertices})\nR: "))
            while(vertice2 < 1 or vertice2 > num_de_vertices or vertice2 == vertice1):
                print("\n\t [ Valor invalido - Tente Novamente ]")
                vertice2 = int(
                    input(f"\nQual o ponto de chegada?(1 - {num_de_vertices})\nR: "))

            peso = int(input("\nQual o peso da aresta?\nR: "))

            meuGrafo.add_aresta(vertice1, vertice2, peso)
        elif escolha == 2:
            system("clear" or "cls")
            meuGrafo.print_matriz_adjacencia()

            origem = int(input("\nDigite a origem: "))
            while origem < 1 or origem > num_de_vertices:
                print("\n\t [ Valor invalido - Tente Novamente ]")
                origem = int(input("\nDigite a origem: "))

            destino = int(input("\nDigite o destino: "))
            while destino < 1 or destino > num_de_vertices:
                print("\n\t [ Valor invalido - Tente Novamente ]")
                destino = int(input("\nDigite o destino: "))

            resultado = meuGrafo.dijkstra(origem)
            print(
                f"\nCaminho Minimo da Origem ate o Destino: {resultado[destino - 1]}")

            print(f"\nCaminho Minimo da Origem a todos os Destinos: ", end="")
            for i in resultado:
                print(i, end=" ")

            pause()
        elif escolha == 3:
            system("clear" or "cls")
            meuGrafo.print_matriz_adjacencia()
            pause()
        elif escolha == 4:
            system("clear" or "cls")
            break
        else:
            print("\t [Tente Novamente]")
            pause()


main()
# ------------------------------------------------------------------------------------------------------------------------------------------
