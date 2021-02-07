from django.db import models
from django.db.models.constraints import UniqueConstraint


# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    class Meta:
        constraints = [
            UniqueConstraint(fields=['name', 'date'], name='unique_event'), 
        ]
    
    def __str__(self):
        return f"{self.name} on {self.date}"

    def count_registrations(self):
        """
        Returns the amount of people that are signed up
        """
        return self.registration_set.count()

    def count_participants(self):
        """
        Returns the amount of people that are checked in
        """
        #return self.registration_set.filter(checked_in_at__isnull=True).count()
        return self.registration_set.checked_in().count()
