from xivo_dao.resources.utils.search import SearchConfig
from xivo_dao.resources.utils.search import SearchSystem

from workano_confd_licence.licence.model import LicenceModel, SessionModel


survey_config = SearchConfig(
    table=LicenceModel,
    columns={
        'id': LicenceModel.id,
        'ip': LicenceModel.ip,
        'domain': LicenceModel.domain,
    },
    default_sort='id',
)


session_config = SearchConfig(
    table=SessionModel,
    columns={
        'uuid': SessionModel.uuid,
        'tenant_uuid': SessionModel.tenant_uuid,
    },
    default_sort='uuid',
)


survey_search = SearchSystem(survey_config)
session_search = SearchSystem(session_config)

