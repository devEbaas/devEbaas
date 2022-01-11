import socket
from django.http import HttpRequest
from rest_framework import serializers
from trueHomeAPI.apps.activity.models import ActivityModel
from trueHomeAPI.apps.property.api.serializers import PropertyFilterSerializer
from trueHomeAPI.apps.survey.api.serializers import SurveySerializer
from trueHomeAPI.apps.common_functions import find_survey_by_activity, validate_activity_condition
from django.contrib.sites.shortcuts import get_current_site

class ActivitySerializer(serializers.ModelSerializer):
    # property = serializers.StringRelatedField()
    # property = PropertySerializer(many=True, read_only=True)
    class Meta:
        model = ActivityModel
        fields = '__all__'

class ActivityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityModel
        exclude = ['updated_at', 'property_id']

    def to_representation(self, instance):
        activity_data = super(ActivityListSerializer, self).to_representation(instance)
        property_data = PropertyFilterSerializer(instance.property_id).data
        survey = find_survey_by_activity(instance.id)
        survey_data = SurveySerializer(survey, context= self.context).data
        try:
            if survey_data:
                activity_data['survey'] = "{0}/survey/detail/{1}/".format(get_current_site(self.context['request']), survey.id)
        except Exception as ex:
            activity_data['survey'] = None 
            print(ex)
        # Asignación de propiedades a la instancia 
        # print(get_current_site(self.context['request']))
        activity_data['condition'] = validate_activity_condition(instance)
        activity_data['property'] = property_data

        return activity_data

class ReAgendActivitySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    schedule = serializers.DateTimeField()


class CancelActivitySerializer(serializers.Serializer):
    id = serializers.IntegerField()

        # pass
    

# qs = ActivityModel.objects.prefetch_related('property_id')