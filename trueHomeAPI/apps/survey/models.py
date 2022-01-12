from django.db import models
from trueHomeAPI.apps.activity.models import ActivityModel

# Create your models here.
class SurveyModel(models.Model):
    activity_id = models.OneToOneField(ActivityModel, on_delete=models.CASCADE)
    answers = models.JSONField(verbose_name='Answers')
    created_at = models.DateTimeField(auto_now_add=True ,null=False , blank=False)

     # meta con información de nombre del modelo
    class Meta: 
        verbose_name = 'Survey'
        verbose_name_plural = 'Surveys'