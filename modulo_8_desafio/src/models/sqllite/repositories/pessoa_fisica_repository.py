from src.models.sqllite.entities.pessoa_fisica import PessoaFisica
from src.models.sqllite.interfaces.cliente import Cliente


class PessoaFisicaRepository(Cliente):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert_pessoa_fisica(self, renda_mensal, idade, nome_completo, celular, email, categoria, saldo):
        with self.db_connection as database:
            try:
                self.pessoa_fisica = PessoaFisica(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
                database.session.add(self.pessoa_fisica)
                database.session.commit()
            except Exception as error:
                return error

    def list(self):
        with self.db_connection as database:
            self.pessoa_fisica = database.session.query(PessoaFisica).all()
            return self.pessoa_fisica

    def sacar(self, valor: float, id_pessoa_fisica: int):
        with self.db_connection as database:
            self.pessoa_fisica = database.session.query(PessoaFisica).filter(PessoaFisica.id == id_pessoa_fisica).first()
            if self.pessoa_fisica.saldo < valor:
                return 'Saldo insuficiente'
            self.pessoa_fisica.saldo -= valor
            database.session.commit()
            return self.pessoa_fisica
    

    def extrato(self, id_pessoa_fisica: int):
        with self.db_connection as database:
            self.pessoa_fisica = database.session.query(PessoaFisica).all()
            return self.pessoa_fisica