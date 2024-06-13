# config_manager/crud/configuration.py
from sqlalchemy import select, update, delete
from config_manager.database import database
from config_manager.models.configuration import configuration
from config_manager.schemas.configuration import ConfigurationCreate, ConfigurationUpdate

async def create_configuration(config: ConfigurationCreate):
    query = configuration.insert().values(
        country_code=config.country_code,
        requirements=config.requirements
    )
    await database.execute(query)

async def get_configuration(country_code: str):
    query = select([configuration]).where(configuration.country_code == country_code)
    return await database.fetch_one(query)
# async def get_configuration(country_code: str):
#     query = select([configuration.c.country_code, configuration.c.requirements]).where(configuration.c.country_code == country_code)
#     return await database.fetch_one(query)

async def update_configuration(country_code: str, config: ConfigurationUpdate):
    query = update(configuration).where(configuration.c.country_code == country_code).values(
        requirements=config.requirements
    )
    await database.execute(query)

async def delete_configuration(country_code: str):
    query = delete(configuration).where(configuration.c.country_code == country_code)
    await database.execute(query)
