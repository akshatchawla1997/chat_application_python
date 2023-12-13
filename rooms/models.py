# rooms/models.py

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    bio = models.CharField(max_length=100)
    image = models.ImageField(upload_to="user_images", default="default.jpg")
    verified = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.full_name == "" or self.full_name == None:
            self.full_name = self.user.username
        super(Profile, self).save(*args, **kwargs)

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class MeetingMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')

    message = models.CharField(max_length=10000000000)

    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)


    
    class Meta:
        ordering = ['date']
        verbose_name_plural = "Message"

    def __str__(self):
        return f"{self.sender} - {self.receiver}"

    @property
    def sender_profile(self):
        sender_profile = Profile.objects.get(user=self.sender)
        return sender_profile
    @property
    def reciever_profile(self):
        reciever_profile = Profile.objects.get(user=self.reciever)
        return reciever_profile