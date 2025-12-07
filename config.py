
import json
import os

with open('secrets.json') as f:
    secrets = json.load(f)

class Config:
    # SQLite database file in the project root
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "database.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APP_SECRET = secrets['APP_SECRET']
