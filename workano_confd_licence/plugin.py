import logging

from .licence.resource import LicenceItemResource, LicenceListResource, LicenceResource
from .licence.services import build_survey_service
from .db import init_db

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info("workano licence plugin start loading")
        init_db(
            "postgresql://asterisk:proformatique@localhost/asterisk?application_name=workano-licence-plugin"
        )
        api = dependencies["api"]
        survey_service = build_survey_service()

        # survey
        api.add_resource(
            LicenceResource,
            "/licence/check",
            resource_class_args=(survey_service,)
        )

        api.add_resource(
            LicenceListResource,
            '/licences',
            resource_class_args=(survey_service,)
        )
        api.add_resource(
            LicenceItemResource,
            '/licences/<int:uuid>',
            endpoint='licences',
            resource_class_args=(survey_service,)
        )


        logger.info("!!!!!!!!!!!!! workano licence plugin loaded!!!!")
