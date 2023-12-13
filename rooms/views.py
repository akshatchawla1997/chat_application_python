# rooms/views.py
from rest_framework import generics, viewsets
from .models import Room, User, MeetingMessage
from .serializer import RoomSerializer, UserSerializer, MeetingMessageSerializer
from django.db.models import Subquery, Q, OuterRef
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
            id__in =  Subquery(
                User.objects.filter(
                    Q(sender__reciever=user_id) |
                    Q(reciever__sender=user_id)
                ).distinct().annotate(
                    last_msg=Subquery(
                        MeetingMessage.objects.filter(
                            Q(sender=OuterRef('id'),reciever=user_id) |
                            Q(reciever=OuterRef('id'),sender=user_id)
                        ).order_by('-id')[:1].values_list('id',flat=True) 
                    )
                ).values_list('last_msg', flat=True).order_by("-id")
            )
        ).order_by("-id")
            
        return messages
    