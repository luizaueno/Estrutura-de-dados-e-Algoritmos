# Implemente o Selection Sort. O algoritmo deve localizar o menor elemento do vetor e trocá-lo com o elemento da posição atual de análise, repetindo o processo para todo o conjunto.

def select(vetor):
    for pos_atual in range(len(vetor)):
        indice_min = pos_atual
        for indice in range(pos_atual+1, len(vetor)):
            if vetor[indice] < vetor[indice_min]:
                indice_min = indice
        aux = vetor[indice_min]
        vetor[indice_min] = vetor[pos_atual]
        vetor[pos_atual] = aux
    return vetor



entrada = input("Digite os valores das densidades separadas por espaço: ")
vetor = [int (x) for x in entrada.split()]
print(f"Valores de entrada {entrada}")
select(vetor)
print(f"Vetor ordenado {vetor}")