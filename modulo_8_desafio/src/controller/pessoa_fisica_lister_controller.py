from src.repository.pessoa_fisica_repository import PessoaFisicaRepository
from src.models.sqllite.entities.pessoa_fisica import PessoaFisica

class PessoaFisicaListerController:
    def __init__(self, pessoa_fisica_repository :  PessoaFisicaRepository):
        self.pessoa_fisica_repository = pessoa_fisica_repository

    def list(self):

        return self.pessoa_fisica_repository.list()

    def __format_response(self, List[PessoaFisica]) -> dict:
        return {
            "data": { 
                "type": "pessoa_fisica",

            }
        }
