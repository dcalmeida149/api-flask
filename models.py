
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from datetime import datetime

class MyData(db.Model):
    __tablename__ = 'my_data'
    id = db.Column(db.Integer, primary_key=True)
    field1 = db.Column(db.String, nullable=False)
    field2 = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(datetime.timezone.utc))

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2


class MyLog(db.Model):
    __tablename__ = 'my_log'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String, nullable=False)
    table_name = db.Column(db.String, nullable=False)
    action = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now)