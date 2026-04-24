# Pesquisadores utilizam IDs numéricos para identificar fragmentos de sequências genéticas.Inserção: Organize 12 fragmentos.
# Busca com Contagem: A função de busca deve retornar não apenas se o fragmento existe, mas também qual é a profundidade (nível) em que ele se encontra, indicando quão complexo foi o acesso a essa informação genética.

class Fragmento:
    def __init__(self, id_fragmento):
        self.id = id_fragmento
        self.esquerda = self.direita = None

class SequenciamentoDNA:
    def __init__(self):
        self.raiz = None

    def inserir(self, id_fragmento):
        if self.raiz is None:
            self.raiz = Fragmento(id_fragmento)
        else:
            self._inserir_recursivo(self.raiz, id_fragmento)

    def _inserir_recursivo(self, no_atual, id_fragmento):
        if id_fragmento < no_atual.id:
            if no_atual.esquerda is None:
                no_atual.esquerda = Fragmento(id_fragmento)
            else:
                self._inserir_recursivo(no_atual.esquerda, id_fragmento)
        elif id_fragmento > no_atual.id:
            if no_atual.direita is None:
                no_atual.direita = Fragmento(id_fragmento)
            else:
                self._inserir_recursivo(no_atual.direita, id_fragmento)

    def buscar_com_profundidade(self, id_alvo):
        print(f"\n--- Mapeando Fragmento {id_alvo} ---")
        return self._buscar_recursivo(self.raiz, id_alvo, 1)

    def _buscar_recursivo(self, no_atual, id_alvo, nivel):
        if no_atual is None:
            print(" [X] Fragmento não encontrado no sequenciamento.")
            return None
        if no_atual.id == id_alvo:
            print(f" >>> Sucesso: Fragmento localizado no nível {nivel} de complexidade.")
            return nivel
        if id_alvo < no_atual.id:
            return self._buscar_recursivo(no_atual.esquerda, id_alvo, nivel + 1)
        else:
            return self._buscar_recursivo(no_atual.direita, id_alvo, nivel + 1)

# --- INTERAÇÃO ---
dna = SequenciamentoDNA()
for i in [1000, 500, 1500, 250, 750, 1250]: dna.inserir(i)
dna.buscar_com_profundidade(750)