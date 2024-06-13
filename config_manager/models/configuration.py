# config_manager/models/configuration.py
from sqlalchemy import Table, Column, String, MetaData
from . import metadata

configuration = Table(
    "configurations",
    metadata,
    Column("country_code", String(2), primary_key=True),
    Column("requirements", String, nullable=False)
)
