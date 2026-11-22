from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_inicio():
    response = client.get("/")
    assert response.status_code == 200
    assert "Mercado de Flores de Acho" in response.json()["mensaje"]

def test_catalogo_visible():
    response = client.get("/catalogo")
    assert response.status_code == 200
    assert len(response.json()["productos"]) >= 3

def test_calculo_delivery_rimac():
    response = client.get("/delivery/Rimac")
    assert response.status_code == 200
    assert response.json()["costo_envio"] == 10.0