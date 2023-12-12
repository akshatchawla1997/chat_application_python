# rooms/urls.py
from django.urls import path
from .views import RoomListCreateView
from .consumers import ChatConsumer

urlpatterns = [
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi(), name='chat-room'),
]
