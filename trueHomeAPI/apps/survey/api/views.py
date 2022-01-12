from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import logging
# Modelos y serializadores
from trueHomeAPI.apps.survey.api.serializers import SurveySerializer
from trueHomeAPI.apps.survey.models import SurveyModel

# Se definen los loggers
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

class SurveyAPIView(APIView):
    def get(self, request):
        surveys = SurveyModel.objects.all()
        survey_serializer = SurveySerializer(surveys, many=True)
        return Response(survey_serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        try:
            survey_serializer = SurveySerializer(data = request.data)
            if survey_serializer.is_valid():
                survey_serializer.save()
                return Response(survey_serializer.data, status = status.HTTP_201_CREATED)
            else:
                return Response(survey_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(f"Ha ocurrido el siguiente error: {ex}")
            return Response(data ={'message':'Ha ocurrido un error en el servidor'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        