from os import name, spawnl
import re
from datetime import date
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta, date
import flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = 'thisissecret'

db = SQLAlchemy(app)


class bodycheckup(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(30))
    Heartbeat = db.Column(db.String(30))
    Spo2 = db.Column(db.String(30))
    # Spo2 = db.Column(db.Integer)
    sleep = db.Column(db.String(100))
    diabetes = db.Column(db.String(30))
    today = date.today()
    datejoined = db.Column(db.DateTime, default=today)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.Name}"


class Registration(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)
    email = db.Column(db.String(200))
    dob = db.Column(db.String(200))
    gender = db.Column(db.String(200))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(200))
    guardianName = db.Column(db.String(200))
    guardianage = db.Column(db.Integer)
    guardianRelation = db.Column(db.String(200))
    guardianaddress = db.Column(db.String(200))
    guardianage = db.Column(db.Integer)
    guardianphone = db.Column(db.String(200))
    today = date.today()
    datejoined = db.Column(db.DateTime, default=today)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.name}"


class Guardianaddmemberlist(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    guardianName = db.Column(db.String(200))
    guardianage = db.Column(db.Integer)
    guardianRelation = db.Column(db.String(200))
    guardianaddress = db.Column(db.String(200))
    guardianage = db.Column(db.Integer)
    guardianphone = db.Column(db.String(200))
    today = date.today()
    datejoined = db.Column(db.DateTime, default=today)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.guardianName}"


def funbodycheckup():
    data = bodycheckup(Name='Rohan', Heartbeat='69',
                       Spo2='99', sleep='7 hours', diabetes='no')
    db.session.add(data)
    db.session.commit()
    Rdata = Registration(name='Rohan', age=22, email='rohan22@gmail.com', dob='16 jan', gender='male', address='123 Main Street, New York, NY 10030', phone="9561236038",
                         guardianName='feddrick', guardianage=50, guardianRelation='Father', guardianaddress='123 Main Street, New York, NY 10030', guardianphone='9561236037')
    db.session.add(Rdata)
    db.session.commit()
    return flask.redirect("/")


@app.route('/')
def home():
    Users = Registration.query.all()
    Patientupdatedata = bodycheckup.query.all()
    Guardianaddmember = Guardianaddmemberlist.query.all()
    try:
        print(Users[0])
    except:
        funbodycheckup()
        home()
    return render_template('index.html', Users=Users, lastcheckupdata=Patientupdatedata[-1], userlogin=Users[-1], Guardianaddmember=Guardianaddmember)
        # return render_template('index.html', Users=Users, lastcheckupdata=Patientupdatedata[-1], userlogin=Users[-1], Guardianaddmember=Guardianaddmember)


@app.route('/<string:name>', methods=['GET', 'POST'])
def userpage(name):
    Users = Registration.query.all()
    Patientupdatedata = bodycheckup.query.all()
    Guardianaddmember = Guardianaddmemberlist.query.all()
    for data in Users:
        if(data.name == name or name in data.name):
            print('yes')
            return render_template('index.html', Users=Users, lastcheckupdata=Patientupdatedata[-1], userlogin=data, Guardianaddmember=Guardianaddmember)
        
    return flask.redirect('/')


@app.route('/bot', methods=['GET', 'POST'])
def bot():
    Users = Registration.query.all()
    Patientupdatedata = bodycheckup.query.all()
    return render_template('chattingbot.html', Users=Users, lastcheckupdata=Patientupdatedata[-1], userlogin=Users[-1])


@app.route('/morningexercise', methods=['GET', 'POST'])
def mornignexercise():
    Users = Registration.query.all()
    Patientupdatedata = bodycheckup.query.all()
    Guardianaddmember = Guardianaddmemberlist.query.all()
    try:
        print(Users[0])
        return render_template('morningexercise.html', Users=Users, lastcheckupdata=Patientupdatedata[-1], userlogin=Users[-1],Guardianaddmember=Guardianaddmember)
    except:
        funbodycheckup()
        return render_template('morningexercise.html', Users=Users, lastcheckupdata=Patientupdatedata[-1], userlogin=Users[-1],Guardianaddmember=Guardianaddmember)
        
@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    Users = Registration.query.all()
    Patientupdatedata = bodycheckup.query.all()
    Guardianaddmember = Guardianaddmemberlist.query.all()
    try:
        print(Users[0])
        return render_template('gallery.html', Users=Users, lastcheckupdata=Patientupdatedata[-1], userlogin=Users[-1],Guardianaddmember=Guardianaddmember)
    except:
        funbodycheckup()
        return render_template('gallery.html', Users=Users, lastcheckupdata=Patientupdatedata[-1], userlogin=Users[-1],Guardianaddmember=Guardianaddmember)

@app.route('/about', methods=['GET', 'POST'])
def About():
    Users = Registration.query.all()
    Patientupdatedata = bodycheckup.query.all()
    Guardianaddmember = Guardianaddmemberlist.query.all()
    try:
        print(Users[0])
        return render_template('about.html', Users=Users, lastcheckupdata=Patientupdatedata[-1], userlogin=Users[-1],Guardianaddmember=Guardianaddmember)
    except:
        funbodycheckup()
        return render_template('about.html', Users=Users, lastcheckupdata=Patientupdatedata[-1], userlogin=Users[-1],Guardianaddmember=Guardianaddmember)

@app.route('/fullbodychckup', methods=['GET', 'POST'])
def fullbodychckup():
    Name = request.form.get('Name')
    Bpm = request.form.get('bpm')
    Spo2 = request.form.get('percentO2')
    Sleep = request.form.get('sleepcycle')
    diabetesY = request.form.get('DiabetesY')
    print(Name, Bpm, Spo2, Sleep, diabetesY)

    # return render_template('index.html')
    data = bodycheckup(Name=Name, Heartbeat=Bpm, Spo2=Spo2,
                       sleep=Sleep, diabetes=diabetesY)
    db.session.add(data)
    db.session.commit()

    return flask.redirect("/")


@app.route('/newregister', methods=['GET', 'POST'])
def newregister():
    name = request.form.get('name')
    age = request.form.get('age')
    email = request.form.get('email')
    dob = request.form.get('dob')
    gender = request.form.get('gender')
    address = request.form.get('address')
    phone = request.form.get('phone')
    guardianName = request.form.get('guardianName')
    guardianage = request.form.get('guardianage')
    guardianRelation = request.form.get('guardianRelation')
    guardianaddress = request.form.get('guardianaddress')
    guardianphone = request.form.get('guardianphone')
    Rdata = Registration(name=name, age=age, email=email, dob=dob, gender=gender, address=address, phone=phone, guardianName=guardianName,
                         guardianage=guardianage, guardianRelation=guardianRelation, guardianaddress=guardianaddress, guardianphone=guardianphone)
    db.session.add(Rdata)
    db.session.commit()
    return render_template('bodycheck.html', patiantname=name)

@app.route('/newguardianmember', methods=['GET', 'POST'])
def newmember():
    guardianName = request.form.get('guardianName')
    guardianage = request.form.get('guardianage')
    guardianRelation = request.form.get('guardianRelation')
    guardianaddress = request.form.get('guardianaddress')
    guardianphone = request.form.get('guardianphone')
    Rdata = Guardianaddmemberlist( guardianName=guardianName,
                         guardianage=guardianage, guardianRelation=guardianRelation, guardianaddress=guardianaddress, guardianphone=guardianphone)
    db.session.add(Rdata)
    db.session.commit()
    return flask.redirect('/')




if __name__ == "__main__":
    app.run(debug=True)
