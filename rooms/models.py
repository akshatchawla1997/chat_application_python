# rooms/models.py

from django.contrib.auth.models import User
from django.db import models
import uuid

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class MeetingMessage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name} in {self.room.name} at {self.timestamp}"

