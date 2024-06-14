# config_manager/api/configuration.py
from fastapi import APIRouter, HTTPException
from config_manager.schemas.configuration import ConfigurationCreate, ConfigurationUpdate, Configuration
from config_manager.crud.configuration import create_configuration, get_configuration, update_configuration, delete_configuration

router = APIRouter()

@router.post("/create_configuration", response_model=Configuration)
async def create_config(config: ConfigurationCreate):
    await create_configuration(config)
    return config

@router.get("/get_configuration/{country_code}", response_model=Configuration)
async def read_config(country_code: str):
    config = await get_configuration(country_code)
    if config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return config

@router.post("/update_configuration/{country_code}", response_model=Configuration)
async def update_config(country_code: str, config: ConfigurationUpdate):
    existing_config = await get_configuration(country_code)
    if existing_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    await update_configuration(country_code, config)
    return {**existing_config, **config.dict()}

@router.delete("/delete_configuration/{country_code}")
async def delete_config(country_code: str):
    existing_config = await get_configuration(country_code)
    if existing_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    await delete_configuration(country_code)
    return {"message": "Configuration deleted successfully"}
