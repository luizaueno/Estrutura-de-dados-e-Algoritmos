# Um marketplace como o Mercado Livre organiza os anúncios de um vendedor por preço para alimentar os filtros da interface.
#Inserção: O aluno deve inserir preços de produtos vindos de uma lista desordenada.
#Busca Extrema: Implemente funções para encontrar o produto mais barato e o mais caro da loja sem percorrer a árvore inteira, apenas usando a propriedade da BST (extrema esquerda e extrema direita).

class Produto:
    def __init__(self, preco):
        self.preco = preco
        self.esquerda = self.direita = None

class FiltroPrecos:
    def __init__(self):
        self.raiz = None

    def inserir(self, preco):
        if self.raiz is None:
            self.raiz = Produto(preco)
        else:
            self._inserir_recursivo(self.raiz, preco)

    def _inserir_recursivo(self, no_atual, preco):
        if preco < no_atual.preco:
            if no_atual.esquerda is None:
                no_atual.esquerda = Produto(preco)
            else:
                self._inserir_recursivo(no_atual.esquerda, preco)
        elif preco > no_atual.preco:
            if no_atual.direita is None:
                no_atual.direita = Produto(preco)
            else:
                self._inserir_recursivo(no_atual.direita, preco)

    def buscar_extremos(self):
        if not self.raiz:
            print("Loja vazia!")
            return
        
        # O mais barato está no extremo esquerdo
        barato = self.raiz
        while barato.esquerda: barato = barato.esquerda
        
        # O mais caro está no extremo direito
        caro = self.raiz
        while caro.direita: caro = caro.direita
        
        print(f"\n--- RESUMO DE PREÇOS ---")
        print(f" Menor Preço: R$ {barato.preco}")
        print(f" Maior Preço: R$ {caro.preco}")

# --- INTERAÇÃO ---
loja = FiltroPrecos()
precos = [150.0, 80.0, 300.0, 45.0, 200.0]
for p in precos: loja.inserir(p)
loja.buscar_extremos()
