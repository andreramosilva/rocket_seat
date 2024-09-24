from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqllite.entities.pets import Pets
from .pets_repository import PetsRepository


class MockConnection:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data = [
                (
                    [mock.call.query(Pets)],
                    [
                        Pets(id=1, name="Polly", type="Dog"),
                        Pets(id=2, name="Zeca", type="Cat")
                    ]
                )
            ]
        )

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("NoResultFound")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(Pets)
    mock_connection.session.all.assert_called_once()
    assert len(response) == 2
    assert response[0].name == "Polly"
    assert response[1].name == "Zeca"

def test_list_pets_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(Pets)
    mock_connection.session.all.assert_not_called()
    assert len(response) == 0
    assert response == []
def test_delete_pet():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    repo.delete_pet("petName")

    mock_connection.session.query.assert_called_once_with(Pets)
    mock_connection.session.filter.assert_called_once_with(Pets.name == "petName")
    mock_connection.session.delete.assert_called_once()
    mock_connection.session.commit.assert_called_once()
    mock_connection.session.rollback.assert_not_called()
def test_delete_pet_error():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)
    with pytest.raises(NoResultFound):
        repo.delete_pet("petName")
    mock_connection.session.rollback.assert_called_once()
    