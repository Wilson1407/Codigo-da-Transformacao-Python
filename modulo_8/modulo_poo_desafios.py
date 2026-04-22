"""
Criar um Sistema de Bioblioteca

Class Livro

Class Biblioteca (main)

    (Produtos)
    Livros, Periodicos, Jornal, Maps, Gibi/Mangás

    (Processos / Serviços)
    Ler, Pesquisa, emprestado-Devolução

"""

class Livros:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

        def __str__(self):
            status = "Disponivel" if self.disponivel else "Emprestado"
            return f" '{self.titulo}' - {self.autor} [status]"
        
    class Biblioteca:
        def __init__(self):
            self.livros = []

        def adicionar_livro(self, livro):
            self.livros.append(livro)

        def emprestrar_livro(self, titulo_procurado):
            for livro in self.livros:
                if self.livro.disponivel:
                    livro.disponivel = False
                    print(f"Emprestimo de '(livro.titulo)' realizado")
                else:
                    print(f"O Livro '{livro.titulo}' já está ocupado.")
                    return
                print("Livro não encontrado no acervo. ")