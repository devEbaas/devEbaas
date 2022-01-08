from rest_framework import serializers
from trueHomeAPI.apps.survey.models import SurveyModel

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyModel
        fields = '__all__'