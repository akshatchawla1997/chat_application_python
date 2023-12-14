# rooms/urls.py
from django.urls import path, include
from .views import RoomListCreateView, UserViewSet, MyInbox, GetMessages, SendMessage, SearchUser, ProfileDetails
from rest_framework.routers import DefaultRouter
from .consumers import ChatConsumer

router = DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi(), name='chat-room'),
    path('api/', include(router.urls)), 
    # chat messages api
    path('my-messages/<user_id>/', MyInbox.as_view()),
    path('get-messages/<sender_id>/<receiver_id>/', GetMessages.as_view()),
    path('send-messages/', SendMessage.as_view()),
    # profile details
    path('profile/<int:pk>/',ProfileDetails.as_view()),
    path('profile/search/<username>/',SearchUser.as_view())
]
