import requests
from framework.utils.logger import get_logger

logger = get_logger("APIClient")


class APIClient:

    def __init__(self, base_url=None):
        self.base_url = base_url
        self.session = requests.Session()
        logger.info(f"Initialized APIClient with base_url: {self.base_url}")

    def get(self, endpoint, headers=None, params=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET Request → {url} | params={params}")

        response = self.session.get(url, headers=headers, params=params)

        logger.info(f"Response Status → {response.status_code}")
        return response

    def post(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST Request → {url} | data={data} json={json}")

        response = self.session.post(url, data=data, json=json, headers=headers)

        logger.info(f"Response Status → {response.status_code}")
        return response

    def put(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT Request → {url}")

        response = self.session.put(url, data=data, json=json, headers=headers)

        logger.info(f"Response Status → {response.status_code}")
        return response

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE Request → {url}")

        response = self.session.delete(url, headers=headers)

        logger.info(f"Response Status → {response.status_code}")
        return response