from django.contrib import admin

from rooms.models import Room, MeetingMessage,  Profile, MeetingMessage


class ProfileAdmin(admin.ModelAdmin):
    list_editable = ['verified']
    list_display = ['user', 'full_name' ,'verified']

class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')

class MeetingMessageAdmin(admin.ModelAdmin):
    list_editable = ['is_read', 'message']
    list_display = ['user','sender', 'receiver', 'is_read', 'message']


admin.site.register(Room)
admin.site.register(MeetingMessage,MeetingMessageAdmin)
admin.site.register(Profile,ProfileAdmin)