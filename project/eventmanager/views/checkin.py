from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm
from eventmanager.models import Event, Participant, Registration

def checkin(request, event_id, participant_id):
    response = f"You have checked in {participant_id}"
    return HttpResponse(response)
