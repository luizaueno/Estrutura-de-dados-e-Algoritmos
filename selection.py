
# Utilize o algoritmo Selection Sort para ordenar a lista de pontuações. O algoritmo deve buscar o maior elemento e colocá-lo na primeira posição, repetindo o processo para os demais.

def select(vetor):
    for pos_atual in range(len(vetor)):
        indice_min = pos_atual
        for indice in range(pos_atual +1, len(vetor)):
            if vetor[indice] < vetor[indice_min]:
                indice_min = indice
                aux = vetor[indice_min]
                vetor[indice_min] = vetor[pos_atual]
                vetor[pos_atual] = aux
    return vetor

entrada = input("Digite os valores separados por espaço: ")
vetor = [int(x) for x in entrada.split()]
print(f"Valores de entrada {entrada}")
select(vetor)
print(f"Vetor ordenado {vetor}")

def select(vetor):
    for posicao_atual in range(len(vetor)):
        indice_min = posicao_atual
        for indice in range(posicao_atual+1, len(vetor)):
            if vetor[indice] < vetor[indice_min]:
                indice_min = indice
            aux = vetor[indice_min]
            vetor[indice_min] = vetor[posicao_atual]
            vetor[posicao_atual] = aux

    return vetor


entrada = input("Digite os IDs separados por espaço: ")
vetor = [int (x) for x in entrada.split()]
print(f"Vetor original: {entrada}")
select(vetor)
print(f"Horários ordenados {vetor}")

