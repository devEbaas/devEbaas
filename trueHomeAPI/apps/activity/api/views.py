from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from trueHomeAPI.apps.activity.api.serializers import ActivitySerializer
from trueHomeAPI.apps.activity.models import ActivityModel
import logging

class ActivityAPIView(APIView):

    def get(self, rquest):
        activities = ActivityModel.objects.all()
        activity_serializer = ActivitySerializer(activities, many=True)
        return Response(activity_serializer.data, status = status.HTTP_200_OK)

    def post(self, request):
        try:
            activity_serializer = ActivitySerializer(data = request.data)
            if activity_serializer.is_valid():
                activity_serializer.save()
                return Response(activity_serializer.data, status = status.HTTP_201_CREATED)
            else:
                return Response(data={'message': 'Por favor, verifique que todos los campos han sido llenados correctamente'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logging.getLogger('Ha ocurrido un error al guardar la propiedad')
            return Response(data={'message': 'Ha ocurrido un error en el servidor'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
