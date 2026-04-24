# Crie uma estrutura de classe para o No e para a ListaMusical. Implemente o método inserir_no_final.

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaMusical:
    def __init__(self):
        self.head = None
    
    def inserir_no_final(self, valor):
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
            print(no_atual.valor, end = " ")
            no_atual = no_atual.proximo

lista = ListaMusical()
lista.inserir_no_final(5)
lista.inserir_no_final(8)
lista.imprimir()