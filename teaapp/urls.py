from django.urls import path
from .views import *
app_name = "teaapp"

urlpatterns = [
    path("teas/", tea_list, name="tea_list"),
]
