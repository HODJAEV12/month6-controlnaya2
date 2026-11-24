from django.contrib import admin
from django.urls import path

from .views import RegisterView, StatsView

urlpatterns = [
    path("api/v1/stats/", StatsView.as_view(), name="stats"),
    path("api/v1/register/", RegisterView.as_view(), name="register"),
]