from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from main import app
from asiaYo.order.order_services import OrderService

client = TestClient(app)


def test_order_process_success():
    # 測試 OrderService 在正常情況下的行為
    order_service = OrderService(validators=[MagicMock()], transformers=[MagicMock()])
    order_service.validators[0].validate.return_value = None  # 无异常
    order_service.transformers[0].transform.return_value = None  # 无异常

    # 測試正確 Case
    normal_order_data = {
        "id": "A0000001",
        "name": "Name",
        "address": {
            "city": "taipei-city",
            "district": "da-an-district",
            "street": "fuxing-south-road",
        },
        "price": "100",
        "currency": "TWD",
    }
    response = client.post("/api/orders", json=normal_order_data)

    assert response.status_code == 200


def test_order_process_failure():
    # 測試 OrderService 在遇到問題時的行為
    order_service = OrderService(validators=[MagicMock()], transformers=[MagicMock()])
    order_service.validators[0].validate.side_effect = ValueError("Invalid order")

    # 測試異常 Case
    bad_order_data = {}
    response = client.post("/api/orders", json=bad_order_data)

    assert response.status_code == 422
