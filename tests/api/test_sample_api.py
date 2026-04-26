from framework.api.api_client import APIClient

def test_get_users(config):
    base_url = config.get("api", "base_url")

    client = APIClient(base_url=base_url)

    response = client.get("/users")

    assert response.status_code == 200
    assert "users" in response.json()