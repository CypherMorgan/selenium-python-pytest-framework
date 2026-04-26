from framework.api.api_client import APIClient

def test_get_users():
    client = APIClient(base_url="https://dummyjson.com")

    response = client.get("/users")

    assert response.status_code == 200
    assert "users" in response.json()