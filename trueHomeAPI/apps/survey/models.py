from django.db import models
from trueHomeAPI.apps.activity.models import ActivityModel

# Create your models here.
class SurveyModel(models.Model):
    id = models.IntegerField(primary_key=True, null=False, blank=False)
    activity_id = models.ForeignKey(ActivityModel, on_delete=models.CASCADE)
    answers = models.JSONField(verbose_name='Answers')
    created_at = models.DateTimeField(auto_now_add=True ,null=False , blank=False)