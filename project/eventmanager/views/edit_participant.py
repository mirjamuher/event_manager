from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm
from eventmanager.models import Event, Participant, Registration
import csv
import io

def edit_participant(request, participant_id):
    response = f"You are managing participant no {participant_id}"
    return HttpResponse(response)
