# Implemente o algoritmo Bubble Sort para ordenar um vetor de densidades. O código deve percorrer o vetor e realizar as trocas necessárias entre elementos vizinhos.

def bubble(vetor):
    for passagem in range(len(vetor)):
        for indice_atual in range(len(vetor)-1):
            if vetor[indice_atual] > vetor[indice_atual +1]:
                aux = vetor[indice_atual]
                vetor[indice_atual] = vetor[indice_atual +1]
                vetor[indice_atual +1] = aux


entrada = input("Digite os valores das densidades separadas por espaço: ")
vetor = [int (x) for x in entrada.split()]
print(f"Valores de entrada {entrada}")
bubble(vetor)
print(f"Vetor ordenado {vetor}")