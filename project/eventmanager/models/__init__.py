from .event import Event
from .participant import Participant
from .registration import Registration

__all__ = [
    'Event',
    'Participant',
    'Registration',
]


"""
three-step guide to making model changes:

Change your models (in models).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.
"""
