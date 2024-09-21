class Pessoa:
    def __init__(self, nome="", idade=0, profissao=""):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"{self.nome} tem {self.idade} anos e sua profissão é: {self.profissao}"

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        if self.profissao:
            return print(f"Olá, sou {self.nome}! Trabalho como {self.profissao}.")
        else:
            return print(f"Olá, sou {self.nome}!")


pessoa1 = Pessoa("Adriano", 38, "QA Manager")
print(pessoa1)
pessoa1.aniversario()
print(pessoa1)
pessoa1.saudacao

pessoa2 = Pessoa("Aline", 39)
print(pessoa2)
pessoa2.aniversario()
print(pessoa2)
pessoa2.saudacao
