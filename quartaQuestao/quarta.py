def produto(lista:list, esq:int, dir:int):
    return lista[esq] if esq == dir else lista[esq]*produto(lista, esq+1, dir)

varExemplo1 = [1,2,3]
varExemplo2 = [2,5,1,2,3]

def modulo():
    #Teste1
    print(produto(varExemplo1, 0, len(varExemplo1)-1))
    #Teste2
    print(produto(varExemplo2, 0, len(varExemplo2)-1))

modulo()