from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.utils import timezone


# Create your models here.

class Registration(models.Model):
    participant = models.ForeignKey('Participant', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    checked_in_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['participant', 'event'], name='unique_registration'), 
        ]
