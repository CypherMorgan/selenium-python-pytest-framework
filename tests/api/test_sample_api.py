import allure
import json
from framework.api.api_client import APIClient


@allure.feature("User API")
@allure.story("Get Users List")
@allure.severity(allure.severity_level.CRITICAL)
def test_get_users(config):

    base_url = config.get("api", "base_url")

    with allure.step("Initialize API client"):
        client = APIClient(base_url=base_url)

    with allure.step("Send GET request to /users"):
        response = client.get("/users")
        response_json = response.json()

        allure.attach(
            json.dumps(response_json, indent=2),
            name="Response Body",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Validate response status code is 200"):
        assert response.status_code == 200

    with allure.step("Validate response contains 'users' key"):
        assert "users" in response_json

    with allure.step("Validate users is a list"):
        assert isinstance(response_json["users"], list)
        assert len(response_json["users"]) > 0