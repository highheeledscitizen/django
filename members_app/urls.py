from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("input_page", views.input_page, name="input_page"),
    path("input_list", views.input_list, name="input_list"),
]
