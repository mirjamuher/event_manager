from django.db import models
from django.db.models.constraints import UniqueConstraint


# Create your models here.

class Participant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    organisation = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length = 100, blank=True)
    email = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=15, blank=True)
    comment = models.TextField(blank=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['first_name', 'last_name', 'email'], name='unique_participant'),
        ]
