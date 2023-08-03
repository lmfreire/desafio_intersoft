from django.shortcuts import render
from rest_framework import generics

from .models import Venda

from .serializers import VendaSerializer, VendaUpdateSerializer

class VendaView(generics.ListCreateAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class VendaUpdateView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Venda.objects.all()
    serializer_class = VendaUpdateSerializer