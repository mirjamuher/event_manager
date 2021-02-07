from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.utils import timezone

class RegistrationQuerySet(models.QuerySet):
    def checked_in(self):
        """
        Filters for registrations of people that have been checked in.
        """
        return self.filter(checked_in_at__isnull=False)

class Registration(models.Model):
    participant = models.ForeignKey('Participant', on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    checked_in_at = models.DateTimeField(null=True, blank=True)

    objects = RegistrationQuerySet.as_manager()

    class Meta:
        constraints = [
            UniqueConstraint(fields=['participant', 'event'], name='unique_registration'), 
        ]
