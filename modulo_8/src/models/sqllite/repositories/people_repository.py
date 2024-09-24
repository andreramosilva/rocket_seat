from src.models.sqllite.entities.people import People

class PeopleRepository:
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