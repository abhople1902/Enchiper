from flask import Flask, request, jsonify, render_template, redirect
import requests
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime, timedelta,date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'thisissecret'

db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    Name = db.Column(db.Integer, primary_key=True)
    Heartbeat = db.Column(db.String(30))
    Spo2 = db.Column(db.Integer)
    sleep = db.Column(db.String(100))   
    diabetes = db.Column(db.String(30))
    date = db.Column(db.DateTime, default=datetime.utcnow)

class Registration(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    guardianName = db.Column(db.String(200))
    guardianage = db.Column(db.Integer)
    guardianRelation = db.Column(db.String(200))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"

@app.route('/')
def home():
    return render_template('index copy.html')





if __name__ == "__main__":
    app.run(debug=True)
