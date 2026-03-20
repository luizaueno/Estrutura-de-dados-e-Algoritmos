# Crie um Deque para gerenciar tarefas. Novas tarefas entram no fim da fila, mas se o gestor definir uma tarefa como
# "Crítica", ela deve entrar na frente. O desenvolvedor sempre remove para realizar a tarefa que estiver no topo (frente).

# Inicialização de um Deque vazio (sem limite de tamanho)
deque = []

def inserir_tarefas_criticas(valor):
    """Insere um elemento no início do Deque (índice 0)"""
    # O método insert(posicao, valor) desloca os demais elementos para a direita
    deque.insert(0, valor)
    print(f"Inserido na Frente: {valor}. Deque atual: {deque}")

def inserir_fim(valor):
    """Insere um elemento no final do Deque"""
    deque.append(valor)
    print(f"Inserido no Fim: {valor}. Deque atual: {deque}")

def remover_tarefas_criticas():
    """Remove o primeiro elemento do Deque"""
    if len(deque) > 0: # Verificação de Underflow
        removido = deque.pop(0)
        print(f"Removido da Frente: {removido}. Deque atual: {deque}")
        return removido
    else:
        print("Erro: Deque Vazio! Nada para remover na frente.")
        return None

def remover_fim():
    """Remove o último elemento do Deque"""
    if len(deque) > 0:
        removido = deque.pop() # Por padrão, pop() remove o último elemento
        print(f"Removido do Fim: {removido}. Deque atual: {deque}")
        return removido
    else:
        print("Erro: Deque Vazio! Nada para remover no fim.")
        return None

# --- Bloco de Interação com o Usuário ---
print("--- Simulador de lista de tarefas ---")
while True:
    print("\n1: Inserir Tarefas Críticas | 2: Inserir Tarefa Comum | 3: Remover Tarefas Críticas | 4: Remover Tarefa Comum| 5: Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        item = input("Insira tarefa crítica: ")
        inserir_tarefas_criticas(item)
    elif opcao == '2':
        item = input("Insira tarefa comum: ")
        inserir_fim(item)
    elif opcao == '3':
        remover_tarefas_criticas()
    elif opcao == '4':
        remover_fim()
    elif opcao == '5':
        print("Encerrando o simulador.")
        break
    else:
        print("Opção inválida.")