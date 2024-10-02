from src.models.sqllite.entities.pessoa_juridica import PessoaJuridica
from src.models.sqllite.interfaces.cliente import Cliente


class PessoaJuridicaRepository(Cliente):
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def insert_pessoa_juridica(self, faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo):
        with self.db_connection.session() as database:
            try:
                self.pessoa_juridica = PessoaJuridica(faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
                self.db_connection.session.add(self.pessoa_juridica)
                self.db_connection.session.commit()
            except Exception as error:
                return error

    def list(self):
        with self.db_connection.session() as database:
            self.pessoa_juridica = database.session.query(PessoaJuridica).all()
            return self.pessoa_juridica

    def sacar(self, valor):
        if self.pessoa_juridica.saldo < valor:
            return 'Saldo insuficiente'
        self.pessoa_juridica.saldo -= valor
        return self.pessoa_juridica
    

    def extrato(self):
        return self.pessoa_juridica

    