import random
import string
import allure
from scooter_api import ScooterApi


class Helpers:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    @allure.step("Создание случайных данных для создания курьера")
    def create_random_courier_data_for_registration():
        return {
            "login": Helpers.generate_random_string(10),
            "password": Helpers.generate_random_string(10),
            "firstName": Helpers.generate_random_string(10)
        }

    @staticmethod
    @allure.step("Получение id курьера по его данным")
    def get_courier_id(courier_data):
        login_response = ScooterApi.login_courier(courier_data)

        if login_response.status_code == 200:
            return login_response.json()["id"]

    @staticmethod
    @allure.step("Получение id заказа по трэк-номеру")
    def get_order_id(track_id):
        order_response = ScooterApi.order_info(track_id)

        if order_response.status_code == 200:
            return order_response.json()["order"]["id"]

    @staticmethod
    @allure.step("Удаление курьера по его данным")
    def delete_courier_if_exists(courier_data):
        courier_id = Helpers.get_courier_id(courier_data)

        if courier_id is not None:
            ScooterApi.delete_courier(courier_id)
