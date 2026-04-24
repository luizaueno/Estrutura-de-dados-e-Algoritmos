# Uma plataforma de recrutamento organiza candidatos por "Pontuação Técnica" (0 a 1000).Inserção: Popule a árvore com 20 candidatos.
# Busca de Sucessor: Dado um candidato com pontuação 750, a função de busca deve encontrar quem é o candidato imediatamente superior a ele (o sucessor em ordem) para uma vaga de backup.

class Candidato:
    def __init__(self, score):
        self.score = score
        self.esquerda = self.direita = None

class BancoTalentos:
    def __init__(self):
        self.raiz = None

    def inserir(self, score):
        if self.raiz is None:
            self.raiz = Candidato(score)
        else:
            self._inserir_recursivo(self.raiz, score)

    def _inserir_recursivo(self, no_atual, score):
        if score < no_atual.score:
            if no_atual.esquerda is None:
                no_atual.esquerda = Candidato(score)
            else:
                self._inserir_recursivo(no_atual.esquerda, score)
        elif score > no_atual.score:
            if no_atual.direita is None:
                no_atual.direita = Candidato(score)
            else:
                self._inserir_recursivo(no_atual.direita, score)

    def buscar_sucessor(self, score_alvo):
        print(f"\n--- Buscando sucessor para Score {score_alvo} ---")
        no_candidato = self._localizar(self.raiz, score_alvo)
        
        if no_candidato and no_candidato.direita:
            # Sucessor é o menor do ramo direito
            sucessor = no_candidato.direita
            while sucessor.esquerda: sucessor = sucessor.esquerda
            print(f" >>> Sucessor (Backup) encontrado: Score {sucessor.score}")
        else:
            print(" [!] Não há sucessor imediato para este candidato.")

    def _localizar(self, no_atual, alvo):
        if no_atual is None or no_atual.score == alvo:
            return no_atual
        if alvo < no_atual.score:
            return self._localizar(no_atual.esquerda, alvo)
        return self._localizar(no_atual.direita, alvo)

# --- INTERAÇÃO ---
rh = BancoTalentos()
scores = [500, 250, 750, 600, 800]
for s in scores: rh.inserir(s)
rh.buscar_sucessor(750)
