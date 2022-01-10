from django.urls import path
from trueHomeAPI.apps.activity.api.views import ActivityAPIView

urlpatterns = [
    path('activity/', ActivityAPIView.as_view(), name='activity_api')
]
