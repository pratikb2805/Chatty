from django.contrib import admin
from django.urls import path, include
from .views import respond
urlpatterns = [
    path('', respond )
]
