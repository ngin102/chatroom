from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room

@login_required
def chatrooms(request):
    all_chatrooms = Room.objects.all()

    return render(request, 'chatrooms.html', {'chatrooms': all_chatrooms})

@login_required
def chatroom(request, slug):
    chatroom = Room.objects.get(slug = slug)

    return render(request, 'active_chatroom.html', {'chatroom': chatroom})