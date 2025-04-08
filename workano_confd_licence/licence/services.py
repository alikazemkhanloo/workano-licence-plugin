from wazo_confd.helpers.resource import CRUDService

from . import dao
from .notifier import build_survey_notifier
from .validator import build_survey_validator


class SurveyService(CRUDService):
    def __init__(self, dao, validator, notifier, extra_parameters=None):
        super().__init__(dao, validator, notifier, extra_parameters=None)

    def check_licence(self):
        return dao.check_licence()
    

def build_survey_service():
    return SurveyService(dao, build_survey_validator(), build_survey_notifier())
