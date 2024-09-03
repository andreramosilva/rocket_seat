class Refeicao():
    def __init__(self, nome, descricao, data_hora , esta_na_dieta):
        self.nome = nome
        self.descricao = descricao
        self.data_hora = data_hora
        self.esta_na_dieta = False # default value

    def __str__(self):
        return f'{self.nome} - {self.descricao} - {self.data_hora} - {self.esta_na_dieta}'