from django.shortcuts import get_object_or_404
from django.db import transaction
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import logging
# Modelos, serializadores y funciones
from trueHomeAPI.apps.activity.api.serializers import ActivitySerializer, ActivityListSerializer, CancelActivitySerializer, ReAgendActivitySerializer
from trueHomeAPI.apps.common_functions import validate_schedule_availability
from trueHomeAPI.apps.activity.models import ActivityModel


# Se definen los loggers
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
class ActivityAPIView(APIView):
    def get(self, request):
        # Obtención de query pararms
        start_date = request.query_params.get('start_date', None);
        end_date = request.query_params.get('end_date', None)
        status_param = request.query_params.get('status', None)
        
        try:
            # se definen los rangos de fecha por default 
            default_start_date = timezone.now().replace(hour=0, minute=0, second=0) - timezone.timedelta(days=3)
            default_end_date = timezone.now().replace(hour=23, minute=59, second=59) + timezone.timedelta(weeks=2)
            # variable para setear el query_string por default de la petición
            query_request = ActivityModel.objects.filter(schedule__gte = default_start_date, schedule__lte = default_end_date).order_by('schedule')
            # Se valida que query params se han proporcionado, en caso de no proporcionar, se toma el query_request inicial
            if start_date and end_date and status_param:
                print('entra en el primero')
                query_request = ActivityModel.objects.filter(schedule__gte=start_date, schedule__lte=end_date, status = status_param).order_by('schedule')
            elif start_date and end_date:
                print('entra aquí')
                query_request = ActivityModel.objects.filter(schedule__gte=start_date, schedule__lte=end_date).order_by('schedule')
            elif status_param:
                print('entra en el tercero')
                query_request = ActivityModel.objects.filter(status = status_param).order_by('schedule')

            activity_serializer = ActivityListSerializer(query_request,many=True, context={'request': request})
            return Response(activity_serializer.data, status = status.HTTP_200_OK)
        except Exception as ex:
            logger.error(f"Ha ocurrido el siguiente error: {ex}")
            return Response(data ={'message': 'no se ha podido obtener la lista de actividades'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Función para guardar una nueva actividad
    def post(self, request):
        try:
            activity_serializer = ActivitySerializer(data = request.data)
            activity_serializer.updated_at = timezone.now()
            if activity_serializer.is_valid():
                activity_data = activity_serializer.validated_data
                if activity_data['property_id'].status == "ENABLED":
                    # Retorna True si no hay actividiades e la hora seleccionada
                    is_available = validate_schedule_availability(activity_data['property_id'], activity_data['schedule'])
                    if is_available:
                        with transaction.atomic():
                            activity_serializer.save()
                            return Response(activity_serializer.data, status = status.HTTP_201_CREATED)
                    
                    return Response(data={'message': 'El horario ya se encuentra ocupado por otra actividad'},status=status.HTTP_400_BAD_REQUEST)
                
                return Response(data={'message': 'No se puede crear una actividad para una propiedad desactivada'},status=status.HTTP_400_BAD_REQUEST)

            return Response(activity_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(f"Ha ocurrido el siguiente error: {ex}")
            return Response(data = {'message': 'Ha ocurrido un error en el servidor'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CancelActivityAPIView(APIView):
    def post(self, request):
        try:
            cancel_serializer = CancelActivitySerializer(data = request.data)
            if cancel_serializer.is_valid():
                data = cancel_serializer.validated_data
                activity_to_cancel = get_object_or_404(ActivityModel.objects.all(), pk = data['id'])
                if activity_to_cancel.status == 'CANCELLED':
                    return Response(data = {'message': 'La Actividad ya ha sido cancelada'}, status = status.HTTP_400_BAD_REQUEST)
                with transaction.atomic():
                    activity_to_cancel.status = 'CANCELLED'
                    activity_to_cancel.updated_at = timezone.now()
                    activity_to_cancel.save()
                    return Response(ActivityListSerializer(activity_to_cancel, context={'request': request}).data, status = status.HTTP_202_ACCEPTED)

            return Response(cancel_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(f"Ha ocurrido el siguiente error: {ex}")
            return Response(data = {'message': 'Ha ocurrido un error al actualizar el estatus de la actividad'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

class ReAgendActivityAPIView(APIView):
    def post(self, request):
        reagend_serializer = ReAgendActivitySerializer(data = request.data)
        try:
            if reagend_serializer.is_valid():
                data = reagend_serializer.validated_data
                activity_to_reagend = get_object_or_404(ActivityModel.objects.all(), pk=data['id'])
                if activity_to_reagend.status == "CANCELLED":
                    return Response(data ={'message':'La actividad no se puede reagendar debido a que está cancelada'}, status = status.HTTP_400_BAD_REQUEST)

                    # Se valida la disponibilidad de horario de la propiedad
                is_available = validate_schedule_availability(activity_to_reagend.property_id, data['schedule'])
                if is_available:
                    with transaction.atomic():
                        activity_to_reagend.schedule = data['schedule']
                        activity_to_reagend.updated_at = timezone.now()
                        activity_to_reagend.save()
                        return Response(ActivityListSerializer(activity_to_reagend,context={'request': request}).data, status = status.HTTP_202_ACCEPTED)
                return Response(data = {'message':'La fecha y hora proporcionada ya está en uso'}, status = status.HTTP_400_BAD_REQUEST)
            
            return Response(reagend_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            logger.error(f"Ha ocurrido el siguiente error: {ex}")
