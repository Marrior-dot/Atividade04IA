from random import randint
import array

def stochasticHillClimbing(lista:list):
    for position in range(len(lista)):
        listacopy = lista.copy()
        posicaoAtual = lista[position]
        del listacopy[position]
        
        for vizinho in listacopy:
            

        #while checarCustoVizinhos(listacopy, lista[position]):
        #    posicaVizinho = randint(0, len(listacopy)-1)
        #    vizinho = listacopy[posicaVizinho]
        #    if posicaVizinho <= position:
        #        lista[position] = vizinho
        #        tabuleiro[position][posicaVizinho] = 1
        #        break

#def checarCustoVizinhos(lista:list, posicaoAtual: int):
#    for vizinho in lista:
#        if posicaoAtual > vizinho:
#            return False
#    return True
def checarCustoVizinhos(lista:list, posicaoAtual: int):
    paresElemento1 = 0
    paresElemento2 = 0
def gerarLista():
    lista = []
    for i in range(0,8,1):
        lista.append(randint(0, 7))
    return lista

def gerarTabuleiro(lista:list):
    tabuleiro = [[],[],[],[],[],[],[],[]]
    for i in range(0,len(lista),1):
        for j in range(0,len(lista),1):
            if j == lista[i]:
                tabuleiro[i].append(1)
            else:
                tabuleiro[i].append(0)
    return tabuleiro

lista = gerarLista()
tabuleiro = gerarTabuleiro(lista)
stochasticHillClimbing(lista)
for i in tabuleiro:
    print(f"{i}\n")