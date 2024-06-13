# config_manager/api/configuration.py
from fastapi import APIRouter, HTTPException
from config_manager.schemas.configuration import ConfigurationCreate, ConfigurationUpdate, Configuration
from config_manager.crud.configuration import create_configuration, get_configuration, update_configuration, delete_configuration
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request
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
# Add this in config_manager/api/configuration.py


# @router.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=400,
#         content={"detail": exc.errors()}
#     )

# @router.exception_handler(Exception)
# async def general_exception_handler(request: Request, exc: Exception):
#     return JSONResponse(
#         status_code=500,
#         content={"detail": str(exc)}
#     )
