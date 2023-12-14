# rooms/views.py
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Room, User, MeetingMessage, Profile
from .serializer import RoomSerializer, UserSerializer, MeetingMessageSerializer, ProfileSerializer
from django.db.models import Subquery, Q, OuterRef
from rest_framework.response import Response
from rest_framework import status
class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MyInbox(generics.ListAPIView):
    serializer_class = MeetingMessageSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']

        messages = MeetingMessage.objects.filter(
            Q(sender=user_id, receiver__received_messages__sender=user_id) |
            Q(receiver=user_id, sender__received_messages__receiver=user_id)
        ).distinct().order_by("-id")

        return messages

    
class GetMessages(generics.ListAPIView):
    serializer_class = MeetingMessageSerializer

    def get_queryset(self):
        sender_id = self.kwargs['sender_id']
        receiver_id = self.kwargs['receiver_id']
        messages = MeetingMessage.objects.filter(
            sender__in=[sender_id, receiver_id],
            receiver__in=[sender_id, receiver_id]
        )
        return messages
    
class SendMessage(generics.CreateAPIView):
    serializer_class = MeetingMessageSerializer

class ProfileDetails(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]

class SearchUser(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    # permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        username = self.kwargs['username']
        logged_in_user = self.request.user
        users = Profile.objects.filter(
            Q(user__username__icontains = username) |
            Q(full_name__icontains = username) |
            Q(user__email__icontains = username) &
            ~Q(user = logged_in_user)
        )
        if not users.exists():
            return Response(
                {"details": "no users found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
