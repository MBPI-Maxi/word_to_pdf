# connect the database here
# using the pc workstation here
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.exc import OperationalError
from os import getenv

load_dotenv()

is_connected = False
engine = None

def load_env():
    if getenv("ENVIRONMENT") == "MBPI":
        url = URL.create(
            drivername=getenv("DB_DRIVER"),
            username=getenv("DB_USER"),
            host=getenv("DB_HOST"),
            database=getenv("DB_NAME"),
            port=getenv("DB_PORT"),
            password=getenv("DB_PASSWORD")
        )
    else:
        raise ValueError("Environment not valid")

    return url

def process():
    global is_connected
    global engine

    url_env = load_env()
    engine = create_engine(url_env)
    
    try:
        with engine.connect() as conn:
            is_connected = True
    except OperationalError as e:
        is_connected = str(e)

process()