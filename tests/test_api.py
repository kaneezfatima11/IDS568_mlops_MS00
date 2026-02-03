import sys
from pathlib import Path

# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_predict():
    payload = {"features": [5.1, 3.5, 1.4, 0.2]}
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "prediction" in data
    assert isinstance(data["prediction"], int)
