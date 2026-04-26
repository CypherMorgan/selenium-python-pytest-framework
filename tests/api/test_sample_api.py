import allure
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

        allure.attach(
            str(response.json()),
            name="Response Body",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Validate response status code is 200"):
        assert response.status_code == 200

    with allure.step("Validate response contains 'users' key"):
        assert "users" in response.json()