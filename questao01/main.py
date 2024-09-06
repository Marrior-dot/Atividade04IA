from random import randint
import array

class rainha():
    def __init__(self, linha:int, coluna:int):
        self.linha = linha
        self.coluna = coluna    
    
    def __str__(self) -> str:
        return f"{self.linha}, {self.coluna}"

def stochasticHillClimbing(lista:list):
    for position in range(len(lista)):
        listaVizinhos = lista.copy()
        posicaoAtual = rainha(position, lista[position])
        #del listaVizinhos[position]
        listaVizinhos[position] = None
        print(posicaoAtual)
        print(listaVizinhos)
        print(checarCusto(posicaoAtual, listaVizinhos))
        print("---------------------------------------------------")

        #for vizinho in range(len(listaVizinhos)):
        #    if(checarCusto(rainha(vizinho, listaVizinhos[vizinho]), lista) <= checarCusto(posicaoAtual, lista)):
        #        posicaoVizinhoAleatorio = randint(0, len(listaVizinhos)-1)
        #        vizinhoAleatorio = rainha(posicaoVizinhoAleatorio, listaVizinhos[posicaoVizinhoAleatorio])


        #while checarCustoVizinhos(listacopy, lista[position]):
        #    posicaVizinho = randint(0, len(listacopy)-1)
        #    vizinho = listacopy[posicaVizinho]
        #    if posicaVizinho <= position:
        #        lista[position] = vizinho
        #        tabuleiro[position][posicaVizinho] = 1
        #        break
def checarCusto(posicaoRainha:rainha,lista:list):
    pares = 0
    
    for i in range(0,len(lista),1):
        #Checar na horizontal
        if posicaoRainha.coluna == lista[i] and lista[i] != None:
            pares += 1
        #Checar na vertical
        if posicaoRainha.linha == i and lista[i] != None:
            pares += 1
        #Checar na diagonal da esquerda para a direita
        
    
    
    #Checar na diagonal
    return pares


    
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