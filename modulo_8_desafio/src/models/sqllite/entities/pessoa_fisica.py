from sqlalchemy import Column, Integer, String , BIGINT, ForeignKey
from src.models.sqllite.settings.base import base


class PessoaFisica(base):
    __tablename__ = 'pessoa_fisica'

    id = Column(Integer, primary_key=True)
    renda_mensal = Column(BIGINT)
    idade = Column(Integer)
    nome_completo = Column(String)
    celular = Column(String)
    email = Column(String)
    categoria = Column(String)
    saldo = Column(BIGINT)

    # def __init__(self, renda_mensal, idade, nome_completo, celular, email, categoria, saldo):
    #     self.renda_mensal = renda_mensal
    #     self.idade = idade
    #     self.nome_completo = nome_completo
    #     self.celular = celular
    #     self.email = email
    #     self.categoria = categoria
    #     self.saldo = saldo

    def __repr__(self):
        return "<PessoaFisica(nome_completo='%s', celular='%s', email='%s', categoria='%s', saldo='%s')>" % (
            self.nome_completo, self.celular, self.email, self.categoria, self.saldo
        )
