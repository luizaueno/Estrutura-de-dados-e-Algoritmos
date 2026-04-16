class FilaDupla:
    def __init__(self):
        self.valores = []
    def add_frente(self, valor):
        self.valores.insert(0, valor)
    def add_fim(self, valor):
        self.valores.append(valor)
    def remove_frente(self):
        if len(self.valores) > 0:
            return self.valores.pop(0)
        else:
            print("Pilha vazia")
            return None
    def remove_fim(self):
        if len(self.valores) > 0:
            return self.valores.pop()
        else:
            print("Pilha vazia")
            return None
    
minha_fila = FilaDupla()
minha_fila.add_frente(5)
minha_fila.add_fim(7)
minha_fila.add_frente(9)
print(minha_fila.valores)
minha_fila.remove_fim()
minha_fila.remove_frente()
print(minha_fila.valores)