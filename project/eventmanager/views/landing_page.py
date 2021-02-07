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


def landing_page(request):
    context = {}
    return render(request, 'eventmanager/landing_page.html', context)


@login_required
def dashboard(request):
    latest_event_list = Event.objects.order_by('-date')[:10]
    context = {
        'latest_event_list': latest_event_list,
    }
    return render(request, 'eventmanager/dashboard.html', context)
