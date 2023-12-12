# meetingroom/asgi.py
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import rooms.routing

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        rooms.routing.websocket_urlpatterns
    ),
})
