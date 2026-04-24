# Um firewall armazena endereços IPs (convertidos para inteiros longos) que tentaram ataques de força bruta. 
#Inserção: Alimente a BST com IPs suspeitos.
# Busca Negativa: Implemente um teste onde o aluno busca por um IP que não está na árvore. O programa deve explicar por que a busca falhou (ex: "ID maior que o último nó folha encontrado").


class IP:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class FirewallBST:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = IP(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = IP(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = IP(valor)
            else:
                self._inserir_recursivo(no_atual.direita, valor)

    def checar_ip(self, ip_alvo):
        print(f"\n--- Verificando IP: {ip_alvo} ---")
        return self._buscar_negativa(self.raiz, ip_alvo, None)

    def _buscar_negativa(self, no_atual, alvo, pai):
        if no_atual is None:
            # Explicação da falha baseada no último nó visitado
            direcao = "maior" if alvo > pai.valor else "menor"
            print(f" [OK] IP Seguro. Motivo: ID {alvo} é {direcao} que o nó folha {pai.valor}.")
            return None

        if no_atual.valor == alvo:
            print(f" [ALERTA] IP {alvo} LOCALIZADO NA LISTA NEGRA!")
            return no_atual.valor

        if alvo < no_atual.valor:
            return self._buscar_negativa(no_atual.esquerda, alvo, no_atual)
        else:
            return self._buscar_negativa(no_atual.direita, alvo, no_atual)

# --- INTERAÇÃO ---
firewall = FirewallBST()
for ip in [200, 100, 300, 50, 150]: firewall.inserir(ip)
firewall.checar_ip(120) # Exemplo de busca negativa