from fastapi.testclient import TestClient

from app.app import app

client = TestClient(app)


def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_predict_valid_payload():
    r = client.post("/predict", json={"features": [1.0, 2.5, 3.5]})
    assert r.status_code == 200
    body = r.json()
    assert "prediction" in body
    assert body["prediction"] == 7.0


def test_predict_invalid_payload_missing_features():
    r = client.post("/predict", json={})
    # FastAPI/Pydantic validation error
    assert r.status_code in (400, 422)
