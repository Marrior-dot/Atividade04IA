def ultimoDaLista(elemento:int):
    return [elemento]

def reverter(lista:list ,  novaLista:list):
    return novaLista if len(lista) == 0 else ultimoDaLista(lista[-1]) + reverter(lista[:-1], novaLista)

def modulo():
    #Teste1
    print(reverter([5,4,2,1], []))
    #Teste2
    print(reverter([2,15,621,41,22,1,10], []))