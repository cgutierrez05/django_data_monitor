from django.urls import path
from . import views

urlpatterns = [
   path("", views.base, name=""),
   path("index/", views.index, name="index"),
]