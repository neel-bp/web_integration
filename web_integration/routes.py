from web_integration import app, rest_link
from flask import render_template, abort, request
import requests
from web_integration.utilfuncs import time_con

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('hello.html')

@app.route('/starter',methods=['GET','POST'])
def starter():
    return render_template('starter-kit.html', title='Starter', page_title='Starter Page', breadcrumb_title='starter')

@app.route('/patients', methods=['GET'])
def patients():
    r = requests.get(f'{rest_link}/patients')
    if r.status_code != 200:
        abort(500)
    patient_list = r.json()
    return render_template('patients.html',title='Patients',page_title='Patients',breadcrumb_title='Patients',patient_list=patient_list, time_con=time_con,rest_link=rest_link)

@app.route('/patients/<patient_id>', methods=['GET','POST'])
def patient(patient_id):
    if request.method == 'GET':
        r = requests.get(f'{rest_link}/patients/{patient_id}')
        if r.status_code == 404:
            abort(404)
        if r.status_code != 200:
            abort(500)
        patient_data = r.json()
        try:
            address = patient_data['address']
            address = f'{address["country"]} {patient_data["city"]} {patient_data["street"]}'
        except:
            address = ""
        return render_template('patient.html', patient_data=patient_data, title=f'{patient_data["name"]} {patient_data["surname"]}', rest_link=rest_link, time_con=time_con, address=address, breadcrumb_title=f'{patient_data["name"]} profile')

@app.route('/doctors', methods=['GET'])
def doctors():
    r = requests.get(f'{rest_link}/doctors')
    if r.status_code != 200:
        abort(500)
    doctor_list = r.json()
    return render_template('doctors.html',title='Doctors',page_title='Doctors',breadcrumb_title='Doctors',doctor_list=doctor_list, time_con=time_con,rest_link=rest_link)