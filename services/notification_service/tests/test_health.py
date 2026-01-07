from fastapi.testclient import TestClient

from services.notification_service.app.main import create_app


def test_health() -> None:
    client = TestClient(create_app())
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["service"]
