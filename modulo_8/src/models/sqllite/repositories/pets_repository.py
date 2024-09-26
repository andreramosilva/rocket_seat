from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqllite.entities.pets import Pets
from src.models.sqllite.interfaces.pets_repository import PetsRepositoryInterface


class PetsRepository(PetsRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection


    def list_pets(self) -> List[Pets]:
        with self.__db_connection as database:
            try:
                pets = database.session.query(Pets).all()
                return pets
            except NoResultFound:
                return []
            
    def delete_pet(self, pet_name: int) -> None:
        with self.__db_connection as database:
            try:
                (database.session.query(Pets)
                    .filter(Pets.name == pet_name)
                    .delete()
                )
                database.session.commit()
                # pet = database.session.query(Pets).filter(Pets.name == pet_name).one()
                # database.session.delete(pet)
                # database.session.commit()
            except Exception as e:
                print(e)
                database.session.rollback()
                raise e