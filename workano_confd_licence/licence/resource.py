from ast import IsNot
import logging
from operator import is_not
from flask_restful import Resource
from wazo_confd.helpers.restful import ItemResource, ListResource
from wazo_confd.auth import required_acl
from flask import  request, url_for
from workano_confd_licence.licence.model import LicenceModel, SessionModel
from workano_confd_licence.licence.schema import LicenceSchema
from . import dao

try:
    from wazo_call_logd.rest_api import AuthResource
except ImportError:
    from wazo_call_logd.http import AuthResource

logger = logging.getLogger(__name__)


class LicenceResource(AuthResource):
    def __init__(self, service):
        self.service = service
        super().__init__()

    def get(self):
        token = request.headers.get('X-Auth-Token')
        tenant = request.headers.get('Wazo-Tenant')
        domain = request.args.get('domain')
        session_uuid = request.args.get('sessionUuid')

        session: SessionModel = dao.get_session(session_uuid, tenant)
        licence: LicenceModel = dao.get_licence(domain)

        if(licence is None):
            return {}
        return {
            'licence_start': licence.licence_start.isoformat(),
            'licence_duration': licence.licence_duration.total_seconds(),
            'company_name': licence.company_name,
            'has_mobile': licence.has_mobile,
            'is_mobile_session': session.mobile,
            'domain': licence.domain,
            'ip': licence.ip,
        }


class LicenceListResource(ListResource):
    schema = LicenceSchema
    model = LicenceModel

    def build_headers(self, model):
        return {}


    @required_acl('confd.licence.create')
    def post(self):
        return super().post()

    @required_acl('confd.licence.read')
    def get(self):
        return super().get()


class LicenceItemResource(ItemResource):
    schema = LicenceSchema
    model = LicenceModel
    has_tenant_uuid = True
    

    @required_acl('confd.licence.read')
    def get(self, uuid):
        return super().get(uuid)

    @required_acl('confd.licence.update')
    def put(self, uuid):
        return super().put(uuid)

    @required_acl('confd.licence.delete')
    def delete(self, uuid):
        return super().delete(uuid)
