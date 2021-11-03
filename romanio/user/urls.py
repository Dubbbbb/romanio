from django.urls import path
from .views import UserSignIn, register

urlpatterns = [
    path('signin/', register, name="signin"),
]
