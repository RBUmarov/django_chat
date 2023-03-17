
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]

# from django.urls import path
# from channels.routing import ProtocolTypeRouter, URLRouter
# from .consumers import LiveScoreConsumer
#
# websocket_urlpatterns = URLRouter([
#     path(
#         'ws/<str:room_name>/', LiveScoreConsumer,
#         name="room_name",
#     ),
# ])