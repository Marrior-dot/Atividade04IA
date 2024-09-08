from random import randint, choice
import array

class rainha():
    def __init__(self, linha:int, coluna:int):
        self.linha = linha
        self.coluna = coluna    
    
    def __str__(self) -> str:
        return f"{self.linha}, {self.coluna}"

def stochasticHillClimbing(lista:list):
    for position in range(len(lista)):
        custos = []
        #Lista para modificar as posições do vizinho e da posição atual
        listaVizinhosModificar = lista.copy()
        #Lista para procurar os vizinhos
        listaVizinhosProcurar = lista.copy()
        posicaoAtual = rainha(position, lista[position])
        #listaVizinhos[position] = None
        listaVizinhosModificar[position] = None
        del listaVizinhosProcurar[position]
        #print(posicaoAtual)
        #print(listaVizinhos)
        #print(checarCusto(posicaoAtual, listaVizinhos))
        #print("---------------------------------------------------")

        for vizinho in range(len(listaVizinhosProcurar)):
            #if listaVizinhos[vizinho] == None:
            #    continue
            #Escolhe de maneira aleatória uma coluna para o vizinho
            colunaVizinho = choice(listaVizinhosProcurar)
            #Usa o valor da coluna para conseguir o valor da linha do vizinho
            linhaVizinho = listaVizinhosModificar.index(colunaVizinho)     
            if(checarCusto(rainha(linhaVizinho, colunaVizinho), listaVizinhosModificar) <= checarCusto(posicaoAtual, listaVizinhosModificar)):
                #lista[]
                lista[position] = colunaVizinho
                posicaoAtual = rainha(position, colunaVizinho) #vizinhoAleatorio
                break

    tabuleiro = gerarTabuleiro(lista)

    for i in tabuleiro:
        print(f"{i}\n")
              
def checarCusto(posicaoRainha:rainha,lista:list):
    pares = 0
    jEsquerda = posicaoRainha.coluna
    jDireita = posicaoRainha.coluna
    #Checar na horizontal e na vertical
    for i in range(0,len(lista),1):
        #Checar na horizontal
        if posicaoRainha.coluna == lista[i] and lista[i] != None:
            pares += 1
        #Checar na vertical
        if posicaoRainha.linha == i and lista[i] != None:
            pares += 1

    #Checar na diagonal subindo
    for i in range(posicaoRainha.linha,0,-1):
        rDone = False
        lDone = False

        try:
            #Checar na diagonal subindo para a esquerda
            if lista[i] != None and lista[i] == jEsquerda:
                pares += 1
            #Checar na diagonal subindo para a direita
            if lista[i] != None and lista[i] == jDireita:
                pares += 1
        except IndexError:
            pass
        
        rDone = True if jDireita == len(lista) else False
        lDone = True if jEsquerda == 0 else False

        jEsquerda -= 1
        jDireita += 1
        if rDone and lDone:
            break
    
    jEsquerda = posicaoRainha.coluna
    jDireita = posicaoRainha.coluna


    for i in range(posicaoRainha.linha,len(lista)-1,1):
        rDone = False
        lDone = False

        try:
            if lista[i] != None and lista[i] == jEsquerda:
                pares += 1
            if lista[i] != None and lista[i] == jDireita:
                pares += 1
        except IndexError:
            pass
        
        rDone = True if jDireita == len(lista) else False
        lDone = True if jEsquerda == 0 else False

        jEsquerda -= 1
        jDireita += 1
        if rDone and lDone:
            break
    #Checar na diagonal descendo
    return pares

def compararCustos(listaVizinhos:list, posicaAtual:rainha, listaRainhas:list):
    for i in listaVizinhos:
        if checarCusto(posicaAtual, listaRainhas) < checarCusto(rainha(i, listaRainhas[i]), listaRainhas):
            return True
    return False


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
stochasticHillClimbing(lista)