from django.db import models


# Create your models here.
class PropertyModel(models.Model):
    title = models.CharField(primary_key=True ,max_length=255, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(null=False, blank=False)
    updated_at = models.DateTimeField(null=False, blank=False)
    disabled_at = models.DateTimeField(null=True)
    status = models.CharField(null=False, max_length=255)

    def __str__(self):
        return self.title