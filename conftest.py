import pytest
from helper import Helpers


@pytest.fixture()
def random_courier_data_for_registration():
    random_courier_data = Helpers.create_random_courier_data_for_registration()
    yield random_courier_data
    Helpers.delete_courier_if_exists(random_courier_data)
