import sqlite3
from framework.utils.logger import get_logger

logger = get_logger("DBClient")


class DBClient:

    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        logger.info(f"Connecting to DB: {self.db_path}")
        self.connection = sqlite3.connect(self.db_path)

    def execute_query(self, query, params=None):
        logger.info(f"Executing query: {query} | params={params}")

        cursor = self.connection.cursor()
        cursor.execute(query, params or [])

        result = cursor.fetchall()

        logger.info(f"Query result: {result}")
        return result

    def close(self):
        if self.connection:
            logger.info("Closing DB connection")
            self.connection.close()