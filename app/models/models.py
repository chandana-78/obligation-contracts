from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50))

class Obligation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    type = db.Column(db.String(50))
    due_date = db.Column(db.Date)
    assigned_to = db.Column(db.String(100))
    status = db.Column(db.String(50))
    document_path = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
