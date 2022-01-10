from trueHomeAPI.apps.survey.models import SurveyModel
from trueHomeAPI.apps.property.models import PropertyModel


def find_survey_by_activity(activity_id):
    try:
        survey = SurveyModel.objects.get(activity_id = activity_id)
        return survey
    except Exception as ex:
        survey = None
        return survey
    
# def find_property_by_activity(property_id):
#     print(property_id)
#     try:
#         property = PropertyModel.objects.get(title = property_id)
#         return property
#     except Exception as Ex:
#         print(Ex)
#         property = None
#         return property