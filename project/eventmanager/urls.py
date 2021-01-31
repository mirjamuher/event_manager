from django.urls import path
from . import views
import views.create_event
import views.landing_page
import views.manage_event
import views.edit_participant
import views.checkin

app_name = 'eventmanager'
urlpatterns = [
    path('', views.landing_page.landing_page, name='landing_page'),
    path('create', views.create_event.create_event, name='create_event'),
    path('manage/<int:event_id>', views.manage_event.manage_event, name='manage_event'),
    # path('manage/<int:event_id>/<int:participant_id>', views.manage_participants, name='manage_participants'),
    path('manage/participant/<int:participant_id>', views.edit_participant.edit_participant, name='edit_participant'),
    path('checkin/<int:event_id>/<int:participant_id>', views.checkin.checkin, name='checkin'),
]
