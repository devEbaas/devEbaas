from django.db.models import fields
from rest_framework import serializers
from trueHomeAPI.apps.activity.models import ActivityModel

class ActivitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ActivityModel
        fields = '__all__'