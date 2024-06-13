# config_manager/schemas/configuration.py
from pydantic import BaseModel

class ConfigurationBase(BaseModel):
    country_code: str
    requirements: str

class ConfigurationCreate(ConfigurationBase):
    pass

class ConfigurationUpdate(BaseModel):
    requirements: str

class Configuration(ConfigurationBase):
    class Config:
        # orm_mode = True
        from_attributes = True
class ConfigurationResponse(ConfigurationBase):
    country_code: str
    requirements: str

    class Config:
        from_attributes = True
