import random
import numpy as np
import time

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
    
    return individuo, aptidao, falhas

def media_algoritmo():
    melhores_solucoes = []
    cinco_maiores = []
    media_falhas = []
    tempoExecucao = []
    for i in range(50):
        time_inicial = time.time()
        individuo, aptidao, falhas = stochastic_hill_climbing()
        time_final = time.time()
        tempoExecucao.append(time_final - time_inicial)
        media_falhas.append(falhas)
        melhores_solucoes. append((individuo,aptidao))

    media_falhas_media = np.mean(media_falhas)
    media_falhas_desvio_padrao = np.std(media_falhas)
    media_tempoExecucao = np.mean(tempoExecucao)
    desvio_padrao_tempoExecucao = np.std(tempoExecucao)
    print(f"Média de iterações: {media_falhas_media}")
    print(f"Desvio padrão de iterações: {media_falhas_desvio_padrao}")
    print(f"Média de tempo de execução: {media_tempoExecucao}")
    print(f"Desvio padrão de tempo de execução: {desvio_padrao_tempoExecucao}\n")

    cinco_maiores = sorted(melhores_solucoes, key=lambda x: x[1], reverse=True)[:5]
    for i in range(5):
        print(f"\nSolução {i+1}: Indivíduo: {cinco_maiores[i][0]} / Fitness: {cinco_maiores[i][1]}")
        printar_tabuleiro(cinco_maiores[i][0])

individuo = stochastic_hill_climbing()
media_algoritmo()


    
    