from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sandbox_user:sandbox_password@flask-api-study-db/sandbox'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)