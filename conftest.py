import allure
import pytest
from framework.core.driver_factory import DriverFactory
from framework.core.config_loader import ConfigLoader
from framework.utils.screenshot import take_screenshot


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against"
    )


@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    return ConfigLoader(env)


@pytest.fixture(scope="class")
def driver(config):
    driver = DriverFactory.get_driver(config)

    base_url = config.get("app", "base_url")
    driver.get(base_url)

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            screenshot_path = take_screenshot(driver, item.name)

            print(f"\nScreenshot saved at: {screenshot_path}")

            allure.attach.file(
                screenshot_path,
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            if hasattr(report, "extra"):
                from pytest_html import extras
                report.extra.append(extras.image(screenshot_path))