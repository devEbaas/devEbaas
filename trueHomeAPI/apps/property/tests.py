from django.test import TestCase
from rest_framework import status
from trueHomeAPI.apps.property.models import PropertyModel
from django.urls import reverse

# Create your tests here.
class PropertyTestCase(TestCase):

    def setUp(self):
        self.property_url = reverse('property_api')
        self.property = PropertyModel.objects.create(
            title = 'Propiedad de Temozón',
            address = 'Calle 12 x 9 y 11 s/n',
            description = 'Propiedad enventa',
            status = 'ENABLED'
        )

    def test_list_properties(self):
        properties = self.client.get(self.property_url,{},format="json")
        self.assertEqual(properties.status_code, status.HTTP_200_OK)