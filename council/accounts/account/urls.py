from django.urls import path
from .views import register

urlpatterrns = [
    path('register/', register, name='register'),
]