"""
ASGI config for tender project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import dashboard.routing
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tender.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
      AuthMiddlewareStack(
        URLRouter(
          dashboard.routing.websocket_urlpatterns
        )
      )
    )
})
