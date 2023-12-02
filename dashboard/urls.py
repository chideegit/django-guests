from django.urls import path 
from .views import * 

urlpattern = [
    path('', dashboard, name='dashboard')
]