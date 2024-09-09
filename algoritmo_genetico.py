import random
import math
import time
import statistics

def somar_bin(a, b):
    # Considerando a e b de tamanho maximo de 3 bits
    # Resultando em um número maximo de 4 bits
    a = ['0', *a]
    b = ['0', *b]
    x = '0'
    binario = ['0', '0', '0', '0']
    for i in range(3, -1, -1):
        if (a[i] == '1' and b[i] == '1'):
            binario[i] = x
            x = '1'
        elif (a[i] == '0' and b[i] == '0'):
            binario[i] = x
            x = '0'
        else:
            if (x == '1'):
                binario[i] = '0'
                x = '1'
            else:
                binario[i] = '1'
                x = '0'
    return ''.join(binario)


# Função para converter um número inteiro em binário
def int_para_bin(val):
    # Considerando 0 <= val < 8
    binario = ['0', '0', '0']
    for i in range(2, -1, -1):
        binario[i] = str(val % 2)
        val = math.floor(val / 2)
    return ''.join(binario)


# Função para converter um número binário em inteiro
def bin_para_int(binario):
    # Binario sendo representado em string
    val = 0
    for i in range(len(binario)):
        if (binario[i] == '1'):
            val += 2**(len(binario) - i - 1)
    return val


def gerar_bin(n=3):
    return ''.join([str(random.randint(0, 1)) for i in range(n)])


# Função que gera a população inicial para o problema
def inicializar_populacao():
    P = []
    # Gerar populacao inicial de tamanho 20
    for i in range(20):
        P_index = []
        for j in range(8):
            # Escolha de numeros aleatorios
            # Representados como binario na lista de populacao
            P_index.append(gerar_bin())
        P.append(P_index)
    return P


# Função que verifica se duas rainhas estão na mesma diagonal
def existe_diagonal_entre(posicoes, i, j):
    aux = int_para_bin(j - i)
    diagonal_superior = somar_bin(posicoes[i], aux)
    diagonal_inferior = somar_bin(posicoes[j], aux)
    if (diagonal_superior[0] != '0'):
        return False
    if (diagonal_superior[1:] == posicoes[j]):
        return True

    if (diagonal_inferior[0] != '0'):
        return False
    if (diagonal_inferior[1:] == posicoes[i]):
        return True
    return False


# Função que calcula o fitness de cada indivíduo da população
def calcular_fitness(P):
    FP = []
    for item in P:
        aptidao = 28
        for i in range(8):
            for j in range(i + 1, 8):
                if (item[i] == item[j]):
                    aptidao -= 1
                if (existe_diagonal_entre(item, i, j)):
                    aptidao -= 1
        FP.append(aptidao)
    return FP


# Função que seleciona um pai
def selecionar_pais(FP):
    porcentagem = []
    soma = 0
    # Calculando a porcentagem de cada individuo para usar na roleta
    for item in FP:
        soma += item
    for item in FP:
        porcentagem.append((item / soma) * 100)

    # Construindo a roleta cumulativa
    roleta = []
    soma_acumulada = 0
    for perc in porcentagem:
        soma_acumulada += perc
        roleta.append(soma_acumulada)

    # Girando a roleta: gerando número aleatório entre 0 e 100
    valor_aleatorio = random.uniform(0, 100)
    # Selecionando o pai
    for i, valor_roleta in enumerate(roleta):
        if valor_aleatorio <= valor_roleta:
            return i


# Função para selecionar 9 pares de pais
def selecionar_pares_pais(P, FP, num_pares=9):
    pais_selecionados = []
    for _ in range(num_pares):
        pai1 = selecionar_pais(FP)
        pai2 = selecionar_pais(FP)
        pais_selecionados.append((P[pai1], P[pai2]))
    return pais_selecionados


# Função que faz o processo de cruzamento
def cruzar(pares_pais):
    taxa_cruzamento = 0.8
    filhos = []
    for pai1, pai2 in pares_pais:
        if random.random() <= taxa_cruzamento:
            ponto_corte = 4  # Ponto de corte de valor 4
            filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
            filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
            filhos.append(filho1)
            filhos.append(filho2)
        else:
            filhos.append(pai1)
            filhos.append(pai2)
    return filhos


# Função que faz o processo de mutação
def mutacao(filhos):
    taxa_mutacao = 0.03
    P_mutada = []  # Lista para armazenar os indivíduos após mutação
    for individuo in filhos:
        individuo_mutado = []  # Lista para armazenar o indivíduo mutado
        for gene in individuo:
            if random.random() <= taxa_mutacao:
                # Seleciona um índice aleatório para inverter um bit
                posicao_bit = random.randint(0, len(gene) - 1)
                gene_mutado = list(gene)
                # Inverte o bit na posição selecionada
                gene_mutado[posicao_bit] = '1' if gene_mutado[
                    posicao_bit] == '0' else '0'
                # Reconstrói o gene mutado como uma string
                individuo_mutado.append(''.join(gene_mutado))
            else:
                # Se não for mutado, mantém o gene original
                individuo_mutado.append(gene)
        P_mutada.append(
            individuo_mutado
        )  # Adiciona o indivíduo mutado à lista de população mutada
    return P_mutada


