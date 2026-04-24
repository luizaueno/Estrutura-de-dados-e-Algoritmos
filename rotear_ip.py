# Um roteador de alta performance armazena prefixos de rede (IDs numéricos) para decidir o salto de saída.
# Inserção: Insira uma sequência de 10 IDs de sub-redes.
# Busca: Implemente uma busca que, além de achar o ID, mostre todos os "Roteadores" (Nós) que o pacote atravessou do topo (raiz) até o destino. 

class IP:
    def __init__(self, id_pacote):
        self.id = id_pacote
        self.esquerda = None 
        self.direita = None 

class RoteamentoBST:
    def __init__(self):
        self.raiz = None
    
    def inserir(self, id_pacote):
        if self.raiz is None:
            self.raiz = IP(id_pacote)
            print(f"Raiz criada: (ID {id_pacote})")
        else: 
            self.inserir_recursivo(self.raiz, id_pacote)

    def inserir_recursivo(self, no_atual, id_pacote):
        if id_pacote < no_atual.id:
            if no_atual.esquerda is None:
                no_atual.esquerda = IP(id_pacote)
                print(f"Inserindo {id_pacote} à esquerda de {no_atual.id}")
            else:
                self.inserir_recursivo(no_atual.esquerda, id_pacote)
        elif id_pacote > no_atual.id:
            if no_atual.direita is None:
                no_atual.direita = IP(id_pacote)
                print(f"Inserindo {id_pacote} à direita de {no_atual.id}")
            else:
                self.inserir_recursivo(no_atual.direita, id_pacote)
        else:
            print(f"Erro: ID {id_pacote} duplicado.")

    def buscar_com_passos(self, id_alvo):
        if not self.raiz:
            print("Árvore de roteamento vazia!")
            return None
        print(f"\n--- Traceroute para ID {id_alvo} ---")
        return self._buscar_recursivo(self.raiz, id_alvo, 1)

    def _buscar_recursivo(self, no_atual, id_alvo, passo):
        if no_atual is None:
            print(f" Salto {passo}: Espaço vazio. Destino não alcançado.")
            return None

        # Log do Traceroute (mostra os nós atravessados)
        print(f" Salto {passo}: Passando pelo roteador {no_atual.id}...")

        if no_atual.id == id_alvo:
            print(f" >>> SUCESSO: Pacote entregue ao ID {id_alvo}!")
            return no_atual.id

        if id_alvo < no_atual.id:
            return self._buscar_recursivo(no_atual.esquerda, id_alvo, passo + 1)
        else:
            return self._buscar_recursivo(no_atual.direita, id_alvo, passo + 1)

# --- INTERAÇÃO ---
roteador = RoteamentoBST()

print("--- CADASTRO DE SUB-REDES ---")
while True:
    entrada = input("ID da sub-rede (ou 'fim'): ").strip()
    if entrada.lower() == 'fim': break
    try:
        roteador.inserir(int(entrada)) 
    except ValueError:
        print("Digite um número.")

while True:
    busca = input("\nID para rastrear (ou 'sair'): ").strip()
    if busca.lower() == 'sair': break
    try:
        roteador.buscar_com_passos(int(busca))
    except ValueError:
        print("Digite apenas números.")