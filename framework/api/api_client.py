import requests

class APIClient:
    def __init__(self, base_url=None):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint, headers=None, params=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, headers=headers, params=params)
        return response

    def post(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, data=data, json=json, headers=headers)
        return response

    def put(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, data=data, json=json, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, headers=headers)
        return response