from os import environ

import databases

DB_USER = environ.get("DB_USER", "my_service")
DB_PASSWORD = environ.get("DB_PASSWORD", "")
DB_HOST = environ.get("DB_HOST", "0.0.0.0")
DB_NAME = "storageInvDtb"

SQLALCHEMY_DATABASE_URL = (
     f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
)
database = databases.Database(SQLALCHEMY_DATABASE_URL)
