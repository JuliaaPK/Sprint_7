# Данные для создания заказов
class OrderCreation:
    parameters = 'order_data'
    values = [
        {
            "firstName": "Marcus",
            "lastName": "Marcus1",
            "address": "address",
            "metroStation": 4,
            "phone": "+7 111 111 11 11",
            "rentTime": 5,
            "deliveryDate": "2024-09-15",
            "comment": "no comment",
            "color": [
                "BLACK"
            ]
        },
        {
            "firstName": "Marcus12",
            "lastName": "Marcus122",
            "address": "address1",
            "metroStation": 5,
            "phone": "+7 222 222 22 22",
            "rentTime": 5,
            "deliveryDate": "2024-09-20",
            "comment": "no comment",
            "color": [
                "BLACK", "GRAY"
            ]
        },
        {
            "firstName": "Marcus13",
            "lastName": "Marcus123",
            "address": "address2",
            "metroStation": 10,
            "phone": "+7 333 333 33 33",
            "rentTime": 5,
            "deliveryDate": "2024-09-25",
            "comment": "no comment",
            "color": []
        }
    ]

# Ошибки, возникающие при обработке запросов
class TextConstants:
    error_repeat_reg_courier = "Этот логин уже используется. Попробуйте другой."
    error_not_enough_data_for_reg = "Недостаточно данных для создания учетной записи"
    error_login_not_found = "Учетная запись не найдена"
    error_not_enough_data_for_login = "Недостаточно данных для входа"