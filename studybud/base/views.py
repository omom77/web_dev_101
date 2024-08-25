from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# http request object
def home(request):
    return HttpResponse('Home page')

def room(request):
    return HttpResponse('ROOM')