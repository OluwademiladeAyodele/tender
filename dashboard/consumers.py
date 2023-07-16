import json
from channels.consumer import AsyncConsumer
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async


user = get_user_model()

class WebApi(AsyncConsumer):
  async def websocket_connect(self, event):
    print("connect", event)
    
    await self.send({
    'type': 'websocket.accept'
    })

  async def websocket_receive(self, event):
    print("receive", event)

  async def websocket_disconnect(self, event):
    print("disconnect", event)
   
  async def chat_message(self, event):
    print("chat_message", event)
    
    # notify.send(sender = event["nuser"], recipient=self.scope["user"], verb="You just have a new message")
    await self.send({
      'type': 'websocket.send',
      'text': event["text"]
    })

