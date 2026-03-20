# Implemente um sistema que simule o botão "Voltar" de um navegador web. O usuário deve inserir as URLs visitadas
# e, ao selecionar a opção de retornar, o programa deve exibir a última URL visitada e removê-la da estrutura.
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


print("--- Simulador do botão voltar ---")
while True:
    print("\n1: Adicionar URL | 2: Retornar | 3: Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        itens = input("Digite os números dos pacotes separados por espaço: ")
        for item in itens.split():
          empilhar(item)
    elif opcao == '2':
        desempilhar()
    elif opcao == '3':
        print("Encerrando simulador.")
        break
    else:
        print("Opção inválida.")