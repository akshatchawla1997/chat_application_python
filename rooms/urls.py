# rooms/urls.py
from django.urls import path, include
from .views import RoomListCreateView, UserViewSet, MyInbox
from rest_framework.routers import DefaultRouter
from .consumers import ChatConsumer

router = DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi(), name='chat-room'),
    path('api/', include(router.urls)), 
    path("my-messages/<user_id>/", MyInbox.as_view())
]
