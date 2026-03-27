class NodeSE:
  def __init__(self, elemento):
    self.elemento = elemento
    self.proximo = None

# Classe de controle da lista
class ListaSE_interativa:
  def __init__(self):
    self.Inicio = None
    self.Fim = None
    self.Tamanho = 0

  def desenhar_lista(self):
      if self.Tamanho == 0:
        print("\n[ESTADO ATUAL]: Lista Vazia (CABEÇA -> NULO <- CAUDA)")
        return
      print(f"\n--- CONFIGURAÇÃO DA LSE (Tamanho: {self.Tamanho}) ---")
      print(f"PONTEIRO CABEÇA: [{self.Inicio.elemento}]")



  def inserir_cabeca(self, valor):
        """Inclusão na Cabeça: Complexidade O(1) [cite: 84]"""
        novo = NodeSE(valor)
        if self.Tamanho == 0:
            self.Inicio = self.Fim = novo
        else:
            # O novo nó aponta para a atual cabeça
            novo.proximo = self.Inicio
            # A referência de início da lista muda para o novo nó [cite: 185]
            self.Inicio = novo
        self.Tamanho += 1
        print(f"\n(+) INSERIDO {valor} NA CABEÇA")
        self.desenhar_lista()


  def remover_cabeca(self):
        if self.Tamanho == 0:
            print("\n[ERRO]: Underflow! Lista já está vazia.")
            return

        while self.Tamanho > 0:
          valor_removido = self.Inicio.elemento
          self.Inicio = self.Inicio.proximo
          self.Tamanho -= 1

          if self.Inicio is None:
            self.Fim = None
          print(f"\n(-) REMOVIDO {valor_removido} DA CABEÇA")
          self.desenhar_lista()

# --- Menu de Interação ---
lse = ListaSE_interativa()
while True:
    print("\n1: Inserir Canal: | 2: Limpar Histórico | 3: Sair")
    op = input("Escolha uma opção: ")

    if op == '1':
        lse.inserir_cabeca(int(input("Canal: ")))
    elif op == '2':
        lse.remover_cabeca()
    elif op == '3':
        print("Finalizando simulador.")
        break