from django.db import models

# Create your models here.

class Participant(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    organisation_name = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length = 100, blank=True)
    email = models.EmailField(max_length=250, blank=True)
    phone_number = models.CharField(max_lengt=15, blank=True)
    comment = models.TextField(blank=True)

