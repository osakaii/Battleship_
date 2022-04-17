from django.urls import re_path
from . import consumers

ws_urlpatterns = [
    re_path(r'ws/game/(?P<game_name>\w+)/$', consumers.BattleShipConsumer.as_asgi())
]
