# Um servidor de CDN (Content Delivery Network) armazena IDs de vídeos populares para acesso rápido.
#Inserção: Crie uma árvore com IDs de vídeos.
# Verificação de Balanceamento: Após as inserções, o aluno deve buscar o vídeo com o ID central.

class Video:
    def __init__(self, id_video):
        self.id = id_video
        self.esquerda = self.direita = None

class CacheCDN:
    def __init__(self):
        self.raiz = None

    def inserir(self, id_video):
        if self.raiz is None:
            self.raiz = Video(id_video)
        else:
            self._inserir_recursivo(self.raiz, id_video)

    def _inserir_recursivo(self, no_atual, id_video):
        if id_video < no_atual.id:
            if no_atual.esquerda is None:
                no_atual.esquerda = Video(id_video)
            else:
                self._inserir_recursivo(no_atual.esquerda, id_video)
        elif id_video > no_atual.id:
            if no_atual.direita is None:
                no_atual.direita = Video(id_video)
            else:
                self._inserir_recursivo(no_atual.direita, id_video)

    def verificar_cache_central(self):
        if not self.raiz:
            print("Cache vazio.")
        else:
            print(f"\n--- Verificação de Balanceamento ---")
            print(f" O Vídeo no topo do Cache (Raiz) é o ID: {self.raiz.id}")

# --- INTERAÇÃO ---
cdn = CacheCDN()
for v in [500, 250, 750, 100, 300]: cdn.inserir(v)
cdn.verificar_cache_central()
