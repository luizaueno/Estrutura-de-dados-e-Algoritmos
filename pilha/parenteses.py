# Crie um código que receba uma expressão matemática (ex: ((A+B)*C)) e use uma pilha para verificar se todos os parênteses abertos
# foram devidamente fechados.

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
