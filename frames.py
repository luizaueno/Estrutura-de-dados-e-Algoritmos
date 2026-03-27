#  Um software de edição envia frames para renderizar. Os frames entram pela Cauda.
# Implemente uma função que remova da Cabeça para processar, exibindo o ID do frame processado.

# Classe que representa a célula (nó)
class NodeSE:
    def __init__(self, elemento):
        self.elemento = elemento  # Conteúdo do nó
        self.proximo = None      # Ponteiro para o próximo nó (Next)

# Classe de controle da Lista Singularmente Encadeada [cite: 101]
class ListaSE_Interativa:
    def __init__(self):
        # A lista nasce vazia: Cabeça e Cauda apontam para NULO [cite: 108, 111, 112]
        self.Inicio = None
        self.Fim = None
        self.Tamanho = 0

    def desenhar_lista(self):
        """Exibe graficamente o estado dos nós e ponteiros [cite: 41, 44]"""
        if self.Tamanho == 0:
            print("\n[ESTADO ATUAL]: Lista Vazia (CABEÇA -> NULO <- CAUDA)")
            return

        print(f"\n--- CONFIGURAÇÃO DA LSE (Tamanho: {self.Tamanho}) ---")
        # Mostra as referências de controle da lista [cite: 27, 29, 32]
        print(f"PONTEIRO CABEÇA: [{self.Inicio.elemento}]")
        print(f"PONTEIRO CAUDA : [{self.Fim.elemento}]")

        atual = self.Inicio
        fluxo = "CABEÇA -> "
        while atual:
            # Representação visual da conexão entre os nós [cite: 191, 196]
            seta = " -> " if atual.proximo else " -> NULO (FIM)"
            fluxo += f"| {atual.elemento} |{seta}"
            atual = atual.proximo
        print(fluxo)
        print("-" * 45)


    def inserir_cauda(self, valor):
        """Inclusão na Cauda: Complexidade O(1) [cite: 87]"""
        novo = NodeSE(valor)
        if self.Tamanho == 0:
            self.Inicio = self.Fim = novo
        else:
            # A atual cauda passa a apontar para o novo nó [cite: 245, 291]
            self.Fim.proximo = novo
            # A referência de fim da lista muda para o novo nó [cite: 194, 245]
            self.Fim = novo
        self.Tamanho += 1
        print(f"\n(+) INSERIDO {valor} NA CAUDA")
        self.desenhar_lista()

    def remover_cabeca(self):
        """Remoção na Cabeça: Complexidade O(1) [cite: 90]"""
        if self.Tamanho == 0:
            print("\n[ERRO]: Underflow! Lista já está vazia.")
            return

        valor = self.Inicio.elemento
        # A cabeça pula para o próximo nó da corrente [cite: 553]
        self.Inicio = self.Inicio.proximo
        if self.Inicio is None:
            self.Fim = None

        self.Tamanho -= 1
        print(f"\n(-) REMOVIDO {valor} DA CABEÇA")
        self.desenhar_lista()

# --- Menu de Interação ---
lse = ListaSE_Interativa()
while True:
    print("\n1: Inserir Cauda | 2: Remover Cabeça | 3: Sair")
    op = input("Escolha uma opção: ")

    if op == '1':
        lse.inserir_cauda(int(input("ID: ")))
    elif op == '2':
        lse.remover_cabeca()
    elif op == '3':
        print("Finalizando simulador.")
        break