# Олег Захарян, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request


# тест
def test_order_creation():
    response = sender_stand_request.create_order(data.order_body)
    track_number = response.json()["track"]

# получение заказа по номеру
    order_response = sender_stand_request.get_order(track_number)

# проверка статуса
    assert order_response.status_code == 200
