from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_customer():
    response = client.post(
        "/customers/",
        json={"name": "Test Customer", "email": "test@example.com"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Customer"
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_create_product():
    response = client.post(
        "/products/",
        json={
            "name": "Test Product",
            "price": 99.99,
            "description": "A test product"
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["price"] == 99.99
    assert data["description"] == "A test product"
    assert "id" in data
