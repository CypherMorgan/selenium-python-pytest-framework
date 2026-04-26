import pytest
from pages.login_page import LoginPage
from framework.core.data_reader import get_login_test_data
from framework.utils.logger import get_logger

logger = get_logger("LoginTest")

test_data = get_login_test_data()


@pytest.mark.parametrize("data", test_data)
def test_login(driver, data):

    login_page = LoginPage(driver)

    username = data["username"]
    password = data["password"]
    expected = data["expected"]

    logger.info(f"Testing login with user: '{username}'")
    logger.info(
        f"Test data -> username: '{username}', password: '{password}', expected: '{expected}'"
    )

    try:
        logger.info("Entering username")
        login_page.enter_username(username)

        logger.info("Entering password")
        login_page.enter_password(password)

        logger.info("Clicking login button")
        login_page.click_login()

        message = login_page.get_message().lower().replace("×", "").strip()

        logger.info(f"Login response message: '{message}'")

        if expected == "success":

            assert "secure area" in message, (
                f"\nLogin expected SUCCESS but failed.\n"
                f"Username: '{username}'\n"
                f"Password: '{password}'\n"
                f"Actual message: '{message}'"
            )

            logger.info("Login success validated")

        else:

            assert "invalid" in message, (
                f"\nLogin expected FAILURE but passed.\n"
                f"Username: '{username}'\n"
                f"Password: '{password}'\n"
                f"Actual message: '{message}'"
            )

            logger.info("Login failure validated")

    except Exception as e:
        logger.error(f"Test execution failed due to error: {str(e)}")
        raise