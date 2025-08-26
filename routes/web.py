
from fastapi import APIRouter
from app.http.controllers.home_controller import HomeController

router = APIRouter()

@router.get("/")
def read_root():
    return HomeController.index()
