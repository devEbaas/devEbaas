from django.test import TestCase
from rest_framework import status
from trueHomeAPI.apps.activity.models import ActivityModel
from trueHomeAPI.apps.property.models import PropertyModel
from django.urls import reverse
# Create your tests here.
class ActivityTestCase(TestCase):
    
    def setUp(self):
        # URLs para prueba de peticiones
        self.activity_url = reverse('activity_api')
        self.property_url = reverse('property_api')
        self.reagend_url = reverse('reagend_activity')
        self.cancel_url = reverse('cancel_activity')

        self.property = PropertyModel.objects.create(
            title = 'Propiedad de Hunuku',
            address = 'Calle 9 x 2 y 6 s/n',
            description = 'Propiedad de eduardo',
            status = 'ENABLED'
        )
        self.property_disabled = PropertyModel.objects.create(
            title = 'Propiedad de deshabilitada',
            address = 'Calle 47 x 32 y 34',
            description = 'Propiedad de valladolid, Yucatán',
            status = 'DISABLED'
        )
        self.activity = ActivityModel.objects.create(
            property_id = self.property,
            schedule = "2022-01-12T09:00:00-06:00",
            title = "Test para prueba de creación de actividad",
            status = "ACTIVE"
        )
        self.activity_to_reagend = ActivityModel.objects.create(
            property_id = self.property,
            schedule = "2022-01-12T09:00:00-06:00",
            title = "Test para prueba de creación de actividad",
            status = "ACTIVE"
        )
        self.activity_cancelled = ActivityModel.objects.create(
            property_id = self.property,
            schedule = "2022-01-10T09:00:00-06:00",
            title = "Test para reagendar actividad cancelada",
            status = "CANCELLED"
        )

    def test_activity_list (self):
        response = self.client.get(self.activity_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_activity(self):
        activity = {
            "property_id" : self.property.id,
            "schedule" : "2022-01-13T09:00:00-06:00",
            "title" : "Test para prueba de creación de actividad",
            "status" : "ACTIVE"
        }
        # Se le asigna una actividad a la propiedad
        activity_response = self.client.post(self.activity_url, activity, format='json')
        # Se valida el status de la peticione
        self.assertEqual(activity_response.status_code, status.HTTP_201_CREATED)

    # Creamos una actividad con un horario ue ya está en uso
    def test_create_activity_duplicated_schedule(self):
        activity = {
            "property_id" : self.property.id,
            "schedule" : "2022-01-12T09:00:00-06:00",
            "title" : "Actividad con schedule ya en uso",
            "status" : "ACTIVE"
        }
        activity_response = self.client.post(self.activity_url, activity, format="json")
        self.assertEqual(activity_response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_activity_disabled_property(self):
        activity = {
            "property_id" : self.property_disabled.id,
            "schedule" : "2022-01-15T09:00:00-06:00",
            "title" : "Test creación de actividad para propiedad deshabilitada",
            "status" : "ACTIVE"
        }
        activity_response = self.client.post(self.activity_url, activity, format="json")
        self.assertEqual(activity_response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_reagend_activity(self):
        activity = {
            "id": self.activity.id,
            "schedule": "2022-01-15T09:00:00-06:00"
        }
        activity_response = self.client.post(self.reagend_url, activity, format="json")
        self.assertEqual(activity_response.status_code, status.HTTP_202_ACCEPTED)
    
    def test_reagend_activity_duplicated_schedule(self):
        # se le asigna el mismo schedule que la primera actividad
        activity = {
            "id": self.activity_to_reagend.id,
            "schedule": "2022-01-12T09:00:00-06:00"
        }
        activity_response = self.client.post(self.reagend_url, activity, format="json")
        self.assertEqual(activity_response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_reagend_cancelled_activity(self):
        activity = {
            "id": self.activity_cancelled.id,
            "schedule": "2022-01-09T09:00:00-06:00"
        }
        activity_response = self.client.post(self.reagend_url, activity, format="json")
        self.assertEqual(activity_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cancel_activity(self):
        activity = {
            "id": self.activity.id,
        }
        activity_response = self.client.post(self.cancel_url, activity, format="json")
        self.assertEqual(activity_response.status_code, status.HTTP_202_ACCEPTED)

    def test_cancel_activity_with_cancelled_status(self):
        activity = {
            "id": self.activity_cancelled.id,
        }
        activity_response = self.client.post(self.cancel_url, activity, format="json")
        self.assertEqual(activity_response.status_code, status.HTTP_400_BAD_REQUEST)