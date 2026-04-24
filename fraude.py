# Uma operadora de cartão de crédito armazena os valores das transações de um cliente nos últimos 10 minutos em uma BST para detectar comportamentos atípicos.
# Inserção: Insira 15 valores de transações.
# Busca por Intervalo: O sistema deve buscar e listar todas as transações entre R$ 100,00 e R$ 500,00. 
# Se nenhuma transação for encontrada nesse intervalo, deve emitir um alerta de "Perfil de Consumo Estável".

class Transacao:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class MonitoramentoFraude:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = Transacao(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = Transacao(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = Transacao(valor)
            else:
                self._inserir_recursivo(no_atual.direita, valor)

    def buscar_intervalo(self, min_valor, max_valor):
        encontrados = []
        print(f"\n--- Analisando transações entre R$ {min_valor} e R$ {max_valor} ---")
        self._buscar_intervalo_recursivo(self.raiz, min_valor, max_valor, encontrados)
        if not encontrados:
            print(" [!] Alerta: Perfil de Consumo Estável.")
        else:
            print(f" [!] Transações detectadas no intervalo: {encontrados}")
        return encontrados

    def _buscar_intervalo_recursivo(self, no_atual, min_valor, max_valor, encontrados):
        if no_atual is None:
            return
        if no_atual.valor > min_valor:
            self._buscar_intervalo_recursivo(no_atual.esquerda, min_valor, max_valor, encontrados)
        if min_valor <= no_atual.valor <= max_valor:
            encontrados.append(no_atual.valor)
        if no_atual.valor < max_valor:
            self._buscar_intervalo_recursivo(no_atual.direita, min_valor, max_valor, encontrados)

# --- INTERAÇÃO ---
fintech = MonitoramentoFraude()
print("--- CADASTRO DE TRANSAÇÕES ---")
while True:
    entrada = input("Valor da transação (ou 'fim'): ").strip()
    if entrada.lower() == 'fim': break
    try: fintech.inserir(float(entrada))
    except ValueError: print("Digite um número.")

print("\n--- MÓDULO DE DETECÇÃO DE INTERVALO ---")
fintech.buscar_intervalo(100.0, 500.0)
