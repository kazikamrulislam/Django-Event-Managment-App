from django.shortcuts import render, redirect
from .import forms
# from .import models
from .models import Event


def home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})


def add_event(request):
    if request.method == 'POST':
        event_form = forms.EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            return redirect('add_event')
        
    else:
        event_form = forms.EventForm()
        
    return render(request, 'add_event.html',{'form': event_form})
