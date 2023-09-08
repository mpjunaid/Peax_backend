from django.urls import path
from .views import (
    RegsiterView,
    LoginView,
    UserView,
    LogoutView,
    PlantsView,
    PlantAdd,
    PlantEditWithID,
)

urlpatterns = [
    path("register/", RegsiterView.as_view()),
    path("login/", LoginView.as_view()),
    path("user/", UserView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("plants/", PlantsView.as_view()),
    path("plantAdd/", PlantAdd.as_view()),
    path("plantEditWithId/", PlantEditWithID.as_view()),
]
