from django.urls import path
from . import views 

urlpatterns = [
    path('clientes/', views.ClienteView.as_view()),
    path('clientes/<pk>/', views.ClienteUpdateView.as_view()),
]
