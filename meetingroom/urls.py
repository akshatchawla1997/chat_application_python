# meetingroom/urls.py
from django.contrib import admin
from django.urls import path, include
from rooms.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('room/', include('rooms.urls')),
    path('api/', include(router.urls)),  # Include the URLs generated by the router
]
