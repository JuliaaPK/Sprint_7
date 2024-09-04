import requests
from urls import Urls


class ScooterApi:

    @staticmethod
    def registration_courier(courier_data):
        return requests.post(Urls.BASE_URL + Urls.COURIER_REGISTRATION_ENDPOINT, json=courier_data)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(Urls.BASE_URL + Urls.COURIER_REGISTRATION_ENDPOINT + f"/{courier_id}")

    @staticmethod
    def login_courier(courier_data):
        return requests.post(Urls.BASE_URL + Urls.COURIER_LOGIN_ENDPOINT, json=courier_data)

    @staticmethod
    def order_creation(order_datas):
        return requests.post(Urls.BASE_URL + Urls.ORDER_CREATION_ENDPOINT, json=order_datas)

    @staticmethod
    def order_info(track_id):
        return requests.get(Urls.BASE_URL + Urls.ORDER_CREATION_ENDPOINT + f"/track?t={track_id}")

    @staticmethod
    def accept_order(order_id, courier_id):
        return requests.put(Urls.BASE_URL + Urls.ORDER_ACCEPT_ENDPOINT + f"/{order_id}?courierId={courier_id}")

    @staticmethod
    def order_list(params):
        params_array = []

        for key in params:
            params_array.append(f"{key}={params[key]}")

        return requests.get(Urls.BASE_URL + Urls.ORDER_CREATION_ENDPOINT + f"?{'&'.join(params_array)}")
