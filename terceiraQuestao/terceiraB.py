def produto(lista:list, esq:int, dir:int):
    if(esq == dir):
        return lista[esq]
    else:
        return lista[esq]*produto(lista, esq+1, dir)

def modulo():
    teste1 = [3,4,4]
    print(f"Produto: {produto(teste1, 0, len(teste1)-1)}")

    teste2 = [66,32,12,10,4]
    print(f"Produto: {produto(teste2, 0, len(teste2)-1)}")