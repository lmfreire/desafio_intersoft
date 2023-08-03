from django.urls import path
from . import views 

urlpatterns = [
    path('produtos/', views.ProdutoView.as_view()),
    path('produtos/<pk>/', views.ProdutoUpdateView.as_view()),
]
