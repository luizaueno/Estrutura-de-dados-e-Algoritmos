#  Crie uma LSE onde cada nó é o nome de uma música.
# O usuário pode adicionar músicas ao final da lista.
# Implemente uma função exibir_playlist que percorre a lista da cabeça até o NULO.

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

    def inserir_cauda(self, valor):
       
        novo = NodeSE(valor)
        if self.Tamanho == 0:
            self.Inicio = self.Fim = novo
        else:
            # A atual cauda passa a apontar para o novo nó
            self.Fim.proximo = novo
            # A referência de fim da lista muda para o novo nó 
            self.Fim = novo
        self.Tamanho += 1
        print(f"\n(+) INSERIDO {valor} NA CAUDA")
        self.desenhar_lista()

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


# --- Menu de Interação ---
lse = ListaSE_Interativa()
while True:
    print("\n1: Inserir Música | 2: Exibir Playlist | 3: Sair")
    op = input("Escolha uma opção: ")

    if op == '1':
        lse.inserir_cauda(input("Música: "))
    elif op == '2':
        lse.remover_cabeca()
    elif op == '3':
        print("Finalizando simulador.")
        break