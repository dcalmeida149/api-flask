
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MyData(db.Model):
    __tablename__ = 'my_data'
    id = db.Column(db.Integer, primary_key=True)
    field1 = db.Column(db.String, nullable=False)
    field2 = db.Column(db.String, nullable=False)
    # Adicione mais campos conforme necessário
