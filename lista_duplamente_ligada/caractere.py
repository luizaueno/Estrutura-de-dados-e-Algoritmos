# Implemente uma LDE onde cada nó é um caractere. Como o cursor pode ir para frente e para trás, 
# o sistema deve permitir percorrer a lista usando os ponteiros.

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0
        self.cursor = None  # Aponta para o nó atual

    def mover_cursor_inicio(self):
        """Posiciona o cursor na cabeça"""
        if self.cabeca:
            self.cursor = self.cabeca
            print(f"Cursor no início: {self.cursor.elemento}")
        else:
            print("Lista vazia, cursor não pode ser movido.")

    def mover_cursor_fim(self):
        """Posiciona o cursor na cauda"""
        if self.cauda:
            self.cursor = self.cauda
            print(f"Cursor no fim: {self.cursor.elemento}")
        else:
            print("Lista vazia, cursor não pode ser movido.")

    def mover_cursor_proximo(self):
        """Move o cursor para o próximo nó"""
        if self.cursor and self.cursor.proximo:
            self.cursor = self.cursor.proximo
            print(f"Cursor avançou: {self.cursor.elemento}")
        else:
            print("Não há próximo nó.")

    def mover_cursor_anterior(self):
        """Move o cursor para o nó anterior"""
        if self.cursor and self.cursor.anterior:
            self.cursor = self.cursor.anterior
            print(f"Cursor retrocedeu: {self.cursor.elemento}")
        else:
            print("Não há nó anterior.")
