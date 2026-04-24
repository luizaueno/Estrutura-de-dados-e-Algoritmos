# Um chatbot de suporte utiliza uma BST para navegar entre temas de ajuda (IDs de tópicos).
#Inserção: Insira os tópicos de ajuda.
# Busca por Prefixo: O aluno deve buscar um tópico específico. Se o tópico não existir, a busca deve retornar o tópico mais próximo (o nó pai onde a busca terminou), oferecendo uma "sugestão aproximada" ao usuário.


class Topico:
    def __init__(self, id_topico):
        self.id = id_topico
        self.esquerda = self.direita = None

class ChatbotBST:
    def __init__(self):
        self.raiz = None

    def inserir(self, id_topico):
        if self.raiz is None:
            self.raiz = Topico(id_topico)
        else:
            self._inserir_recursivo(self.raiz, id_topico)

    def _inserir_recursivo(self, no_atual, id_topico):
        if id_topico < no_atual.id:
            if no_atual.esquerda is None:
                no_atual.esquerda = Topico(id_topico)
            else:
                self._inserir_recursivo(no_atual.esquerda, id_topico)
        elif id_topico > no_atual.id:
            if no_atual.direita is None:
                no_atual.direita = Topico(id_topico)
            else:
                self._inserir_recursivo(no_atual.direita, id_topico)

    def buscar_ajuda(self, id_alvo):
        print(f"\n--- Pesquisando Tópico {id_alvo} ---")
        return self._buscar_com_sugestao(self.raiz, id_alvo, None)

    def _buscar_com_sugestao(self, no_atual, alvo, pai):
        if no_atual is None:
            print(f" [?] Tópico não encontrado. Você quis dizer '{pai.id}'?")
            return None

        if no_atual.id == alvo:
            print(f" [!] Tópico {no_atual.id} encontrado! Abrindo menu...")
            return no_atual.id

        if alvo < no_atual.id:
            return self._buscar_com_sugestao(no_atual.esquerda, alvo, no_atual)
        else:
            return self._buscar_com_sugestao(no_atual.direita, alvo, no_atual)

# --- INTERAÇÃO ---
chatbot = ChatbotBST()
for t in [100, 50, 150, 25, 75]: chatbot.inserir(t)
chatbot.buscar_ajuda(80) # Vai sugerir o tópico 75