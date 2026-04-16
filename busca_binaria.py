# Implemente um algoritmo de Busca Binária que receba a lista de códigos de barras (já ordenada) e o código desejado, retornando o número do compartimento ou uma mensagem de erro.

def busca_binaria(vetor, valor_procurado, inicio, fim):
    meio = (inicio + fim) //2
    if inicio > fim:
        return "ERRO! número do compartimento não encontrado"
    elif vetor[meio] == valor_procurado:
        return "Número do compartimento encontrado"
    if valor_procurado < vetor[meio]:
        return busca_binaria(vetor, valor_procurado, inicio, meio-1)
    return busca_binaria(vetor, valor_procurado, meio+1, fim)

entrada = input("Digite os números do compartimento separados por espaço: ")
vetor = [int (x) for x in entrada.split()]
if len(vetor)>= 1000:
    print("Limite excedido. Esse compartimento não existe")

valor_procurado =(int(input("Digite o número do compartimento procurado: ")))
vetor.sort()
resultado =  busca_binaria(vetor, valor_procurado, 0, len(vetor) -1)
print(resultado)