from django.contrib.auth.models import User
from django.db import models

class Room(models.Model):
    roomName = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

class Message(models.Model):
    roomName = models.ForeignKey(Room, related_name = 'messages', on_delete = models.CASCADE)
    userName = models.ForeignKey(User, related_name = 'messages', on_delete = models.CASCADE)
    messageContent = models.TextField()
    dateWritten = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ('dateWritten',)