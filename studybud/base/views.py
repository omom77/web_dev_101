from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

# create rooms list
rooms = [
    {'id':1, 'name':'lets learn python'},
    {'id':2, 'name':'design with me'},
    {'id':3, 'name':'frontend developers'}    
]

# http request object
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)