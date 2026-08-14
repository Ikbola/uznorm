from fastapi.testclient import TestClient

from uznorm.api import app

client = TestClient(app)

OQ_GQ = "\u02bb"
TUTUQ = "\u02bc"


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_normalize_returns_corrected_text():
    response = client.post("/normalize", json={"text": "O'zbekiston"})
    assert response.status_code == 200
    data = response.json()
    assert data["normalized"] == f"O{OQ_GQ}zbekiston"
    assert data["changed"] is True


def test_unchanged_text_reports_no_change():
    response = client.post("/normalize", json={"text": "Toshkent shahri"})
    assert response.json()["changed"] is False


def test_missing_text_field_is_rejected():
    response = client.post("/normalize", json={})
    assert response.status_code == 422