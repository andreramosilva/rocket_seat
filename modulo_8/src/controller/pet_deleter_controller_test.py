from src.controller.pet_deleter_controller import PetDeleterController

def test_delete_pet(mocker):
    pet_repository = mocker.Mock()
    controller = PetDeleterController(pet_repository)
    controller.delete_pet("name")

    pet_repository.delete_pet.assert_called_once_with("name")
