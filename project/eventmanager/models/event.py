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
