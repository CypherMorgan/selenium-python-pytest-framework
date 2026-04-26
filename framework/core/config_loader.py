import yaml
import os

class ConfigLoader:
    def __init__(self, env="dev"):
        self.env = env
        self.config = self.load_config()

    def load_config(self):
        file_path = os.path.join("config", f"{self.env}.yaml")
        with open(file_path, "r") as file:
            return yaml.safe_load(file)

    def get(self, section, key):
        return self.config.get(section, {}).get(key)