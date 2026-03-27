# Implemente uma LDE para armazenar ações de um usuário. Ao realizar uma nova ação, insira na Cauda.
#  O sistema deve permitir "voltar" (ponteiro anterior) e "avançar" (ponteiro próximo).

class NodeDE:
    def __init__(self, elemento):
        self.elemento = elemento
        self.proximo = None
        self.anterior = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0
        self.cursor = None  # Representa a "foto atual"

    def inserir_cauda(self, valor):
        novo = NodeDE(valor)
        if self.tamanho == 0:
            self.cabeca = self.cauda = novo
        else:
            self.cauda.proximo = novo
            novo.anterior = self.cauda
            self.cauda = novo
        self.tamanho += 1
        print(f"Foto '{valor}' adicionada ao álbum.")

    def mover_cursor_inicio(self):
        if self.cabeca:
            self.cursor = self.cabeca
            print(f"Cursor no início: {self.cursor.elemento}")
        else:
            print("Álbum vazio.")

    def mover_cursor_fim(self):
        if self.cauda:
            self.cursor = self.cauda
            print(f"Cursor no fim: {self.cursor.elemento}")
        else:
            print("Álbum vazio.")

    def proxima_foto(self):
        if self.cursor and self.cursor.proximo:
            self.cursor = self.cursor.proximo
            print(f"Próxima foto: {self.cursor.elemento}")
        else:
            print("Não há próxima foto.")

    def foto_anterior(self):
        if self.cursor and self.cursor.anterior:
            self.cursor = self.cursor.anterior
            print(f"Foto anterior: {self.cursor.elemento}")
        else:
            print("Não há foto anterior.")

    def mostrar_album(self):
        """Mostra todas as fotos em sequência"""
        if self.tamanho == 0:
            print("Álbum vazio.")
            return
        atual = self.cabeca
        print("Álbum completo:")
        while atual:
            print(f"- {atual.elemento}")
            atual = atual.proximo

# --- Simulação ---
lde = ListaDuplamenteEncadeada()
print("ÁLBUM DE FOTOS - Navegação com LDE")

while True:
    print("\nOPÇÕES: 1: +Foto | 2: Início | 3: Fim | 4: Próxima | 5: Anterior | 6: Mostrar álbum | 7: Sair")
    op = input("Escolha: ")

    if op == '1':
        lde.inserir_cauda(input("Nome da foto: "))
    elif op == '2':
        lde.mover_cursor_inicio()
    elif op == '3':
        lde.mover_cursor_fim()
    elif op == '4':
        lde.proxima_foto()
    elif op == '5':
        lde.foto_anterior()
    elif op == '6':
        lde.mostrar_album()
    elif op == '7':
        print("Finalizando...")
        break
    else:
        print("Opção inválida.")