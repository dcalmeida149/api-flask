
import json

with open('secrets.json') as f:
    secrets = json.load(f)

class Config:
    SQLALCHEMY_DATABASE_URI = secrets['DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 10,
        'max_overflow': 20,
        'pool_timeout': 30,
        'pool_recycle': 1800,
    }
    APP_SECRET = secrets['APP_SECRET']
