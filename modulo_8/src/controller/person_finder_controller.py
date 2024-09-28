from typing import Dict, List
from src.models.sqllite.interfaces.people_repository import PeopleRepositoryInterface
from src.models.sqllite.entities.people import People
from .interfaces.person_finder_controller import PersonFinderControllerInterface

class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, person_finder : PeopleRepositoryInterface) -> None:
        self.person_finder = person_finder

    def find(self, person_id) -> List[Dict]:
        person = self.__find_person_into_db(person_id)
        response = self.__format_response(person)
        return response

    def __find_person_into_db(self, person_id : id) -> People:
        person = self.person_finder.get_person(person_id)
        if not person:
            raise Exception('Person not found')
        return person

    def __format_response(self, person : People) -> Dict:
        return {
            "data": {
                "type": "person",
                "count": 1,
                "attributes": { 
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "pet_name": person.pet_name,
                    "pet_type": person.pet_type
                }
            }
        }
