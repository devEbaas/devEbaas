from django.db import models
from trueHomeAPI.apps.property.models import PropertyModel

# Create your models here.
class ActivityModel(models.Model):

    STATUS_CHOICES = [
        ('DISABLED', 'disabled'),
        ('ACTIVE', 'active'),
        ('CANCELLED', 'cancelled'),
        ('DONE', 'done')
    ]
    
    property_id = models.ForeignKey(PropertyModel, verbose_name='Property',on_delete=models.CASCADE)
    schedule = models.DateTimeField(null=False, blank=False)
    title = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True,null=False, blank=False)
    updated_at = models.DateTimeField(auto_now_add=True ,null=False, blank=False)
    status = models.CharField(null=False, choices=STATUS_CHOICES, default='ACTIVE',max_length=255)

    def __str__(self):
        return "{0}".format(self.title)
    
    # meta con información de nombre del modelo
    class Meta: 
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'