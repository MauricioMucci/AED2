from os import system

# ------------------------------------------------------------------------------------------------------------------------------------------
# Classe que constroi o grafo por matriz de adjacencia


class GrafoMatriz:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[None] * self.vertices for i in range(self.vertices)]

    def add_aresta(self, vertice1, vertice2, peso):
        self.grafo[vertice1-1][vertice2-1] = peso
        self.grafo[vertice2-1][vertice1-1] = peso

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


# ------------------------------------------------------------------------------------------------------------------------------------------

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
        print("2. Imprimir matriz de adjacencia")
        print("3. Sair")
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

            pause()
        elif escolha == 3:
            system("clear" or "cls")
            break
        else:
            print("\t [Tente Novamente]")


main()
# ------------------------------------------------------------------------------------------------------------------------------------------
