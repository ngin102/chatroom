from django.db import models

class Room(models.Model):
    roomName = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
