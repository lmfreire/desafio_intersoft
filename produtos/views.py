from django.shortcuts import render
from rest_framework import generics

from .models import Produto

from .serializers import ProdutoSerializer, ProdutoUpdateSerializer

class ProdutoView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoUpdateView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Produto.objects.all()
    serializer_class = ProdutoUpdateSerializer