from xivo_dao.helpers.db_manager import daosession
from .persistor import SessionPersistor, LicencePersistor
from .search import survey_search, session_search

from datetime import timedelta


@daosession
def _persistor(session, tenant_uuids=None):
    return LicencePersistor(session, survey_search, tenant_uuids)

@daosession
def _sessionPersistor(session, tenant_uuids=None):
    return SessionPersistor(session, session_search, tenant_uuids)


def create(queuefeatures):
    return _persistor().create(queuefeatures)


def put(queuefeatures):
    _persistor().put(queuefeatures)


def delete(queuefeatures):
    _persistor().delete(queuefeatures)


def get(queuefeatures_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).get_by({'id': queuefeatures_uuid})


def get_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).get_by(criteria)


def find(queuefeatures_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).find_by({'id': queuefeatures_uuid})


def find_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_by(criteria)


def search(tenant_uuids=None, **parameters):
    return _persistor(tenant_uuids).search(parameters)


def find_all_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_all_by(criteria)


def edit(queuefeatures):
    _persistor().edit(queuefeatures)

def get_licence(domain):
    return _persistor().get_licence(domain)


def get_session(uuid, tenant_uuid):
    return _sessionPersistor().get_session(uuid, tenant_uuid)
