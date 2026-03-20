# Desenvolva um script que armazene palavras
# digitadas pelo usuário. Caso o usuário digite o comando "undo", o programa deve
# remover a última palavra inserida, simulando a função de desfazer (Ctrl+Z).

pilha = []

def empilhar(valor):
  """Adiciona um elemento ao topo da pilha (Push)"""
  pilha.append(valor)
  print(f"Elemento {valor} empilhado. Pilha atual: {pilha}")

def desempilhar():
    """Remove o elemento do topo da pilha (Pop)"""
    if len(pilha) > 0: # Verifica se a pilha não está vazia (Underflow)
        removido = pilha.pop()
        print(f"Elemento {removido} removido. Pilha atual: {pilha}")
        return removido
    else:
        print("Erro: A pilha está vazia!")
        return None


print("--- Simulador do botão desfazer ---")
while True:
    print("\n1: Adicionar palavras | undo: apagar | 3: Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        itens = input("Digite os números dos pacotes separados por espaço: ")
        for item in itens.split():
          empilhar(item)
    elif opcao == 'undo':
        desempilhar()
    elif opcao == '3':
        print("Encerrando simulador.")
        break
    else:
        print("Opção inválida.")