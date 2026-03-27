class Pilha:
    def __init__(self):
        self.valores = []
    def push(self, valor):
        self.valores.append(valor)
    def pop(self):
        if len(self.valores) > 0:
            return self.valores.pop()
        else:
            print("Pilha vazia")
            return None
    
minha_pilha = Pilha()
minha_pilha.push(5)
minha_pilha.push(7)
minha_pilha.push(9)
print(minha_pilha.valores)
minha_pilha.pop()
print(minha_pilha.valores)