def produto(lista:list, esq:int, dir:int):
    if(esq == dir):
        return lista[esq]
    else:
        return lista[esq]*produto(lista, esq+1, dir)
    
teste1 = [3,4,4]
print(produto(teste1, 0, len(teste1)-1))