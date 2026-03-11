import pytest
from utilities.driver_factory import DriverFactory
from utilities.config_reader import ConfigReader
from utilities.screenshot import take_screenshot


@pytest.fixture(scope="class")
def driver():

    driver = DriverFactory.get_driver()

    config = ConfigReader()

    driver.get(config.get_base_url())

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
            
            if hasattr(report, "extra"):
                from pytest_html import extras
                report.extra.append(extras.image(screenshot_path))