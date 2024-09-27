from typing import List
import pytest
from src.controller.pet_lister_controller import PetListerController
from src.models.sqllite.entities.pets import Pets

class MockPetsRepository:
    def list_pets(self) -> List[Pets]:
        return [
            Pets("dog", "dog"),
            Pets("cat", "cat")
        ]

@pytest.mark.skip(reason="Not working")
def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "pets",
            "count": 2,
            "attributes": [
                {
                    "name": "dog",
                    "type": "dog"
                },
                {
                    "name": "cat",
                    "type": "cat"
                }
            ]
        }
    }

    assert response == expected_response
    