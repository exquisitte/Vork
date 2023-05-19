import pymongo
import secrets
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

client = pymongo.MongoClient("mongodb+srv://Maksym:iDvvTab5zSPl6jlb@workingcluster.fzwnrkr.mongodb.net/platform_users?retryWrites=true&w=majority")
db = client.platform_users
workers = db["workers"]
vacancies = db["vacancies"]

JWT_ALGORITHM = "HS256"
JWT_EXPIRATION = 3600

DOMAIN = "dev-mrtvgnwzwl7w6105.eu.auth0.com"
API_AUDIENCE = "https://fastapi-login.com/"
ISSUER = "https://dev-mrtvgnwzwl7w6105.eu.auth0.com"
ALGORITHMS = "HS256"
JWT_SECRET = "5a43b01a6e1e22d7b945cd5b4158dbf5e9e4e7fa68f87a8dafe26f73d291d7f"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")

