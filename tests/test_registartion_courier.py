import allure
from data import TextConstants
from helper import Helpers
from scooter_api import ScooterApi


class TestRegistrationCourier:

    @allure.title('Проверка успешной регистрации курьера')
    @allure.description('Проверяем успешную регистрацию курьера с указанием всех обязательных полей')
    def test_successful_registration(self, random_courier_data_for_registration):
        registration_response = ScooterApi.registration_courier(random_courier_data_for_registration)

        assert registration_response.status_code == 201 and registration_response.json()["ok"] is True

    @allure.title('Проверка повторной регистрации курьера с одинаковыми полями')
    @allure.description('Проверяем, что нельзя создать двух одинаковых курьеров')
    def test_registration_two_same_couriers(self, random_courier_data_for_registration):
        ScooterApi.registration_courier(random_courier_data_for_registration)
        response_registration = ScooterApi.registration_courier(random_courier_data_for_registration)
        assert response_registration.status_code == 409 \
               and response_registration.json()["message"] == TextConstants.error_repeat_reg_courier

    @allure.title('Проверка регистрации без указания обязательного поля "пароль"')
    @allure.description('Проверяем, что нельзя зарегистрироваться  без указания одного из обязательных полей')
    def test_without_password_field_for_registration(self, random_courier_data_for_registration):
        courier_data_with_only_login = {
            "login": random_courier_data_for_registration["login"]
        }
        response_registration = ScooterApi.registration_courier(courier_data_with_only_login)

        assert response_registration.status_code == 400 \
               and response_registration.json()["message"] == TextConstants.error_not_enough_data_for_reg

    @allure.title('Проверка регистрации с указанием существующего логина ')
    @allure.description('Проверяем, что нельзя зарегистрироватья с указанием логина, который ранее использовался при регистрации')
    def test_registration_courier_with_same_login(self, random_courier_data_for_registration):
        ScooterApi.registration_courier(random_courier_data_for_registration)
        courier_with_same_login = {
            "login": random_courier_data_for_registration["login"],
            "password": Helpers.generate_random_string(10)
        }
        response_registration = ScooterApi.registration_courier(courier_with_same_login)
        assert response_registration.status_code == 409 \
               and response_registration.json()["message"] == TextConstants.error_repeat_reg_courier
