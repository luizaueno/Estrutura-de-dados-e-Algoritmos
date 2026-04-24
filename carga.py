# Um terminal de containers precisa organizar as cargas pelo Peso Bruto para otimizar o equilíbrio dos navios.
# Cada container possui um ID alfanumérico e um peso em toneladas. Implemente uma BST onde a chave de organização é o peso.
# Inserção: Deve impedir que dois containers com pesos idênticos ocupem o mesmo "slot" lógico na árvore para evitar erro de cálculo de balanço.
# Busca: Crie uma função que busque se existe algum container com exatamente $X$ toneladas e retorne o ID dele.


# --- DEFINIÇÃO DA ESTRUTURA ---

class Container:
    def __init__(self, id_carga, peso):
        self.id = id_carga
        self.peso = peso
        self.esquerda = None  # Pesos menores
        self.direita = None   # Pesos maiores

class GerenciamentoCarga:
    """Controlador da Árvore Binária de Busca."""
    def __init__(self):
        self.raiz = None

    def inserir(self, id_carga, peso):
        """Inicia a inserção na árvore."""
        if self.raiz is None:
            self.raiz = Container(id_carga, peso)
            print(f" Raiz criada: Peso {peso} (ID {id_carga})")
        else:
            self._inserir_recursivo(self.raiz, id_carga, peso)

    def _inserir_recursivo(self, no_atual, id_carga, peso):
        """Decide a posição do container baseando-se no peso."""
        if peso < no_atual.peso:
            if no_atual.esquerda is None:
                no_atual.esquerda = Container(id_carga, peso)
                print(f" Insert: {peso}t (ID {id_carga}) à ESQUERDA de {no_atual.peso}t")
            else:
                self._inserir_recursivo(no_atual.esquerda, id_carga, peso)
        elif peso > no_atual.peso:
            if no_atual.direita is None:
                no_atual.direita = Container(id_carga, peso)
                print(f" Insert: {peso}t (ID {id_carga}) à DIREITA de {no_atual.peso}t")
            else:
                self._inserir_recursivo(no_atual.direita, id_carga, peso)
        else:
            print(f" Erro: O peso {peso} já existe. O sistema não permite pesos duplicados.")

    def buscar_id_por_peso(self, peso_alvo):
        """Interface pública para busca."""
        if self.raiz is None:
            print(" A árvore está vazia!")
            return None
        print(f"\n--- Iniciando busca por {peso_alvo} toneladas ---")
        return self._buscar_recursivo(self.raiz, peso_alvo, 1)

    def _buscar_recursivo(self, no_atual, peso_alvo, passo):
        """Navega pela árvore comparando o peso alvo com o peso de cada nó."""
        if no_atual is None:
            print(f" Passo {passo}: Espaço vazio. Peso {peso_alvo} não encontrado.")
            return None

        print(f" Passo {passo}: Analisando Container ID {no_atual.id} (Peso: {no_atual.peso}t)")

        if no_atual.peso == peso_alvo:
            print(f" >>> SUCESSO: Peso {peso_alvo} encontrado no passo {passo}!")
            return no_atual.id

        if peso_alvo < no_atual.peso:
            print(f"  - Como {peso_alvo} < {no_atual.peso}, indo para a ESQUERDA.")
            return self._buscar_recursivo(no_atual.esquerda, peso_alvo, passo + 1)
        else:
            print(f"  - Como {peso_alvo} > {no_atual.peso}, indo para a DIREITA.")
            return self._buscar_recursivo(no_atual.direita, peso_alvo, passo + 1)

# --- FLUXO DE EXECUÇÃO ---

carga = GerenciamentoCarga()

print("--- SISTEMA DE GERENCIAMENTO DE CARGA (BST) ---")
print("Digite: ID Peso (Ex: CONT123 25.5). Digite 'fim' para terminar.")

# ETAPA 1: CADASTRO
while True:
    entrada = input("\nCadastro (ID Peso): ").strip()
    if entrada.lower() == 'fim': 
        break
    try:
        partes = entrada.split()
        id_cont = partes[0]
        peso_cont = float(partes[1]) # Converte para número (float)
        carga.inserir(id_cont, peso_cont)
    except (ValueError, IndexError):
        print(" Erro! Use o formato:  Numero")

# ETAPA 2: BUSCA
print("\n--- MÓDULO DE BUSCA INTELIGENTE ---")
while True:
    busca = input("\nDigite o PESO para localizar o container (ou 'sair'): ").strip()
    if busca.lower() == 'sair': 
        break
    try:
        peso_procurado = float(busca)
        id_encontrado = carga.buscar_id_por_peso(peso_procurado)
        
        if id_encontrado:
            print(f" RESULTADO: O container com {peso_procurado} é o ID: {id_encontrado}")
        else:
            print(f" RESULTADO: Nenhum container encontrado com exatamente {peso_procurado}.")
    except ValueError:
        print(" Por favor, digite um número válido para o peso.")