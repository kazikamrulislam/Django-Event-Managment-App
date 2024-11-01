from django.shortcuts import render
from event.models import Event

def home(request):
    data = Event.objects.all()
    
    return render(request, 'home.html', {'data': data})