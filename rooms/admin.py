from django.contrib import admin

from rooms.models import Room, MeetingMessage


admin.site.register(Room)
admin.site.register(MeetingMessage)