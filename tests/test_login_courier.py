import allure
from data import TextConstants
from helper import Helpers
from scooter_api import ScooterApi


class TestLoginCourier:

    @allure.title('Проверка успешной авторизации курьера')
    @allure.description('Проверяем успешную авторизацию курьера с указанием всех обязательных полей')
    def test_success_courier_login(self, random_courier_data_for_registration):
        ScooterApi.registration_courier(random_courier_data_for_registration)
        response_login = ScooterApi.login_courier(random_courier_data_for_registration)
        assert response_login.status_code == 200 and response_login.json()["id"] is not None

    @allure.title('Проверка авторизации курьера с неправильно указанным логином')
    @allure.description('Проверяем, что при указании неверного логина, но правильного пароля, невозможно авторизоваться в системе')
    def test_courier_login_with_wrong_login(self,random_courier_data_for_registration):
        ScooterApi.registration_courier(random_courier_data_for_registration)
        another_courier_login = {
            "login": Helpers.generate_random_string(10),
            "password": random_courier_data_for_registration["password"]
        }
        response_login = ScooterApi.login_courier(another_courier_login)
        assert response_login.status_code == 404 \
               and response_login.json()["message"] == TextConstants.error_login_not_found

    @allure.title('Проверка авторизации без указания обязательного поля "логин"')
    @allure.description('Проверяем, что если не указать обязательное поле "логин", невозможно авторизоваться в системе')
    def test_without_login(self, random_courier_data_for_registration):
        ScooterApi.registration_courier(random_courier_data_for_registration)
        courier_without_password = {
            "password": random_courier_data_for_registration["password"]
        }
        response_login = ScooterApi.login_courier(courier_without_password)
        assert response_login.status_code == 400 \
               and response_login.json()["message"] == TextConstants.error_not_enough_data_for_login

    @allure.title('Проверка авторизации под несуществующим пользователем')
    @allure.description('Проверяем, что невозможно авторизоваться под несуществующим пользователем')
    def test_courier_login_without_registration(self,random_courier_data_for_registration):
        response_login = ScooterApi.login_courier(random_courier_data_for_registration)
        assert response_login.status_code == 404 \
               and response_login.json()["message"] == TextConstants.error_login_not_found
