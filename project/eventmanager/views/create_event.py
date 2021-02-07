from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm
from eventmanager.models import Event, Participant, Registration
import csv
import io
from django.contrib.auth.decorators import login_required

@login_required
def create_event(request):
    class EventForm(ModelForm):
        class Meta:
            model = Event
            fields = ['name', 'date']
            widgets = {
                'name': forms.TextInput(attrs={'placeholder': 'Event Name'}),
                'date': forms.DateInput(attrs={'type': 'date'}),
            }

    # If the form was sent:
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return HttpResponseRedirect(reverse('eventmanager:manage_event', args=[event.id]))

    # If the site is called for the first time:
    else:
        form = EventForm()
    return render(request, 'eventmanager/create_event.html', {'form': form})
