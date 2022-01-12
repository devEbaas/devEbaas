from django.urls import path
from trueHomeAPI.apps.activity.api.views import ActivityAPIView, CancelActivityAPIView, ReAgendActivityAPIView

urlpatterns = [
    path('activity/', ActivityAPIView.as_view(), name='activity_api'),
    path('cancel_activity/', CancelActivityAPIView.as_view(), name='cancel_activity'),
    path('reagend_activity/', ReAgendActivityAPIView.as_view(), name='reagend_activity')
]
