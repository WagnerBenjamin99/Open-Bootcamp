from django.urls import path, include
from . import views

urlpatterns = [
    path('queris/', views.queris, name='queris')
]