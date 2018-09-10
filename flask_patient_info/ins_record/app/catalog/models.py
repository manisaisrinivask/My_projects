from app import db
from datetime import datetime


class Patient(db.Model):
    __tablename__ = 'patient'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer,primary_key=False)
    ssn = db.Column(db.String(10),primary_key=False)
    image = db.Column(db.String(100), unique=True)
    phone_number = db.Column(db.String(10), primary_key=False)
    dob= db.Column(db.DateTime, default=datetime.utcnow())

    ins_id = db.Column(db.Integer, db.ForeignKey('insurance.id'))

    def __init__(self, id,name,age,ssn,phone_number,image,ins_id):
        self.id = id
        self.name = name
        self.age=age
        self.ssn=ssn
        self.phone_number=phone_number
        self.image=image
        self.ins_id=ins_id

    def __repr__(self):
        return 'This id is {},Name is {}'.format(self.id, self.name)


class Insurance(db.Model):
    __tablename__ = 'insurance'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, id,name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'This id is {},Name is {}'.format(self.id, self.name)