deque = []

def inserir_frente(valor):
    """Reinsere dado crítico na frente do deque"""
    deque.insert(0, valor)
    print(f"Dado crítico reinserido na frente: {valor}. Cache atual: {deque}")

def inserir_fim(valor):
    """Insere novo dado no fim do deque"""
    deque.append(valor)
    print(f"Dado adicionado ao fim: {valor}. Cache atual: {deque}")

def remover_frente():
    """Remove o dado mais antigo (frente) para análise"""
    if len(deque) > 0:
        removido = deque.pop(0)
        print(f"Dado removido da frente para análise: {removido}. Cache atual: {deque}")
        return removido
    else:
        print("Erro: Cache vazio! Nada para remover na frente.")
        return None

def remover_fim():
    """Remove o dado mais recente (fim) para análise"""
    if len(deque) > 0:
        removido = deque.pop()
        print(f"Dado removido do fim para análise: {removido}. Cache atual: {deque}")
        return removido
    else:
        print("Erro: Cache vazio! Nada para remover no fim.")
        return None

# --- Bloco de Interação com o Usuário ---
print("--- Simulador de Cache com Deque ---")
while True:
    print("\n1: Reinserir Dado Crítico | 2: Adicionar Dado ao Fim | 3: Remover da Frente | 4: Remover do Fim | 5: Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        item = input("Digite o dado crítico: ")
        inserir_frente(item)
    elif opcao == '2':
        item = input("Digite o novo dado: ")
        inserir_fim(item)
    elif opcao == '3':
        remover_frente()
    elif opcao == '4':
        remover_fim()
    elif opcao == '5':
        print("Encerrando o simulador.")
        break
    else:
        print("Opção inválida.")
