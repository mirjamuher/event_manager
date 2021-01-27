from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('/create', views.create_event, name='create_event'),
    path('/manage/<int:event_id>', views.manage_event, name='manage_event'),
    path('/manage/<int:event_id>/<int:participant_id>', views.manage_participants, name='manage_participants'),
    path('/manage/participants/<int:participant_id>', views.edit_participant, name='edit_participant'),
    path('/checkin/<int:event_id>/<int:participant_id>', views.checkin, name='checkin'),
]
