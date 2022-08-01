from src import db

class ManagementToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)