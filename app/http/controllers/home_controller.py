from fastapi import APIRouter

class HomeController:
    @staticmethod
    def index():
        return {"message": "¡FastAPI Framework Test!"}
