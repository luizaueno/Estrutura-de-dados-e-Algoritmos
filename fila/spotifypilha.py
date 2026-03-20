# Em players de música, um buƯer circular armazena "pacotes de áudio". Crie um sistema que simule esse buƯer com tamanho 6.
# O desafio aqui é implementar uma função extra chamada exibir_ordem_real(),
#que mostre os elementos na ordem em que serão processados (do Início ao Fim), independentemente de onde estejam fisicamente no vetor.

tamanho = 6
fila = [None] * tamanho
inicio = -1
fim = -1

def inserir(valor):
  global inicio, fim # deve alterar as variáveis

  if (fim + 1) % tamanho == inicio:
    print(f"ERRO: Fila cheia! Não é possível adicionar mais documentos")
  else:
    if inicio == -1:
      inicio = 0
    fim = (fim + 1) % tamanho
    fila[fim] = valor
    print(f"Inserido: {valor} na posição {fim}. Fila: {fila}")

def remover():
    global inicio, fim
    # Verifica se a fila está vazia (Underflow)
    if inicio == -1:
        print("ERRO: Fila Vazia! Nada para remover.")
        return None

    valor_removido = fila[inicio]
    fila[inicio] = None # Limpa a posição para visualização

    # Se havia apenas um elemento, a fila volta ao estado inicial
    if inicio == fim:
        inicio = -1
        fim = -1
    else:
        # Incremento circular do ponteiro início
        inicio = (inicio + 1) % tamanho

    print(f"Removido: {valor_removido}. Fila atual: {fila}")
    return valor_removido

def exibir_ordem_real():
  ordem = []
  global inicio, fim
    # Verifica se a fila está vazia (Underflow)
  if inicio == -1:
        print("ERRO: Fila Vazia! Nada para remover.")
        return None
  pos = inicio
  while pos !=fim:
    ordem.append(fila[pos])
    fila[pos]
    pos = (pos + 1) % tamanho
  ordem.append(fila[fim]) 
  fila[fim]
  print("Ordem real de processamento:", ordem)
      


# --- Bloco de Interação com o Usuário ---
print(f"--- Simulador de Fila Circular (Tamanho: {tamanho}) ---")
while True:
    print("\n1: Inserir (FIFO) | 2: Remover | 3: Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        item = input("Digite os valores, separados por espaço para inserir na fila: ")
        for item in item.split():
          inserir(item)
    elif opcao == '2':
        remover()
    elif opcao == '3':
        print("Encerrando o simulador.")
        break
    else:
        print("Opção inválida.")
