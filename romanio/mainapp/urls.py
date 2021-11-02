from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    # path('contacts/', contacts_page, name="contacts_page"),
    path('catalog/<str:slug_url>/',CatalogPage.as_view(), name="category"),
    path('<str:slug_category>/<str:slug_url>/', ProductDetail.as_view(), name="product_detail")
]