deque = []
limite = 6  # limite visual do histórico

def inserir_fim(valor):
    """Adiciona comando ao fim do histórico"""
    if len(deque) >= limite:
        removido = deque.pop(0)  # remove o mais antigo automaticamente
        print(f"Histórico cheio. Comando mais antigo removido: {removido}")
    deque.append(valor)
    print(f"Comando adicionado: {valor}. Histórico atual: {deque}")

def remover_frente():
    """Remove o comando mais antigo do histórico"""
    if len(deque) > 0:
        removido = deque.pop(0)
        print(f"Comando mais antigo removido: {removido}. Histórico atual: {deque}")
        return removido
    else:
        print("Erro: Histórico vazio! Nada para remover.")
        return None

# --- Bloco de Interação com o Usuário ---
print("--- Simulador de Histórico de Comandos ---")
while True:
    print("\n1: Adicionar Comando | 2: Remover Comando Mais Antigo | 3: Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        item = input("Digite o comando: ")
        inserir_fim(item)
    elif opcao == '2':
        remover_frente()
    elif opcao == '3':
        print("Encerrando o simulador.")
        break
    else:
        print("Opção inválida.")