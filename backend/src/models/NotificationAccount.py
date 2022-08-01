from src import db
from datetime import datetime

class NotificationAccount(db.Model):
    __tablename__ = 'notification_account'

    notification_id = db.Column(db.BigInteger, db.ForeignKey('notifications.id'), primary_key=True)
    account_id = db.Column(db.BigInteger, db.ForeignKey('accounts.id'), primary_key=True)

    created_at = db.Column(db.DateTime,default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)

    # relationship
    notifications = db.relationship('Notification', foreign_keys=notification_id),
    accounts = db.relationship('Account', foreign_keys=account_id)

    def __init__(self, notification_id, account_id):
        self.notification_id = notification_id
        self.account_id = account_id