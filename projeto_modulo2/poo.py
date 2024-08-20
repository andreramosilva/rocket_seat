
class Pessoa:
    def __init__(self,nome,idade) ->None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá Meu nome é {self.nome} e tenho {self.idade}"

pessoa1 = Pessoa("Alice",30)