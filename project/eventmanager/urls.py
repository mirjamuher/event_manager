from django.urls import path
from eventmanager.views import create_event, landing_page, manage_event, edit_participant, checkin

app_name = 'eventmanager'
urlpatterns = [
    path('', landing_page.landing_page, name='landing_page'),
    path('dashboard', landing_page.dashboard, name='dashboard'),
    path('create', create_event.create_event, name='create_event'),
    path('manage/<int:event_id>', manage_event.manage_event, name='manage_event'),
    # path('manage/<int:event_id>/<int:participant_id>', views.manage_participants, name='manage_participants'),
    path('manage/participant/<int:participant_id>', edit_participant.edit_participant, name='edit_participant'),
    path('checkin/<int:event_id>/<int:participant_id>', checkin.checkin, name='checkin'),
    path('cancel_checkin/<int:event_id>/<int:participant_id>', checkin.cancel_checkin, name="cancel_checkin"),
]
