def reverter(lista:list, novaLista:list = []):
    if len(lista) == 0:
        return novaLista
    novaLista.append(lista[-1])
    return reverter(lista[:-1], novaLista)

def modulo():
    var1 = [1,4,10,23,2222]
    var2 = [1,12,10,50,22]

    #Teste 1
    print(reverter(var1,[]))
    #Teste 2
    print(reverter(var2,[]))

modulo()