# 1) Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    # 2) Na classe Livro, adicione um método especial __str__ que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    def __str__(self) -> str:
        return f"O livro {self.titulo} do autor {self.autor} foi publicado em {self.ano_publicacao}"

    # 3) Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    def emprestar(self):
        self.disponivel = False

    # 4) Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [
            livro
            for livro in Livro.livros
            if livro.ano_publicacao == ano and livro.disponivel
        ]
        return livros_disponiveis


livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro3 = Livro("Duna", "Frank Herbert", 1965)
print(livro1)
print(livro2)
print(livro3)

print(f"Antes de emprestar: Livro disponível? {livro1.disponivel}")
livro1.emprestar()
print(f"Antes de emprestar: Livro disponível? {livro1.disponivel}\n")

Livro.livros = [livro1, livro2, livro3]  # Adicionando os livros à lista de livros
