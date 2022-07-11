from django.urls import path
from requests import delete
from login import views
urlpatterns = [
    path('', views.registerlogin),

    
]