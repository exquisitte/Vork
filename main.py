from fastapi import FastAPI
from BackLogic.find_user_db import user

app = FastAPI()


@app.get("/{worker_id}")
async def find_user(worker_id: str):
    user(worker_id)
