class Fila:
    def __init__(self):
        self.valores = []
    def enqueue(self, valor):
        self.valores.append(valor)
    def dequeue(self):
        if len(self.valores) > 0:
            return self.valores.pop(0)
        else:
            print("Pilha vazia")
            return None
    
minha_fila = Fila()
minha_fila.enqueue(5)
minha_fila.enqueue(7)
minha_fila.enqueue(9)
print(minha_fila.valores)
minha_fila.dequeue()
print(minha_fila.valores)