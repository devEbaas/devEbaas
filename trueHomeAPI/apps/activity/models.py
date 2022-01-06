from django.db import models
from trueHomeAPI.apps.property.models import PropertyModel

# Create your models here.
class ActivityModel(models.Model):
    # id = models.IntegerField(primary_key=True, null=False, blank=False)
    property_id = models.ForeignKey(PropertyModel, on_delete=models.CASCADE)
    schedule = models.DateTimeField(null=False, blank=False)
    title = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(null=False, blank=False)
    updated_at = models.DateTimeField(null=False, blank=False)
    status = models.CharField(null=False, max_length=255)

    def __str__(self):
        return "{0} - {1}".format(self.property_id, self.title)