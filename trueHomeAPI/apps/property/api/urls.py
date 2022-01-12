from django.urls import path
from trueHomeAPI.apps.property.api.views import PropertyAPIView

urlpatterns = [
    path('property/', PropertyAPIView.as_view(), name='property_api')
]
