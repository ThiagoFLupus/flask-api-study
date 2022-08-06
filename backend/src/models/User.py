from src import db
from datetime import datetime

class User(db.Model):
    __tablename__= 'users'

    id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)    

    # valores possíveis para coluna abaixo
    # 1- ADMIN
    # 2- MANAGEMENT
    # 3- COMMON
    permission_level = db.Column(db.Enum('1', '2', '3', name='level'), nullable=False)
    account_id = db.Column(db.BigInteger, db.ForeignKey('accounts.id'), nullable=False)

    created_at = db.Column(db.DateTime,default=datetime.utcnow(), nullable=False)

    # relationship     
    # accounts = db.relationship('Account', foreign_keys=account_id)    

    def __init__(self, email, name, password, permission_level, account_id):
        self.email = email
        self.name = name
        self.password = password
        self.permission_level = permission_level
        self.account_id = account_id

    def __repr__(self):
        return "<User %r>" % self.email