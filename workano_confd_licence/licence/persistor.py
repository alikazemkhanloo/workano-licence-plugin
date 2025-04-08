from xivo_dao.helpers.persistor import BasePersistor
from xivo_dao.resources.utils.search import CriteriaBuilderMixin
from .model import LicenceModel, SessionModel
from datetime import datetime, timedelta
from sqlalchemy import cast
from sqlalchemy.types import DateTime

class LicencePersistor(CriteriaBuilderMixin, BasePersistor):
    _search_table = LicenceModel

    def __init__(self, session, survey_search, tenant_uuids=None):
        self.session = session
        self.search_system = survey_search
        self.tenant_uuids = tenant_uuids


    def _find_query(self, criteria):
        query = self.session.query(LicenceModel)
        return self.build_criteria(query, criteria)

    def _search_query(self):
        return self.session.query(self.search_system.config.table)


    def get_licence(self, domain):
        query = self.session.query(LicenceModel)
        query.filter(LicenceModel.domain == domain)
        return query.first()


class SessionPersistor(CriteriaBuilderMixin, BasePersistor):
    _search_table = SessionModel

    def __init__(self, session, session_search, tenant_uuids=None):
        self.session = session
        self.search_system = session_search
        self.tenant_uuids = tenant_uuids

    def get_session(self, uuid, tenant_uuid):
        query = self.session.query(SessionModel)
        query = query.filter(SessionModel.uuid == uuid)
        query = query.filter(SessionModel.tenant_uuid == tenant_uuid)
        return query.first()

    # def get_average_survey_all_agents_in_queue(self, tenant_uuid, queue_id, from_date, until_date):
    #     from_date = datetime.fromisoformat(from_date) if isinstance(from_date, str) else from_date
    #     until_date = datetime.fromisoformat(until_date) if isinstance(until_date, str) else until_date
    #     until_date = until_date + timedelta(days=1)  # Include the entire day for until_date

    #     query = self.session.query(SurveyModel)
    #     query = query.filter(SurveyModel.tenant_uuid == tenant_uuid)
    #     query = query.filter(SurveyModel.queue_id == queue_id)
    #     query = query.filter(cast(SurveyModel.timestamp, DateTime) >= from_date)
    #     query = query.filter(cast(SurveyModel.timestamp, DateTime) < until_date)
    #     return query

