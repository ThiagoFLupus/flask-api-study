from src import db
from datetime import datetime

class Notification(db.Model):
    __tablename__ = 'notifications'

    id = db.Column(db.BigInteger, primary_key=True)
    message = db.Column(db.Text, nullable=False)

    created_at = db.Column(db.DateTime,default=datetime.utcnow(), nullable=False)

    # relationship
    accounts = db.relationship('NotificationAccount')

    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return "<Notification %r>" % self.id