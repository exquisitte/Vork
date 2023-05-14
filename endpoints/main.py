from fastapi import FastAPI
from Login_Registration.find_user_db import user, login
from Login_Registration.add_employer import add_worker
from models.models import User_reg, User_login
from fastapi import Depends, Response, status
from fastapi.security import HTTPBearer
from utils import VerifyToken
import uvicorn

app = FastAPI()

token_auth_schema = HTTPBearer()


@app.get("/employers/{worker_id}")
async def find_user(worker_id: str, response: Response, token: str = Depends(token_auth_schema)):
    result = VerifyToken(token.credentials).verify()
    if result.get("status"):
        response.status_code = status.HTTP_404_NOT_FOUND
        return result

    user(worker_id)


@app.post("/registration/")
async def creating(user: User_reg):

    add_worker(
        user.email,
        user.exp,
        user.name,
        user.skills,
        user.description,
        user.living_place,
        user.password,
    )

    return {"msg": "User registered successfully"}

@app.post("/login")
async def user_login(user1: User_login):
    return login(user1.email, user1.password)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
