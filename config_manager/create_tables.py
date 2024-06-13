# # config_manager/create_tables.py
# from sqlalchemy import create_engine
# from config_manager.models.configuration import configuration
# from config_manager.database import DATABASE_URL

# engine = create_engine(DATABASE_URL)
# metadata.create_all(engine)
# import sys
# sys.path.append('../')
import sys
import os

# Add the root directory of the project to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlalchemy import create_engine
from config_manager.database import DATABASE_URL, metadata
from config_manager.models.configuration import configuration


engine = create_engine(DATABASE_URL)
metadata.create_all(engine)
