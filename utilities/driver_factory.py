from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utilities.config_reader import ConfigReader


class DriverFactory:

    @staticmethod
    def get_driver():

        config = ConfigReader()

        browser = config.get_browser()

        if browser == "chrome":

            options = webdriver.ChromeOptions()

            if config.is_headless():
                options.add_argument("--headless")

            options.add_argument("--start-maximized")

            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()),
                options=options
            )

        else:
            raise Exception(f"Browser '{browser}' not supported")

        driver.implicitly_wait(config.get_implicit_wait())

        return driver