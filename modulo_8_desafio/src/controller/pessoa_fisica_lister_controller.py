from src.repository.pessoa_fisica_repository import PessoaFisicaRepository

class PessoaFisicaListerController:
    def __init__(self, pessoa_fisica_repository :  PessoaFisicaRepository):
        self.pessoa_fisica_repository = pessoa_fisica_repository

    def list(self):

        return self.pessoa_fisica_repository.list()

    def __format_response(self, pessoa_fisica):
        return {
            'id': pessoa_fisica.id,
            'renda_mensal': pessoa_fisica.renda_mensal,
            'idade': pessoa_fisica.idade,
            'nome_completo': pessoa_fisica.nome_completo,
            'celular': pessoa_fisica.celular,
            'email': pessoa_fisica.email,
            'categoria': pessoa_fisica.categoria,
            'saldo': pessoa_fisica.saldo
        }