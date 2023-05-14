from bson.objectid import ObjectId
from BackLogic.settings import JWT_SECRET, JWT_ALGORITHM, workers, pwd_context
import jwt


def user(id):
    print("hello")
    employer = workers.find_one({"_id": ObjectId(f"{id}")})
    if employer is not None:
        name = employer["name"]
        last_works = employer["experiense"]
        description = employer["description"]
        email = employer["email"]
        living_place = employer["place_live"]
        skills = employer["skills"]
        print(name, last_works, description, email, living_place, skills)
        return employer
    else:
        return "there is no user with this id"


def login(email, password):
    user = workers.find_one({"email": email})
    if user is None:
        return "User not found"

    hashed_password = user["password"]
    if pwd_context.verify(password, hashed_password):
        jwt_payload = {"email": email}
        jwt_token = jwt.encode(jwt_payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return "Correct password, you logged in"
    else:
        return "Incorrect password"
