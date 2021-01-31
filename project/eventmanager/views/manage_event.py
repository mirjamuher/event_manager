from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.forms import ModelForm
from eventmanager.models import Event, Participant, Registration
import csv
import io

# TODO: Create QR code list for download 


# FUNCTIONS HANDLING ORM

def handle_participant_csv_upload(event, djangoStyleFile):
    uploaded_file_as_bytes = djangoStyleFile.read()
    uploaded_file_as_a_string = uploaded_file_as_bytes.decode(djangoStyleFile.charset or 'utf-8')
    file = io.StringIO(uploaded_file_as_a_string)
    reader = csv.DictReader(file)
    for row in reader:
        #TODO: VALIDATE ROW INFO
        participant = get_or_create_participant(row)
        get_or_create_registration(participant, event)
        print(row)

def get_or_create_participant(data:dict):
    email = data['email'].lower()
    try: 
        p = Participant.objects.filter(email=email).get()
        # TODO: How do I update fields of P that haven't been filled before
        # without going through each manually?
    except Participant.DoesNotExist:
        p = Participant(**data)
        p.full_clean()
        p.save()
    return p

def get_or_create_registration(participant, event):
    try:
        rego = participant.registration_set.filter(event=event).get()
    except Registration.DoesNotExist:
        rego = Registration(participant=participant, event=event)
        rego.full_clean()
        rego.save()
    return


# ACTUAL SITE VIEW

def manage_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    class UploadFileForm(forms.Form):
        file = forms.FileField()

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_participant_csv_upload(event, request.FILES['file'])
            print(request.FILES)
            return HttpResponse('Upload was successful')
    else:
        form = UploadFileForm()

    registration_queary = Registration.objects.filter(event=event_id) # returns registration list

    context = {
        'event': event, 
        'form': form, 
        'registration_list': registration_queary,
    }

    return render(request, 'eventmanager/manage_event.html', context)
