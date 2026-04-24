
# Implemente um TAD de Fila para gerenciar os pedidos. O código deve permitir adicionar um novo pedido ao final da fila (inserção) e remover o pedido que já foi atendido na frente da fila (remoção).

class Fila:
    def __init__(self):
        self.pedidos = []

    def dequeue(self, pedidos):
        self.pedidos.append(pedidos)

    def enqueue(self):
        if len(self.pedidos) > 0:
            return self.pedidos.pop()
        else:
            print(f"fila vazia")
            return None
        
minha_fila = Fila()
minha_fila.push(2)
minha_fila.push(7)
minha_fila.pop()
print(minha_fila.pedidos)

