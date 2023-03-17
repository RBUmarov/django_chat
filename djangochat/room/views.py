from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User, Group

from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:50]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})


# def index(request):
#     current_user_groups = request.user.groups.values_list("name", flat=True)
#     context = {
#         "is_bunned": "Bunned" in current_user_groups,
#     }
#     return render(request, 'room/room.html', context)
