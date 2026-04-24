
# Desenvolva uma função recursiva que calcule o custo total de vedação para uma embalagem de nível N, sabendo que o custo base (nível 1) é de R$ 10,00 e o custo do nível N é definido por Custo(N) = N x Custo(N-1).

def custo(n):
    if n == 1:
        return 10
    valor_atual = n * custo(n-1)
    return valor_atual +custo(n-1)
print(custo(2))

