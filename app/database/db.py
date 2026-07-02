import psycopg2
from app.config import settings

def getConnection():
    return psycopg2.connect(
        dbname = settings.db_name,
        user = settings.db_user,
        password = settings.db_password,
        host = settings.db_host
    )