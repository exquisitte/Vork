from fastapi.security import HTTPBearer
from passlib.context import CryptContext
from BackLogic.settings import workers, pwd_context

token_auth_scheme = HTTPBearer()


def add_worker(email, experiense, name, skills, description, place_live, password):
    workers.insert_one({
        "email": email,
        "experiense": experiense,
        "name": name,
        "skills": skills,
        "place_live": place_live,
        "description": description,
        "password": pwd_context.hash(password),
    })

