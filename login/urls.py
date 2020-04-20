from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("new", views.new, name="new"),
    path("login", views.login, name="login"),
    path("alogin", views.alogin, name="alogin")
]