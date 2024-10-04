from sqlalchemy.orm.exc import NoResultFound
from src.models.sqllite.entities.people import People
from src.models.sqllite.entities.pets import Pets
from src.models.sqllite.interfaces.people_repository import PeopleRepositoryInterface


class PeopleRepository(PeopleRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        with self.__db_connection as database:
            try:
                person = People(first_name=first_name, last_name=last_name, age=age, pet_id=pet_id)
                database.session.add(person)
                database.session.commit()
            except Exception as exception:
                print(exception)
                database.session.rollback()
                raise exception
    def get_person(self, person_id: int) -> People:
        with self.__db_connection as database:
            try:
                person = (
                    database.session.query(People)
                    .outerjoin(Pets, People.pet_id == Pets.id)
                    .with_entities(
                        People.first_name, 
                        People.last_name,
                        Pets.name.label("pet_name"),
                        Pets.type.label("pet_type"),
                        )
                        .one()
                    )
                return person
            except NoResultFound:
                return None
