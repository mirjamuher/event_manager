from django.contrib import admin
from .models import Participant, Registration, Event

# Register your models here.

admin.site.register(Participant)
admin.site.register(Event)
admin.site.register(Registration)
