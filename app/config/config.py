import os
from dotenv import load_dotenv

load_dotenv() # Carrega o .env

class Sentings:
    db_host: str = os.getenv("DB_HOST")
    db_name: str = os.getenv("DB_NAME")
    db_user: str = os.getenv("DB_USER")
    db_password: str = os.getenv("DB_PASSWORD")

settings = Sentings()