import allure
import pytest
from data import OrderCreation
from scooter_api import ScooterApi


class TestOrderCreation:
    @allure.title('Проверка создания заказов с необязательным полем "color"')
    @allure.description('Проверяем успешное создание заказа с вариациями поля "color"')
    @pytest.mark.parametrize(OrderCreation.parameters, OrderCreation.values)
    def test_creation_order_with_and_without_color(self, order_data):
        response_creation = ScooterApi.order_creation(order_data)
        track_id = response_creation.json()["track"]

        assert response_creation.status_code == 201 and track_id is not None
