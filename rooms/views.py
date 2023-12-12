# rooms/views.py
from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Room
from .serializer import RoomSerializer

class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

