# # config_manager/create_tables.py
# from sqlalchemy import create_engine
# from config_manager.models.configuration import configuration
# from config_manager.database import DATABASE_URL

# engine = create_engine(DATABASE_URL)
# metadata.create_all(engine)
# import sys
# sys.path.append('../')
import sys
# config_manager/create_tables.py
from sqlalchemy import create_engine
from config_manager.models.configuration import configuration
from config_manager.database import DATABASE_URL

engine = create_engine(DATABASE_URL)
metadata.create_all(engine)