# Função que faz o processo de selecionar os melhores indivíduos
def selecionar_sobreviventes(P, FP, P3, FP3):
    # Selecionar dois mais aptos do grupo original (P, FP)
    maiores = [0, 1]
    for i in range(2, len(FP)):
        if (FP[i] > FP[maiores[0]] and FP[i] < FP[maiores[1]]):
            maiores[0] = maiores[1]
            maiores[1] = i
        elif (FP[i] > FP[maiores[1]] and FP[i] < FP[maiores[0]]):
            maiores[1] = i
        elif (FP[i] > FP[maiores[0]] and FP[i] > FP[maiores[1]]):
            maiores[0] = i
            if (FP[maiores[0]] > FP[maiores[1]]):
                maiores[1] = maiores[0]

    P = [P[maiores[0]], P[maiores[1]]]
    FP = [FP[maiores[0]], FP[maiores[1]]]

    P.extend(P3)
    FP.extend(FP3)

    return P, FP


# Função que retorna a melhor solução encontrada ou a primeira encontrada entre as melhores
def melhor_solucao(P):
    FP = calcular_fitness(P)
    maior = 0
    for i in range(1, len(FP)):
        if FP[maior] < FP[i]:
            maior = i
    return P[maior], FP[maior]


# Função que verifica se uma solução ótima foi encontrada
def solucao_otima_atingida(FP):
    for aptidao in FP:
        if aptidao == 28:
            return True

    return False

# Função que mostra como o indivíduo está representado no tabuleiro de xadrez, ou seja, como as rainhas estão posicionadas no tabuleiro 
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
        numero_do_individuo = bin_para_int(individuo[i])
        pos = i * 2 + numero_do_individuo * 20 + 22
        tabuleiro[pos] = "#"
    print(''.join(tabuleiro))


# Função que executa o algoritmo genético 50 vezes
def executar_50_vezes():
    iteracoes_necessarias = []
    tempos_execucao = []
    melhores_solucoes = []

    for _ in range(50):
        inicio = time.time()

        # Executa o algoritmo genético
        P, FP, geracoes = algoritmo_genetico()

        fim = time.time()

        # Armazenando o tempo de execução e o número de iterações
        iteracoes_necessarias.append(geracoes)
        tempos_execucao.append(fim - inicio)

        # Armazenando a melhor solução encontrada
        melhores_solucoes.append((P, FP))

    # Cálculo da média e desvio padrão
    media_iteracoes = statistics.mean(iteracoes_necessarias)
    desvio_padrao_iteracoes = statistics.stdev(iteracoes_necessarias)

    media_tempo = statistics.mean(tempos_execucao)
    desvio_padrao_tempo = statistics.stdev(tempos_execucao)

    print('Apos executar o algoritmo 50 vezes, temos como resultado:')
    print(25*'-')
    print(f"Média de iterações: {media_iteracoes}")
    print(f"Desvio padrão de iterações: {desvio_padrao_iteracoes}")
    print(f"Média de tempo de execução: {media_tempo:.5f} segundos")
    print(f"Desvio padrão do tempo de execução: {desvio_padrao_tempo:.5f} segundos")

    # Mostrar as cinco melhores soluções
    melhores_solucoes.sort(key=lambda x: x[1], reverse=True)  # Ordenar pela aptidão (FP)
    print("\nCinco melhores soluções:")
    for i, (solucao, aptidao) in enumerate(melhores_solucoes[:5], start=1):
        
        sol, ff = melhores_solucoes[i - 1]
        print('-------------------------')
        print(f"Solução {i}: Individuo: {sol} | Aptidão = {aptidao}")
        printar_tabuleiro(solucao)


# Função principal do algoritmo genético
def algoritmo_genetico():
    P = inicializar_populacao()
    FP = calcular_fitness(P)
    geracao = 1
    while (geracao <= 1000 and not solucao_otima_atingida(FP)):
        P1 = selecionar_pares_pais(P, FP)
        P2 = cruzar(P1)
        P3 = mutacao(P2)
        FP3 = calcular_fitness(P3)
        P, FP = selecionar_sobreviventes(P, FP, P3, FP3)
        geracao += 1
    melhor_P, melhor_FP = melhor_solucao(P)
    return melhor_P, melhor_FP, geracao


# Execução do algoritmo genético
executar_50_vezes()
