# Inserção: Insira pacientes conforme chegam.Busca de Maior Prioridade: Implemente uma busca que localize o paciente com o maior Score de risco. 
# Após localizá-lo, a função deve imprimir o nome do paciente e o caminho percorrido pela equipe médica na árvore.

class Paciente:
    def __init__(self, nome, score):
        self.nome = nome
        self.score = score
        self.esquerda = self.direita = None

class TriagemHospitalar:
    def __init__(self):
        self.raiz = None

    def inserir(self, nome, score):
        if self.raiz is None:
            self.raiz = Paciente(nome, score)
        else:
            self._inserir_recursivo(self.raiz, nome, score)

    def _inserir_recursivo(self, no_atual, nome, score):
        if score < no_atual.score:
            if no_atual.esquerda is None:
                no_atual.esquerda = Paciente(nome, score)
            else:
                self._inserir_recursivo(no_atual.esquerda, nome, score)
        elif score > no_atual.score:
            if no_atual.direita is None:
                no_atual.direita = Paciente(nome, score)
            else:
                self._inserir_recursivo(no_atual.direita, nome, score)

    def buscar_urgencia_maxima(self):
        if not self.raiz:
            print("Nenhum paciente na fila.")
            return
        print(f"\n--- Rota de Emergência (Busca por Maior Score) ---")
        return self._buscar_max(self.raiz)

    def _buscar_max(self, no_atual):
        # Se houver alguém mais grave à direita, continue
        if no_atual.direita:
            print(f" [->] Equipe passando por: {no_atual.nome} (Score {no_atual.score})")
            return self._buscar_max(no_atual.direita)
        
        # Chegou no extremo direito
        print(f" [!!!] ALVO LOCALIZADO: {no_atual.nome} (Score {no_atual.score})")
        return no_atual

# --- INTERAÇÃO ---
hospital = TriagemHospitalar()
hospital.inserir("João", 10)
hospital.inserir("Maria", 45)
hospital.inserir("Ana", 30)
hospital.inserir("Carlos", 50) # Mais grave
hospital.buscar_urgencia_maxima()