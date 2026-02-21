
from fastapi import APIRouter
from app.http.controllers.home_controller import HomeController
from app.http.controllers.naive_bayes_controller import NaiveBayesController
from app.models.naive_bayes import NaiveBayesRequest, NaiveBayesResponse

router = APIRouter()

@router.get("/")
def read_root():
    return HomeController.index()

@router.post("/naive-bayes", response_model=NaiveBayesResponse)
def naive_bayes_predict(request: NaiveBayesRequest):
    return NaiveBayesController.predict(request)
