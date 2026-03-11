import json


def get_login_test_data():

    with open("data/login_test_data.json") as f:
        data = json.load(f)

    return data["login_tests"]