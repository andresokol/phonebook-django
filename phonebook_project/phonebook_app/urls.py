from django.urls import path
from . import views

app_name = "phonebook_app"

urlpatterns = [
    path("", views.index),
    path("stats", views.stats),
]
