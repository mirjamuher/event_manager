from django import forms
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404
from eventmanager.models import Event, Participant, Registration
from django.http import HttpResponse
import csv
import io
from django.contrib.auth.decorators import login_required

# TODO: Create QR code list for download 


# FUNCTIONS HANDLING ORM

def handle_participant_csv_upload(event, djangoStyleFile):
    error_msg = []

    uploaded_file_as_bytes = djangoStyleFile.read()
    uploaded_file_as_a_string = uploaded_file_as_bytes.decode(djangoStyleFile.charset or 'utf-8')
    file = io.StringIO(uploaded_file_as_a_string)
    reader = csv.DictReader(file)

    for row_nr, row in enumerate(reader, start=2):
        # Step One: Clean and verify file info
        cleaned_row = validate_row(row)
        missing_fieldname = is_fieldname_missing(cleaned_row)
        if missing_fieldname:
            error_msg = [f"ERROR: The column(s) {missing_fieldname} are missing. Please add them to your file and try again"]
            break
        
        # Step Two: Update Database
        try:
            participant = get_or_create_participant(cleaned_row)
            get_or_create_registration(participant, event)
        except ValidationError as e:
            error_msg.append(f"In Row {row_nr}: {e}")
            continue
        print(row)

    return error_msg


PARTICIPANT_LIST_FIELDNAMES = {'organisation', 'first_name', 'last_name', 'position', 'email', 'phone_number', 'comment'}

def validate_row(row):
    cleaned_row = {}
    for k, v in row.items():
        v = v.strip()
        if k in PARTICIPANT_LIST_FIELDNAMES:
            if k == 'email':
                cleaned_row[k] = v.lower()
            elif k == 'comment':
                cleaned_row[k] = v
            else:
                cleaned_row[k] = v.title()
    return cleaned_row

def is_fieldname_missing(cleaned_row):
    """
    Compares set PARTICIPANT_LIST_FIELDNAME against keys in participant_dictionary.
    If the same returns empty list, else returns missing fieldname
    """
    key_list = set(cleaned_row)
    missing = PARTICIPANT_LIST_FIELDNAMES.difference(key_list)
    return missing

def get_or_create_participant(data:dict):
    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']

    try: 
        p = Participant.objects.filter(email=email, first_name=first_name, last_name=last_name).get()
    except Participant.DoesNotExist:
        p = Participant(**data)
        p.full_clean()
        p.save()
    else:
        for k, v in data.items():
            # Set field "k" on Participant to be value "v".
            setattr(p, k, v)
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

@login_required
def manage_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    has_been_uploaded = False
    error_msg = ""

    class UploadFileForm(forms.Form):
        file = forms.FileField()

    if request.method == "POST":
        has_been_uploaded = True
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            error_msg = handle_participant_csv_upload(event, request.FILES['file'])
            # return HttpResponse('Upload was successful')
    else:
        form = UploadFileForm()

    registration_query = Registration.objects.filter(event=event_id).order_by('participant__first_name', 'participant__last_name')  # returns registration list

    context = {
        'event': event, 
        'form': form, 
        'registration_list': registration_query,
        'has_been_uploaded': has_been_uploaded,  # shows if site was loaded for the first time
        'error_msg': error_msg,
    }

    return render(request, 'eventmanager/manage_event.html', context)


@login_required
def list_all_events(request):
    event_list = Event.objects.order_by('date')
    context = {
        'event_list': event_list
    }

    return render(request, 'eventmanager/list_all_events.html', context)


"""
NEW STUFF:
    #getattr(object, 'attribute') -> value
    #setattr(object, 'atttribute', 'value')
    #hasattr(object, 'attribute_name') -> bool  # Does the given object have an attribute called attribute_name


def my_function(a, b, *args, **kwargs):
    print(a, b, args, kwargs)

my_function(1, 2)  # 1, 2, [], {}
my_function(1, 2, 4, 5, cat='meow', dog='woof')  # 1, 2, [4, 5], {'cat': 'meow', 'dog': 'woof'}
my_function(cat='meow', b=4, chicken='cluck', dog='woof', a=5)  # 5, 4, [], {'...'}
my_function(**{'cat': 'meow', 'dog': 'woof', 'a': 6, 'b': 8})  # a, b, [], {'cat': 'meow', 'dog': 'woof'}
"""
