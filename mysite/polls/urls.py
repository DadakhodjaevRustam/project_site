from django.urls import path

from . import views

urlpatterns = [
    path("", views.first),
    path("users", views.create),
    path("add", views.index),
]