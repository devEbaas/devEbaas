from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from trueHomeAPI.apps.property.models import PropertyModel
from trueHomeAPI.apps.property.api.serializers import PropertySerializer
import logging

class PropertyAPIView(APIView):
    # get method
    def get(self, request):
        properties = PropertyModel.objects.all()
        property_serializer = PropertySerializer(properties, many=True)
        return Response(property_serializer.data)

    def post(self, request):
        logger = logging.getLogger("Error saving property")
        try:
            property_data = request.data
            property_serializer = PropertySerializer(data = property_data)
            # Se valida si los datos mandados por el usuario son válidos
            if property_serializer.is_valid():
                property_serializer.save()
                return Response(property_serializer.data)
            else:
                return Response(property_serializer.errors)
        except Exception as ex:
            logger.exception(ex)
            return Response("Error saving property")
        