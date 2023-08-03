from django.shortcuts import render
from rest_framework import generics

from .models import Cliente

from .serializers import ClienteSerializer, ClienteUpdateSerializer

class ClienteView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteUpdateView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Cliente.objects.all()
    serializer_class = ClienteUpdateSerializer