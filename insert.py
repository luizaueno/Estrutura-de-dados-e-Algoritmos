
# Implemente o Insertion Sort. O algoritmo deve pegar cada elemento a partir do segundo e "empurrá-lo" para a esquerda até que ele encontre sua posição correta entre os elementos já processados.



def insert(vetor):
    for indice in range(len(vetor)):
        indice_atual = indice 
        while  (indice_atual > 0) and (vetor[indice_atual] < vetor[indice_atual -1]):

            if vetor[indice_atual] < vetor[indice_atual -1]:
                aux = vetor[indice_atual]
                vetor[indice_atual] = vetor[indice_atual -1]
                vetor[indice_atual -1] = aux

                indice_atual -=1


entrada = input("Digite os horários separados por espaço: ")
vetor = [int (x) for x in entrada.split()]
print(f"Vetor original: {entrada}")
insert(vetor)
print(f"Horários ordenados {vetor}")

