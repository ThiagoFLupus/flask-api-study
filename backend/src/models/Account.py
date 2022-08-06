from src import db
from .User import User
from .NotificationAccount import NotificationAccount
from datetime import datetime

class Account(db.Model):
    __tablename__ = 'accounts'

    id = db.Column(db.BigInteger, primary_key=True)
    business_name = db.Column(db.String(100), nullable=False)

    # valores possíveis para a coluna abaixo
    # 1- temporaty
    # 2- active
    # 3- inactive
    status = db.Column(db.Enum('1', '2', '3', name='status'), nullable=False)

    created_at = db.Column(db.DateTime,default=datetime.utcnow(), nullable=False)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)

    # relationship
    users = db.relationship('User', backref='accounts', lazy=True)
    # notifications = db.relationship('NotificationAccount')
    notifications = db.relationship('Notification', secondary='notification_account', lazy='subquery',
        backref=db.backref('accounts', lazy=True))

    def __init__(self, business_name, status):
        self.business_name = business_name
        self.status = status

    def __repr__(self):
        return "<Account %r>" % self.business_name