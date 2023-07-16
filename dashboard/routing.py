from django.urls import path
from . import consumers

websocket_urlpatterns = [
  path("webapi/", consumers.WebApi.as_asgi()),
]