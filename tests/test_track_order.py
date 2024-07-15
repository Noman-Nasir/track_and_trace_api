from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_track_order():
    response = client.get("/api/track/TN12345680")
    assert response.status_code == 200
    response = response.json()

    assert response["articles"] == [
        {"sku": "KB012", "name": "Keyboard", "price": 50.0, "quantity": 1},
        {"sku": "MO456", "name": "Mouse", "price": 25.0, "quantity": 1}
    ]
    assert response["status"] == "delivery"
    # Just make sure we have both data points. We don"t need to check values as they change based on weather.
    assert len(response["weather"]) == 2


def test_track_order_invalid():
    response = client.get("/api/track/invalid_id")
    assert response.status_code == 404
    assert response.json() == {"detail": [{"msg": "Order not found"}]}
