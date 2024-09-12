def produtoLista(x:int, lista:list, esq:int, dir:int):
    if(esq == dir):
        return lista
    lista[esq] = lista[esq]*x
    return produtoLista(x, lista, esq + 1, dir)

def modulo():
    # teste 1
    teste1 = [2,1,4,2]
    print(f"Teste 1:{produtoLista(2,teste1, 0, len(teste1))}")

    # teste 2
    teste2 = [10,2,1,55,6,2]
    print(f"Teste 2:{produtoLista(10, teste2, 0, len(teste2))}")

modulo()
