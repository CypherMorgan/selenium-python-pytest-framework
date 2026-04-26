from fastapi import FastAPI

app = FastAPI()

users = {
    1: {"id": 1, "username": "john", "email": "john@example.com"}
}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return users.get(user_id, {"error": "User not found"})