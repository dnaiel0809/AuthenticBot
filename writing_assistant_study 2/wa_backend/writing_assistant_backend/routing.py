from channels.routing import ProtocolTypeRouter, URLRouter
from django.url import path
from writing_assistant_backend import consumers

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        path('ws/room/<str:room_name>/', consumers.RoomConsurmer.as_asgi())
    ])
})
