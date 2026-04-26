from framework.api.api_client import APIClient
from framework.db.db_client import DBClient
from framework.utils.logger import get_logger

logger = get_logger("APIDBTest")


def test_api_user_matches_db(config):

    base_url = config.get("api", "base_url")
    client = APIClient(base_url)

    logger.info("Fetching user from API")
    response = client.get("/users/1")

    assert response.status_code == 200

    api_data = response.json()
    logger.info(f"API Response: {api_data}")

    db = DBClient("test_data/test.db")
    db.connect()

    logger.info("Fetching user from DB")
    db_data = db.execute_query(
        "SELECT username, email FROM users WHERE id = ?",
        (1,)
    )

    db.close()

    logger.info(f"DB Data: {db_data}")

    assert api_data["username"] == db_data[0][0]
    assert api_data["email"] == db_data[0][1]