from BackLogic.settings import JWT_SECRET, JWT_ALGORITHM, vacancies
from fastapi import FastAPI, Depends, Response, status, HTTPException
from fastapi.security import HTTPBearer
from Login_Registration.find_user_db import user, login
from Login_Registration.add_employer import add_worker
from Models.models import User_reg, User_login, Vacancions, Token, Filters
from utils import VerifyToken
from Vacancion_Logic.works import add_work, vacancion_aplication
from JWT_operations.JWT_OP import create_access_token
import uvicorn

filters = {}

app = FastAPI()

token_auth_schema = HTTPBearer()


@app.get("/employer/{worker_id}/")
async def find_user(worker_id: str, response: Response, token: str = Depends(token_auth_schema)):
    result = VerifyToken(token.credentials).verify(JWT_SECRET, JWT_ALGORITHM)
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
    result = login(user1.email, user1.password)
    if result == "Correct password, you logged in":
        jwt_payload = {"email": user1.email}
        jwt_token = create_access_token(jwt_payload)
        return Token(access_token=jwt_token, token_type="bearer")
    else:
        return result


# Функция зависимости для проверки и декодирования токена
def verify_token(token: HTTPBearer = Depends(token_auth_schema)):
    decoded_token = VerifyToken(token.credentials).verify(JWT_SECRET, JWT_ALGORITHM)
    if decoded_token.get("status"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token or authentication required",
        )
    return decoded_token


@app.post("/work/create")
def work_creating(
    response: Response,
    work: Vacancions,
    decoded_token: dict = Depends(verify_token)
):
    add_work(
        work.employee_email,
        work.city,
        work.company_name,
        work.description,
        work.vacancion_name,
        work.money,
        work.employment_type,
        work.needed_experience
    )
    return decoded_token


@app.get("/work/{work_id}")
async def application(
    work_id: str,
    response: Response,
    decoded_token: dict = Depends(verify_token)
):
    vacancion_aplication(work_id, decoded_token["email"])


@app.post("/work/")
def get_filtered_items(filt: Filters):
    query = {
        "min_money": {"$gte": filt.min_money},
        "max_money": {"$lte": filt.max_money},
        **{k: v for k, v in filt.dict().items() if v is not None}
    }

    items = vacancies.find(query)
    return items

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
