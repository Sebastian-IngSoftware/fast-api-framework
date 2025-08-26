from fastapi import FastAPI
from routes.web import router

app = FastAPI()
app.include_router(router)
