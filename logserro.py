# Logs de erro são inseridos na Cabeça (para que o erro mais recente apareça primeiro).
# Implemente um código que permita inserir 5 logs e depois remova os 2 primeiros.

class NodeSE:
    def __init__(self, elemento):
        self.elemento = elemento
        self.proximo = None

class ListaSE_interativa:
    def __init__(self):
        self.Inicio = None
        self.Tamanho = 0

    def desenhar_lista(self):
        if self.Tamanho == 0:
            print("\n[LISTA VAZIA]")
            return
        
        # Percorre a lista para mostrar todos os logs
        atual = self.Inicio
        print(f"\n--- LOGS ATUAIS (Total: {self.Tamanho}) ---")
        while atual:
            print(f"[{atual.elemento}]", end=" -> ")
            atual = atual.proximo
        print("NULO")

    def inserir_cabeca(self, valor):
        novo = NodeSE(valor)
        # Se a lista não estiver vazia, o novo aponta para o antigo início
        if self.Tamanho > 0:
            novo.proximo = self.Inicio
        
        self.Inicio = novo
        self.Tamanho += 1
        print(f"(+) Inserido: {valor}")

    def remover_cabeca(self):
        if self.Tamanho == 0:
            print("[ERRO]: Lista vazia!")
            return
        
        valor_removido = self.Inicio.elemento
        self.Inicio = self.Inicio.proximo # A cabeça pula para o próximo
        self.Tamanho -= 1
        print(f"(-) Removido: {valor_removido}")

# --- TESTANDO O FLUXO ---
log_sistema = ListaSE_interativa()

# Inserindo 5 logs (um por um)
for i in range(1, 6):
    log_sistema.inserir_cabeca(f"Erro_0{i}")

log_sistema.desenhar_lista()

# Removendo os 2 primeiros (os mais recentes)
log_sistema.remover_cabeca()
log_sistema.remover_cabeca()

log_sistema.desenhar_lista()
