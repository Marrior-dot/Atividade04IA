import random

def gerar_individuo():
    individuo = []
    for i in range(8):
        individuo.append(random.randint(0,7))
    return individuo 

def ocorreu_colisao(individuo, i, j):
    # colisao linear
    if (individuo[i] == individuo[j]):
        return True
    # colisoes diagonais
    if (individuo[i] + (j-i) == individuo[j]):
        return True
    if (individuo[j] + (j-i) == individuo[i]):
        return True
    return False

def calcular_aptidao(individuo):
    aptidao = 28
    for i in range(len(individuo)):
        for j in range(i+1,len(individuo)):
            if(ocorreu_colisao(individuo, i,j)):
                aptidao -=1 
    return aptidao

def printar_tabuleiro(individuo):
    tabuleiro = '''   _______________
0 |_|_|_|_|_|_|_|_|
1 |_|_|_|_|_|_|_|_|
2 |_|_|_|_|_|_|_|_|
3 |_|_|_|_|_|_|_|_|
4 |_|_|_|_|_|_|_|_|
5 |_|_|_|_|_|_|_|_|
6 |_|_|_|_|_|_|_|_|
7 |_|_|_|_|_|_|_|_|
   0 1 2 3 4 5 6 7'''
    tabuleiro = [*tabuleiro]
    for i in range(8):
        numero_do_individuo = individuo[i]
        pos = i*2 + numero_do_individuo*20 + 22
        tabuleiro[pos] = "#"
    print(''.join(tabuleiro))


def stochastic_hill_climbing():
    individuo = gerar_individuo()
    aptidao = calcular_aptidao(individuo)
    print(individuo, aptidao)
    printar_tabuleiro(individuo)

    qtd_maxima_falhas = 500
    falhas = 0
    while falhas <= qtd_maxima_falhas and aptidao < 28:
        novo_individuo = [*individuo]

        index_selecionado = random.randint(0,7)
        linha_selecionada = random.randint(0,7)
        novo_individuo[index_selecionado] = linha_selecionada
        
        nova_aptidao = calcular_aptidao(novo_individuo)

        if aptidao < nova_aptidao:
            falhas = 0
            individuo = novo_individuo
            aptidao = nova_aptidao
        else:
            falhas += 1
    
    return individuo, aptidao


individuo, aptidao = stochastic_hill_climbing()
print("O individuo é "+str(individuo))
print("A aptidao é "+str(aptidao))
printar_tabuleiro(individuo)

