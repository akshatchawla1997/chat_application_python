# rooms/serializers.py
from rest_framework import serializers
from .models import Room,User, MeetingMessage, Profile

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'full_name', 'bio', 'image']
class MeetingMessageSerializer(serializers.ModelSerializer):
    receiver_profile = ProfileSerializer(read_only=True)
    sender_profile = ProfileSerializer(read_only=True)
    class Meta:
        model = MeetingMessage
        fields = ['id', 'user', 'sender', 'sender_profile', 'receiver_profile', 'receiver', 'message', 'is_read', 'date']