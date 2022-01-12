from trueHomeAPI.apps.survey.models import SurveyModel
from trueHomeAPI.apps.activity.models import ActivityModel
import datetime
import pytz

def find_survey_by_activity(activity_id):
    survey = None
    try:
        survey = SurveyModel.objects.get(activity_id = activity_id)
    except Exception as ex:
        print(ex)
    return survey

def validate_activity_condition(activity):
    condition_status = ""
    try:
        
        date = datetime.datetime.now()
        date = pytz.UTC.localize(date)
        schedule = activity.schedule

        schedule = activity.schedule
        if activity.status == 'ACTIVE' and schedule >= date:
            condition_status = "Pendiente a realizar"
        elif activity.status == 'ACTIVE' and schedule <= date:
            condition_status = 'Atrasada'
        elif activity.status == 'DONE':
            condition_status = 'Finalizada'
        elif activity.status == 'DISABLED':
            condition_status = 'Deshabilitada'
        elif activity.status == 'CANCELLED':
            condition_status = 'Cancelada'
        else: 
            condition_status = 'Sin condición'

    except Exception as ex:
        print(ex)
    return condition_status

def validate_schedule_availability(property_id, date):    
    try:
        is_available = None
        end_date = date + datetime.timedelta(hours=1)
        print(end_date)
        total_activities = ActivityModel.objects.filter(schedule__gte=date, schedule__lte=end_date, property_id=property_id).exclude(status = 'CANCELLED').count()
        print(total_activities)
        if total_activities > 0:
            is_available = False
        else:
            is_available = True
    except Exception as ex:
        print(ex)
        return is_available
    return is_available
