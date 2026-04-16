# Implemente um Tipo Abstrato de Dado (TAD) de Pilha utilizando uma lista de Python. O programa deve permitir adicionar palavras (push) e remover a última palavra (pop), seguindo o conceito LIFO.

class Pilha:
    def __init__(self):
        self.palavras = []

    def push(self, palavra):
        self.palavras.append(palavra)

    def pop(self):
        if len(self.palavras) > 0:
            return self.palavras.pop()
        else:
            print(f"pilha vazia")
            return None
        
minha_pilha = Pilha()
minha_pilha.push("programacao")
minha_pilha.push("PYTHON")
minha_pilha.pop()
print(minha_pilha.palavras)
    