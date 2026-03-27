# Implemente uma LDE. Clientes normais entram na Cauda. Clientes prioritários devem ser inseridos na Cabeça. 
# Implemente a remoção tanto da cabeça quanto da cauda.

class NodeDE:
    def __init__(self, elemento):
        self.elemento = elemento
        self.proximo = None
        self.anterior = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    def desenhar_estado(self, acao):
        print(f"\n{'='*60}")
        print(f"AÇÃO: {acao}")
        print(f"{'='*60}")

        if self.tamanho == 0:
            print("ESTADO: [ Vazia ]")
            print("CABEÇA -> NULO | CAUDA -> NULO")
            return

        print(f"CONTROLE: Cabeça=[{self.cabeca.elemento}] | Cauda=[{self.cauda.elemento}] | Total={self.tamanho}")

        atual = self.cabeca
        visual = "NULO <-"
        while atual:
            visual += f" [ {atual.elemento} ] "
            if atual.proximo:
                visual += "<->"
            else:
                visual += "-> NULO"
            atual = atual.proximo
        print(visual)

    def inserir_cabeca(self, valor):
        novo = NodeDE(valor)
        if self.tamanho == 0:
            self.cabeca = self.cauda = novo
        else:
            novo.proximo = self.cabeca
            self.cabeca.anterior = novo
            self.cabeca = novo
        self.tamanho += 1
        self.desenhar_estado(f"INSERIR {valor} NA CABEÇA (Prioritário)")

    def inserir_cauda(self, valor):
        novo = NodeDE(valor)
        if self.tamanho == 0:
            self.cabeca = self.cauda = novo
        else:
            self.cauda.proximo = novo
            novo.anterior = self.cauda
            self.cauda = novo
        self.tamanho += 1
        self.desenhar_estado(f"INSERIR {valor} NA CAUDA (Normal)")

    def remover_cabeca(self):
        if self.tamanho == 0:
            print("\nERRO: Lista vazia!")
            return
        removido = self.cabeca.elemento
        if self.tamanho == 1:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.proximo
            self.cabeca.anterior = None
        self.tamanho -= 1
        self.desenhar_estado(f"ATENDER {removido} NA CABEÇA")

    def remover_cauda(self):
        if self.tamanho == 0:
            print("\nERRO: Lista vazia!")
            return
        removido = self.cauda.elemento
        if self.tamanho == 1:
            self.cabeca = self.cauda = None
        else:
            self.cauda = self.cauda.anterior
            self.cauda.proximo = None
        self.tamanho -= 1
        self.desenhar_estado(f"ATENDER {removido} NA CAUDA")

    def mostrar_fila(self):
        if self.tamanho == 0:
            print("Fila vazia.")
            return
        atual = self.cabeca
        fila = []
        while atual:
            fila.append(atual.elemento)
            atual = atual.proximo
        print("Fila atual:", " -> ".join(fila))

# --- Interface de Interação ---
lde = ListaDuplamenteEncadeada()
print("SIMULADOR DE FILA DE CLIENTES (LDE) - Prof. Calvetti")

while True:
    print("\nOPÇÕES: 1: +Prioritário | 2: +Normal | 3: -Atender Cabeça | 4: -Atender Cauda | 5: Mostrar Fila | 6: Sair")
    op = input("Escolha: ")

    if op == '1':
        lde.inserir_cabeca(input("Nome do cliente prioritário: "))
    elif op == '2':
        lde.inserir_cauda(input("Nome do cliente normal: "))
    elif op == '3':
        lde.remover_cabeca()
    elif op == '4':
        lde.remover_cauda()
    elif op == '5':
        lde.mostrar_fila()
    elif op == '6':
        print("Finalizando...")
        break
    else:
        print("Opção inválida.")
