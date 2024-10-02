from sqlalchemy import Column, Integer, String , BIGINT, ForeignKey
from src.models.sqllite.settings.base import base


class PessoaJuridica(base):
    __tablename__ = 'pessoa_juridica'

    id = Column(Integer, primary_key=True)
    faturamento = Column(BIGINT)
    idade = Column(Integer)
    nome_fantasia = Column(String)
    celular = Column(String)
    email_corporativo = Column(String)
    categoria = Column(String)
    saldo = Column(BIGINT)

    # def __init__(self, faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo):
    #     self.faturamento = faturamento
    #     self.idade = idade
    #     self.nome_fantasia = nome_fantasia
    #     self.celular = celular
    #     self.email_corporativo = email_corporativo
    #     self.categoria = categoria
    #     self.saldo = saldo

    def __repr__(self):
        return "<PessoaJuridica(nome_fantasia='%s', celular='%s', email_corporativo='%s', categoria='%s', saldo='%s')>" % (
            self.nome_fantasia, self.celular, self.email_corporativo, self.categoria, self.saldo
        )
