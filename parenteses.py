# Quando um parêntese abre ( é encontrado, ele é "empilhado"; quando um parêntese fecha ) aparece, o sistema deve "desempilhar" o último que entrou para verificar se formam um par.
# O Desafio: Crie uma classe de Pilha com os métodos push (empilhar) e pop (desempilhar) para simular o armazenamento desses símbolos.

def verificar_parenteses(expressao):
    pilha = []  # inicializa a pilha

    for char in expressao:
        if char == "(":
            pilha.append(char)  # empilha quando encontra "("
        elif char == ")":
            if len(pilha) == 0:  # não há "(" para fechar
                return "Erro: parêntese fechado sem abertura."
            pilha.pop()  # desempilha quando encontra ")"

    # no final, se a pilha não estiver vazia, ainda há "(" sem fechar
    if len(pilha) == 0:
        return "Expressão correta: todos os parênteses foram fechados."
    else:
        return "Erro: ainda há parênteses abertos sem fechamento."

expressao = input("Digite uma expressão matemática: ")
resultado = verificar_parenteses(expressao)
print(resultado)

    