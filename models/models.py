from flask import Flask
from flask_sqlalchemy import SQLalchemy
import random


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
db = SQLalchemy(app)

'''The backref parameter creates a reverse relationship between the User model and the CheckingAccount and SavingsAccount models. 
This means that, in addition to being able to access the user associated with a checking or savings account, you can also access the 
checking and savings accounts associated with a user directly from the User model.'''

class user:

    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    checking_accounts = db.relationship('CheckingAccount', backref='user', lazy=True)
    savings_accounts = db.relationship('SavingsAccount', backref='user', lazy=True)

class CheckingAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(10), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class SavingsAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_number = db.Column(db.String(10), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

def generate_random_number(length):
    return random.randint(10**(length-1), (10**length)-1)


