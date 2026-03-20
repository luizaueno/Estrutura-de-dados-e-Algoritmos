# Implemente um sistema que simule a abertura de abas. O usuário pode adicionar uma nova aba ao final da lista ou, se for
# uma aba de "emergência" (como um alerta de segurança), ela deve ser inserida no início. 
# Permita também fechar a aba mais recente ou a mais antiga.


# Configuração inicial do Deque Circular
TAMANHO = 6
deque = [None] * TAMANHO
frente = -1
tras = -1

def esta_cheia():
    # A fila está cheia se o próximo elemento após 'tras' for o 'frente'
    return (tras + 1) % TAMANHO == frente

def esta_vazia():
    # A fila está vazia se o ponteiro de frente for -1
    return frente == -1

def inserir_frente(valor):
    global frente, tras
    if esta_cheia():
        print(f"ERRO: Deque Cheio! Não foi possível inserir {valor} na frente.")
        return

    if esta_vazia():
        frente = tras = 0
    else:
        # Move o ponteiro para trás de forma circular
        frente = (frente - 1 + TAMANHO) % TAMANHO

    deque[frente] = valor
    print(f"Inserido na Frente: {valor}. Deque: {deque}")

def inserir_tras(valor):
    global frente, tras
    if esta_cheia():
        print(f"ERRO: Deque Cheio! Não foi possível inserir {valor} no fim.")
        return

    if esta_vazia():
        frente = tras = 0
    else:
        # Move o ponteiro para frente de forma circular
        tras = (tras + 1) % TAMANHO

    deque[tras] = valor
    print(f"Inserido no Fim: {valor}. Deque: {deque}")

def remover_frente():
    global frente, tras
    if esta_vazia():
        print("ERRO: Deque Vazio! Nada para remover na frente.")
        return None

    valor = deque[frente]
    deque[frente] = None # Limpeza visual

    if frente == tras: # Apenas um elemento
        frente = tras = -1
    else:
        frente = (frente + 1) % TAMANHO

    print(f"Removido da Frente: {valor}. Deque: {deque}")
    return valor

def remover_tras():
    global frente, tras
    if esta_vazia():
        print("ERRO: Deque Vazio! Nada para remover no fim.")
        return None

    valor = deque[tras]
    deque[tras] = None

    if frente == tras: # Apenas um elemento
        frente = tras = -1
    else:
        tras = (tras - 1 + TAMANHO) % TAMANHO

    print(f"Removido do Fim: {valor}. Deque: {deque}")
    return valor

# --- Menu Interativo ---
print(f"--- Simulador de Deque Circular (Tamanho: {TAMANHO}) ---")
while True:
    print("\n1: Inserir Frente | 2: Inserir Fim | 3: Remover Frente | 4: Remover Fim | 5: Sair")
    op = input("Escolha uma opção: ")

    if op == '1':
        inserir_frente(input("Aba: "))
    elif op == '2':
        inserir_tras(input("Aba: "))
    elif op == '3':
        remover_frente()
    elif op == '4':
        remover_tras()
    elif op == '5':
        break
    else:
        print("Opção inválida.")