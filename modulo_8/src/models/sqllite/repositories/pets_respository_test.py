from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
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



def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(Pets)
    mock_connection.session.all.assert_called_once()
    assert len(response) == 2
    assert response[0].name == "Polly"
    assert response[1].name == "Zeca"
