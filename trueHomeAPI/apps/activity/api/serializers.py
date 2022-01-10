from django.db.models import fields
from rest_framework import serializers
from trueHomeAPI.apps.activity.models import ActivityModel
from trueHomeAPI.apps.property.api.serializers import PropertySerializer
from trueHomeAPI.apps.survey.api.serializers import SurveySerializer
from trueHomeAPI.apps.common_functions import find_survey_by_activity
# from trueHomeAPI.apps.property.models import PropertyModel

class ActivitySerializer(serializers.ModelSerializer):
    # property = serializers.StringRelatedField()
    # property = PropertySerializer(many=True, read_only=True)
    class Meta:
        model = ActivityModel
        fields = '__all__'

    def to_representation(self, instance):
        activity_data = super(ActivitySerializer, self).to_representation(instance)
        survey = find_survey_by_activity(instance.id)
        survey_data = SurveySerializer(survey).data
        property_data = PropertySerializer(instance.property_id).data

        # Se elimina el id de la propiedad de la respuesta
        del activity_data['property_id']
        # Asignación de propiedades a la instancia 
        activity_data['property'] = property_data
        activity_data['survey'] = survey_data

        return activity_data
        
        
        # pass
    

# qs = ActivityModel.objects.prefetch_related('property_id')