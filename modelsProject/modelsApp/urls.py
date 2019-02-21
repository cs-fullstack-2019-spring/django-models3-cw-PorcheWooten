from . import views
from django.urls import path

# Create views
urlpatterns = [
    path("", views.newBook, name="index"),
    path("allBooks", views.allBooks, name="index"),
    path("greaterThan", views.greaterThan, name="index"),
    path("newCar", views.newCar, name="index"),
    path("greaterThanYear", views.greaterThanYear, name="index"),
    path("allCars", views.allCars, name="index"),
]