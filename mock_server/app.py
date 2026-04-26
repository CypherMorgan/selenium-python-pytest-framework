from fastapi import FastAPI

app = FastAPI()

users = {
    1: {"id": 1, "username": "john", "email": "john@example.com"},
    2: {"id": 2, "username": "alice", "email": "alice@example.com"},
}


@app.get("/users")
def get_all_users():
    return {"users": list(users.values())}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return users.get(user_id, {"error": "User not found"})