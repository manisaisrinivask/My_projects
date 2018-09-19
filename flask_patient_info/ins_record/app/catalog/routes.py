from app.catalog import main
from app import db
from app.catalog.models import Patient,Insurance
from flask import render_template,request



@main.route("/")
def index():
    return render_template('home1.html')


@main.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    patients = Patient.query.all()
    forward_message = "Moving Forward..."
    return render_template('home.html', patients=patients)


@main.route("/forwardinsurance/", methods=['POST'])
def insurance_forward():
    insurances = Insurance.query.all()
    forward_message = "Going on....."
    return render_template('homeinsurance.html', insurances=insurances)

