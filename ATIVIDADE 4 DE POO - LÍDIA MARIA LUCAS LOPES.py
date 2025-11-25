# - Lídia Maria L. Lopes

# Problema 1 - Publicações

# Classe base -> Publicacao
class Publicacao:
    def __init__(self, titulo, ano_publicacao):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao

    def descrever(self): # Possui o método descrever que imprime o título e o ano de publicação.
        print(f"Título: {self.titulo}")
        print(f"Ano de publicação: {self.ano_publicacao}")

# Classe Livro -> herda de Publicacao
class Livro(Publicacao):
    def __init__(self, titulo, ano_publicacao, autor): # Adicionei o método autor
        super().__init__(titulo, ano_publicacao) # Referenciando a classe pai usando o super()
        self.autor = autor

    def descrever(self):
        super().descrever()  # Chamando o método descrever da classe base
        print(f"Autor: {self.autor}")

# Classe Revista -> herda de Publicacao
class Revista(Publicacao):
    def __init__(self, titulo, ano_publicacao, edicao):
        super().__init__(titulo, ano_publicacao) # Referenciando a classe pai usando o super()
        self.edicao = edicao

    def descrever(self):
        super().descrever()  # Chamando o método descrever da classe base
        print(f"Edição: {self.edicao}")

# Alguns testes...
livro = Livro("O Senhor dos Anéis", 1954, "J.R.R. Tolkien")
revista = Revista("Revista Exemplo", 2023, "Edição 42")

print("Descrição do livro:")
livro.descrever()

print("\nDescrição da revista:")
revista.descrever()
