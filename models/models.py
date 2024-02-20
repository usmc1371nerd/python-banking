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

#def checking_account:
# id(random number 9 digit generated)
# username(minium character of 7 or 8)

# def savings_account:
# same as above

#def user
#user name
#user password
#create logic to check and login

