# =====================================================================
# 1. DEFINIÇÃO DA ESTRUTURA DE DADOS (Classes)
# =====================================================================

class Node:
    """Representa uma página (curso/notícia) no histórico."""

    def __init__(self, id_acesso, titulo, tipo):
        self.id_acesso = id_acesso  
        self.titulo = titulo 
        self.tipo = tipo  # "Curso" ou "Notícia"
        self.next = None  

    def __str__(self):
        return f"[{self.id_acesso}] {self.tipo}: {self.titulo}"


class ListaCircularOrdenada:
    def __init__(self):
        self.head = None

    def inserir(self, id_acesso, titulo, tipo):
        """Insere um novo acesso na lista mantendo-a ordenada."""
        novo_no = Node(id_acesso, titulo, tipo)

        
        if not self.head:
            self.head = novo_no
            novo_no.next = self.head
            return

        atual = self.head
        anterior = None

        
        if novo_no.id_acesso < self.head.id_acesso:
            ultimo = self.head
            while ultimo.next != self.head:
                ultimo = ultimo.next

            novo_no.next = self.head
            ultimo.next = novo_no
            self.head = novo_no
            return

        
        while True:
            anterior = atual
            atual = atual.next
            if novo_no.id_acesso < atual.id_acesso:
                break
            if atual == self.head:
                break

        anterior.next = novo_no
        novo_no.next = atual

    def exibir_historico(self, voltas=1):
        """Exibe o histórico demonstrando a circularidade."""
        if not self.head:
            print("Histórico vazio.")
            return

        atual = self.head
        contador_voltas = 0

        print("\n--- Histórico de Navegação Ordenado ---")
        while contador_voltas < voltas:
            print(atual)
            atual = atual.next
            if atual == self.head:
                contador_voltas += 1
                if contador_voltas < voltas:
                    print("... [Dando a volta na lista] ...")


# =====================================================================
# 2. CÓDIGO DE EXECUÇÃO (Onde a mágica acontece na prática)
# =====================================================================

if __name__ == "__main__":
    # Criando o histórico do site de programação
    meu_historico = ListaCircularOrdenada()

    print("Inserindo acessos fora de ordem...")
    meu_historico.inserir(3, "Curso de Java Avançado", "Curso")
    meu_historico.inserir(1, "Notícia: Lançamento do Python 3.12", "Notícia")
    meu_historico.inserir(4, "Notícia: O mercado de tecnologia em 2026", "Notícia")
    meu_historico.inserir(2, "Curso de Lógica de Programação", "Curso")

    
    meu_historico.exibir_historico(voltas=2)