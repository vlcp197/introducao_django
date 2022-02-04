from django.urls import path
from . import views

#Aponta para a URL da função
urlpatterns = [
    path('hello/',views.say_hello)
]