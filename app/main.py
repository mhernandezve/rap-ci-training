from fastapi import Depends, FastAPI, Header, HTTPException
from app.routers import items

app = FastAPI()

app.include_router(items.router)
