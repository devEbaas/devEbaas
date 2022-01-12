from django.urls import path
from trueHomeAPI.apps.survey.api.views import SurveyAPIView

urlpatterns = [
    path('survey/', SurveyAPIView.as_view(), name='survey_api')
]
