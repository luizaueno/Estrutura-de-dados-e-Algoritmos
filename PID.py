# Implemente uma LSE onde cada nó representa um processo (PID). O usuário insere na cauda.
# Adicione uma função que conte quantos processos existem na lista sem usar um contador global (percorrendo a lista).


class NodeSE:
    def __init__(self, elemento):
        self.elemento = elemento  # Conteúdo do nó (PID do processo)
        self.proximo = None       # Ponteiro para o próximo nó

class ListaSE_Interativa:
    def __init__(self):
        self.Inicio = None
        self.Fim = None
        self.Tamanho = 0

    def desenhar_lista(self):
        """Exibe graficamente o estado dos nós e ponteiros"""
        if self.Tamanho == 0:
            print("\n[ESTADO ATUAL]: Lista Vazia")
            return

        print(f"\n--- CONFIGURAÇÃO DA LSE (Tamanho via contador: {self.Tamanho}) ---")
        atual = self.Inicio
        fluxo = "CABEÇA -> "
        while atual:
            seta = " -> " if atual.proximo else " -> NULO (FIM)"
            fluxo += f"| PID: {atual.elemento} |{seta}"
            atual = atual.proximo
        print(fluxo)

    def inserir_cauda(self, valor):
        """Inclusão na Cauda: O novo processo entra no fim da fila"""
        novo = NodeSE(valor)
        if self.Inicio is None:
            self.Inicio = self.Fim = novo
        else:
            self.Fim.proximo = novo
            self.Fim = novo
        self.Tamanho += 1
        print(f"\n(+) INSERIDO PID {valor} NA CAUDA")
        self.desenhar_lista()

    def remover_cabeca(self):
        """Remoção na Cabeça: O processo mais antigo sai primeiro (FIFO)"""
        if self.Inicio is None:
            print("\n[ERRO]: Underflow! Fila de processos vazia.")
            return

        valor = self.Inicio.elemento
        self.Inicio = self.Inicio.proximo
        if self.Inicio is None:
            self.Fim = None

        self.Tamanho -= 1
        print(f"\n(-) REMOVIDO PID {valor} DA CABEÇA")
        self.desenhar_lista()

    def contar_processos(self):
        """CONTAGEM MANUAL: Percorre a lista sem usar self.Tamanho"""
        contador_local = 0
        atual = self.Inicio
        
        while atual:
            contador_local += 1
            atual = atual.proximo # Pula para o próximo nó
            
        return contador_local

# --- Menu de Interação ---
lse = ListaSE_Interativa()

while True:
    print("\n1: Inserir PID | 2: Remover Cabeça | 3: Contar Processos | 4: Sair")
    op = input("Escolha uma opção: ")

    if op == '1':
        try:
            pid = int(input("Digite o PID do processo: "))
            lse.inserir_cauda(pid)
        except ValueError:
            print("Por favor, digite um número inteiro.")
            
    elif op == '2':
        lse.remover_cabeca()
        
    elif op == '3':
        # Aqui chamamos a função que percorre a lista
        total = lse.contar_processos()
        print(f"\n[VERIFICAÇÃO DINÂMICA]: Foram encontrados {total} nós percorrendo a lista.")
        
    elif op == '4':
        print("Encerrando simulador de processos.")
        break
    else:
        print("Opção inválida!")