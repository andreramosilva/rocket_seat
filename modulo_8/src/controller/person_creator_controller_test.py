import pytest
from .person_creator_controller import PersonCreatorController

class MockPeopleRepository:
    def insert_person(self, first_name, last_name, age, pet_id):
        pass


def test_create():
    person_info = {
        'first_name' : 'John',
        'last_name' : 'Doe',
        'age' : 25,
        'pet_id' : 1
    }

    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create_person(person_info)
    assert response["data"]["type"] == "person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_info

def test_create_error():
    person_info = {
        'first_name' : 'John12131',
        'last_name' : 'Doe',
        'age' : 25,
        'pet_id' : 1
    }

    controller = PersonCreatorController(MockPeopleRepository())

    with pytest.raises(Exception) as e:
        controller.create_person(person_info)
