from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.forms import ModelForm
from eventmanager.models import Event


# Create your views here.

def landing_page(request):
    context = {}
    return render(request, 'eventmanager/landing_page.html', context)

def create_event(request):
    class EventForm(ModelForm):
        class Meta:
            model = Event
            fields = ['name', 'date']

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


# Still needs EVERYTHING DONE (even create .html page)
def manage_event(request, event_id):
    response = f"You are looking at the event {event_id}"
    return HttpResponse(response)

def manage_participants(request, event_id):
    response = f"You are managing the participants of event {event_id}"
    return HttpResponse(response)

def edit_participant(request, participant_id):
    response = f"You are managing participant no {participant_id}"
    return HttpResponse(response)

def checkin(request, event_id, participant_id):
    response = f"You have checked in {participant_id}"
    return HttpResponse(response)
