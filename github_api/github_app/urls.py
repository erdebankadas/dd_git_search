from django.urls import path
from . import views

urlpatterns = [
    path("", views.repository_list, name="repository_list"),
]
