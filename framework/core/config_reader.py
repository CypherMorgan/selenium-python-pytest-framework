import json


class ConfigReader:

    def __init__(self):
        with open("config/config.json") as file:
            self.config = json.load(file)

    def get_base_url(self):
        return self.config["base_url"]

    def get_browser(self):
        return self.config["browser"]

    def get_implicit_wait(self):
        return self.config["implicit_wait"]

    def is_headless(self):
        return self.config["headless"]