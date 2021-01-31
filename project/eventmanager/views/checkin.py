from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm
from eventmanager.models import Event, Participant, Registration
from datetime import datetime

def registration(event, participant):
    try:
        rego = Registration.objects.filter(participant=participant, event=event).get()
        if not rego.checked_in_at:
            now = datetime.now()
            rego.checked_in_at = now
            rego.full_clean()
            rego.save()
            return f"Success: Registration for {participant.first_name} {participant.last_name} for {event.name} was successful"
        else:
            return f"{participant.first_name} {participant.last_name} already checked in for {event.name} on {rego.checked_in_at}"
    except Registration.DoesNotExist:
        return "Error: Participant is not registered for this event"

def checkin(request, event_id, participant_id):
    event = get_object_or_404(Event, pk=event_id)
    participant = get_object_or_404(Participant, pk=participant_id)

    msg = registration(event, participant)

    context = {
        'event': event,
        'p': participant,
        'msg': msg
    }
    return render(request, 'eventmanager/checkin.html', context)
