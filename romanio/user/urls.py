from django.urls import path
from .views import UserLogin, UserSignIn, logout_view

urlpatterns = [
    path('signin/', UserSignIn.as_view(), name="signin"),
    path('login/', UserLogin.as_view(), name="login"),
    path('logout/', logout_view, name='logout')
]
