from django.urls import path
from . import views 

urlpatterns = [
    path('venda/', views.VendaView.as_view()),
    path('venda/<pk>/', views.VendaUpdateView.as_view()),
]
