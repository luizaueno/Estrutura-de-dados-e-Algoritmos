class Node: 
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Listaligada:
    def __init__(self):
        self.head = None # inicio da lista

    def inserir(self, valor):
        novo_no = Node(valor)
        if self.head is None:
            self.head = novo_no
            return
        no_atual = self.head
        while no_atual.proximo is not None:
            no_atual = no_atual.proximo
        no_atual.proximo = novo_no

    def imprimir(self):
        no_atual = self.head
        while no_atual is not None:
            print(no_atual.valor)
            no_atual = no_atual.proximo

lista = Listaligada()
lista.inserir(3)
lista.inserir(5)
lista.inserir(8)
lista.imprimir()