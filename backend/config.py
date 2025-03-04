import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    SECRET_KEY = os.getenv('SECRET_KEY')
    DATABASE_URL = os.getenv('DATABASE_URL')
    FIRST_SUPERUSER_EMAIL = os.getenv('FIRST_SUPERUSER_EMAIL')
    FIRST_SUPERUSER_PASSWORD = os.getenv('FIRST_SUPERUSER_PASSWORD')

config = Config()
