from framework.db.db_client import DBClient


def test_user_in_db():

    db = DBClient("test_data/test.db")
    db.connect()

    result = db.execute_query(
        "SELECT username, email FROM users WHERE username = ?",
        ("john",)
    )

    db.close()

    assert result[0][0] == "john"
    assert result[0][1] == "john@example.com"