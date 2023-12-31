import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import Message, Room

from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)

        roomName = data['roomname']
        userName = data['username']
        message = data['message']

        await self.save_message(userName, roomName, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': userName,
                'roomname': roomName
            }
        )

    async def chat_message(self, event):
        roomName = event['roomname']
        userName = event['username']
        message = event['message']

        await self.send(text_data = json.dumps({
            'message': message,
            'username': userName,
            'roomname': roomName
        }))

    @sync_to_async
    def save_message(self, userName, roomName, message):
        user = User.objects.get(username = userName)
        room = Room.objects.get(slug = roomName)

        Message.objects.create(roomName = room, userName = user, messageContent = message)
