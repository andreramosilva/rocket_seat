import pytest
from src.models.sqllite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Intereçao com o banco de dados")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(response)

@pytest.mark.skip(reason="Intereçao com o banco de dados")
def test_delete_pet():
    repo = PetsRepository(db_connection_handler)
    repo.delete_pet("Polly")
    
