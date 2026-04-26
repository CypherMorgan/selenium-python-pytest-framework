import allure
import pytest
from framework.core.driver_factory import DriverFactory
from framework.core.config_loader import ConfigLoader
from framework.utils.screenshot import take_screenshot
from framework.utils.logger import get_logger

logger = get_logger("TestRunner")


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against"
    )

    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser to run tests on (chrome/firefox)"
    )


@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    browser_override = request.config.getoption("--browser")

    logger.info(f"Running tests on environment: {env}")

    config = ConfigLoader(env)

    if browser_override:
        logger.info(f"Overriding browser to: {browser_override}")
        config.config["browser"]["name"] = browser_override

    return config


@pytest.fixture(scope="class")
def driver(config):
    logger.info("Initializing WebDriver")

    driver = DriverFactory.get_driver(config)

    base_url = config.get("app", "base_url")
    logger.info(f"Opening URL: {base_url}")

    driver.get(base_url)

    yield driver

    logger.info("Quitting WebDriver")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        logger.error(f"Test FAILED: {item.name}")

        driver = item.funcargs.get("driver")

        if driver:
            screenshot_path = take_screenshot(driver, item.name)

            allure.attach.file(
                screenshot_path,
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            if hasattr(report, "extra"):
                from pytest_html import extras
                report.extra.append(extras.image(screenshot_path))