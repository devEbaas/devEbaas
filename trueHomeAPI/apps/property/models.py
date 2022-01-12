from django.db import models


# Create your models here.
class PropertyModel(models.Model):
    PROPERTY_STATUS = [
        ('DISABLED', 'disabled'),
        ('ENABLED', 'enabled'),
    ]
    title = models.CharField(max_length=255, null=False, blank=False)
    address = models.TextField(null=False, blank=False) 
    description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    disabled_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(null=False, choices= PROPERTY_STATUS, default='ENABLED', max_length=255)

    def __str__(self):
        return self.title

     # meta con información de nombre del modelo
    class Meta: 
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'