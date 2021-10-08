from os import name
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, session
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from datetime import datetime, timedelta, date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'thisissecret'

db = SQLAlchemy(app)


class bodycheckup(UserMixin, db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(30))
    Heartbeat = db.Column(db.String(30))
    Spo2 = db.Column(db.String(30))
    # Spo2 = db.Column(db.Integer)
    sleep = db.Column(db.String(100))
    diabetes = db.Column(db.String(30))
    date = db.Column(db.DateTime, default=datetime.utcnow)


class Registration(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    email = db.Column(db.String(200))
    dob = db.Column(db.String(200))
    gender = db.Column(db.String(200))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(200))
    guardian = db.Column(db.String(200))
    guardianName = db.Column(db.String(200))
    guardianage = db.Column(db.Integer)
    guardianRelation = db.Column(db.String(200))
    guardianarress = db.Column(db.String(200))
    guardianphone = db.Column(db.String(200))
    datejoined = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"


@app.route('/bodycheck')
def bodycheck():
    data = bodycheckup(Name='Ayush', Heartbeat='22', Spo2='12', sleep='7 hours', diabetes='no')
    db.session.add(data)
    db.session.commit()
    Rdata = Registration(name='Ayush', age=22, email='123@gmail.com', dob='16 sept', gender='qwertt',address='1234rtgfdertgvfdertgbvdergv',phone="1234546789",guardian='family',guardianName='qwerty',guardianage=11,guardianRelation='qwert',guardianarress='wqerfgh',guardianphone='asdf')
    db.session.add(Rdata)
    db.session.commit()
    return render_template('indexcopy.html')

@app.route('/')
def home():
    return render_template('indexcopy.html')

@app.route('/fullbodychckup', methods=['GET', 'POST'])
def fullbodychckup():
    Name = request.form.get('Name')
    Bpm = request.form.get('bpm')
    Spo2 = request.form.get('percentO2')
    Sleep =  request.form.get('sleepcycle')
    diabetesY = request.form.get('DiabetesY')
    print(Name,Bpm,Spo2,Sleep,diabetesY)
        # return render_template('indexcopy.html')

    return render_template('indexcopy.html')


if __name__ == "__main__":
    app.run(debug=True)
