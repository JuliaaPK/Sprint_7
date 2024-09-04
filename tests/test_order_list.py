import allure
from data import OrderCreation
from helper import Helpers
from scooter_api import ScooterApi


class TestOrderList:
    @allure.title('Проверка получения списка заказов')
    @allure.description('Проверяем, что после успешного создания заказа и привязки его к курьеру, выводится список всех заказов')
    def test_create_orders_and_get_list_of_orders(self, random_courier_data_for_registration):
        ScooterApi.registration_courier(random_courier_data_for_registration)
        courier_id = Helpers.get_courier_id(random_courier_data_for_registration)
        order_ids = []

        for order_data in OrderCreation.values:
            response_creation_order = ScooterApi.order_creation(order_data)
            track_id = response_creation_order.json()["track"]
            order_id = Helpers.get_order_id(track_id)
            ScooterApi.accept_order(order_id, courier_id)
            order_ids.append(order_id)

        order_list_response = ScooterApi.order_list({"courierId": courier_id})
        order_list = order_list_response.json()["orders"]

        orders_exists = 0

        for order_id in order_ids:
            for order in order_list:
                if order["id"] == order_id:
                    orders_exists += 1
                    break

        assert order_list_response.status_code == 200 and orders_exists == len(order_ids)
