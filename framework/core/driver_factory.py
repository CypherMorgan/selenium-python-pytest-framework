from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(config):
        browser = config.get("browser", "name")
        headless = config.get("browser", "headless")
        implicit_wait = config.get("browser", "implicit_wait")

        if browser == "chrome":
            options = webdriver.ChromeOptions()

            if headless:
                options.add_argument("--headless")

            options.add_argument("--start-maximized")

            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=options
            )

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()

            if headless:
                options.add_argument("--headless")

            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )

        else:
            raise Exception(f"Browser '{browser}' not supported")

        driver.implicitly_wait(implicit_wait)

        return driver