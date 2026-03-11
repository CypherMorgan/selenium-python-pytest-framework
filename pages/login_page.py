from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage:

    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    message_box = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver


    def enter_username(self, username):

        try:
            element = self.driver.find_element(*self.username_input)
            element.clear()
            element.send_keys(username)

        except NoSuchElementException:
            raise Exception("Username input field not found on login page")


    def enter_password(self, password):

        try:
            element = self.driver.find_element(*self.password_input)
            element.clear()
            element.send_keys(password)

        except NoSuchElementException:
            raise Exception("Password input field not found on login page")


    def click_login(self):

        try:
            self.driver.find_element(*self.login_button).click()

        except NoSuchElementException:
            raise Exception("Login button not found on login page")


    def get_message(self):

        try:
            return self.driver.find_element(*self.message_box).text

        except NoSuchElementException:
            raise Exception("Login result message element not found")