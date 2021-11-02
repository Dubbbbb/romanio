from django.urls import path
from .views import *

urlpatterns = [
    path('signin/', UserSignIn.as_view(), name="signin"),
]
