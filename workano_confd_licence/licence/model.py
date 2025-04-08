from __future__ import unicode_literals

from sqlalchemy.schema import (
    Column,
    PrimaryKeyConstraint,
)

from sqlalchemy.sql.schema import CheckConstraint
from sqlalchemy.types import Integer, String, Text, Enum, Date, Interval, Boolean
from sqlalchemy.dialects.postgresql import ARRAY

from xivo_dao.alchemy import enum
from xivo_dao.helpers.db_manager import Base, UUIDAsString


from ..db import Base


class LicenceModel(Base):
    __tablename__ = "plugin_licence"

    id = Column(Integer, nullable=False)
    tenant_uuid = Column(UUIDAsString(36), nullable=False)
    company_name = Column(String(100), nullable=True)
    ip = Column(String(15), nullable=True)
    domain = Column(String(50), nullable=True)
    licence_start = Column(Date(), nullable=True)
    licence_duration = Column(Interval(), nullable=True)
    has_mobile = Column(Boolean(), nullable=True)

    __table_args__ = (PrimaryKeyConstraint("id"),)




class SessionModel(Base):
    __tablename__ = "auth_session"

    tenant_uuid = Column(UUIDAsString(36), nullable=False)
    uuid = Column(UUIDAsString(36), nullable=False)
    mobile = Column(Boolean())

    __table_args__ = (PrimaryKeyConstraint("uuid"),)
