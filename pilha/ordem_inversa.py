pilha = []
pilha_inversa = []

def empilhar(valor):
  """Adiciona um elemento ao topo da pilha (Push)"""
  pilha.append(valor)
  print(f"Elemento {valor} empilhado. Pilha atual: {pilha}")


def inverter():
    """Remove o elemento do topo da pilha (Pop)"""
    if len(pilha) > 0: # Verifica se a pilha não está vazia (Underflow)
      while len(pilha) > 0:
          removido = pilha.pop()
          pilha_inversa.append(removido)

      print(f"Pilha inversa: {pilha_inversa}")
      return pilha_inversa

    else:
       print("Erro: A pilha está vazia!")
       return None


print("--- Inversão do pacote de dados] ---")
while True:
    print("\n 1: Adicionar pacotes | 2: Inverter | 3: Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        itens = input("Digite os números dos pacotes separados por espaço: ")
        for item in itens.split():
          empilhar(item)
    elif opcao == '2':
        inverter()
    elif opcao == '3':
        print("Encerrando simulador.")
        break
    else:
        print("Opção inválida.")