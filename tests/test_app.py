import pytest
from app.app import create_app

@pytest.fixture()
def client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()

def test_home_returns_success_message(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Build Automation Demo Successful!" in resp.data

def test_health_endpoint(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json["status"] == "ok"

def test_add_helper_should_add_numbers():
    app = create_app()
    assert app.add(1, 2) == 3  