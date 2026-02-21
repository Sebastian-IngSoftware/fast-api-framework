
from fastapi import APIRouter
from app.http.controllers.home_controller import HomeController
from app.http.controllers.naive_bayes_controller import NaiveBayesController
from app.schemas.naive_bayes_schema import NaiveBayesInput, NaiveBayesPrediction

router = APIRouter()

@router.get("/")
def read_root():
    return HomeController.index()

@router.post("/naive-bayes", response_model=NaiveBayesPrediction)
def naive_bayes_predict(data: NaiveBayesInput):
    return NaiveBayesController.predict(data)
