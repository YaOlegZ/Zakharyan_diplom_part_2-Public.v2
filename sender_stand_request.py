# Олег Захарян, 12-я когорта — Финальный проект. Инженер по тестированию плюс

import requests
import configuration
import data


# создание заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=body)


# получение заказа по номеру
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response


# тест
def test_order_creation():
    response = create_order(data.order_body)

    track_number = response.json()["track"]
    print("Номер заказа:", track_number)

# получение заказа по номеру
    order_response = get_order(track_number)

# проверка статуса
    assert order_response.status_code == 200
    order_data = order_response.json()
    print (order_data)
