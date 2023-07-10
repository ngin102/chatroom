from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room, Message

@login_required
def chatrooms(request):
    all_chatrooms = Room.objects.all()

    return render(request, 'chatrooms.html', {'chatrooms': all_chatrooms})

@login_required
def chatroom(request, slug):
    chatroom = Room.objects.get(slug = slug)
    messages = Message.objects.filter(roomName=chatroom).order_by('-dateWritten')[0:30][::-1]

    return render(request, 'active_chatroom.html', {'chatroom': chatroom, 'messages': messages})