import pytest
from src.models.sqllite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

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

@pytest.mark.skip(reason="Intereçao com o banco de dados")
def test_insert_person():
    first_name = "John"
    last_name = "Doe"
    age = 30
    pet_id = 1
    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)

@pytest.mark.skip(reason="Intereçao com o banco de dados")
def test_get_person():
    person_id = 1
    repo = PeopleRepository(db_connection_handler)
    response = repo.get_person(person_id)
    print()
    print(response)
    print(response.pet_name)