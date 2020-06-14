from web_integration import app, rest_link
from flask import render_template, abort, request, flash, redirect, url_for
import requests
from web_integration.utilfuncs import time_con

# test routes
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('hello.html')

# test routes
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
    
    elif request.method == 'POST':
        payload = dict(request.form)
  
        for pl in list(payload.keys()):
            if payload[pl] == '':
                payload.pop(pl, None)

        r = requests.put(f'{rest_link}/patients/{patient_id}', json=payload)
        if r.status_code != 200:
            print(f'{r.status_code} {payload}')
            flash('Profile update failed', 'danger')
            return redirect(url_for('patient',patient_id=patient_id))
        else:
            flash('Profile successfully updated', 'success')
            return redirect(url_for('patient',patient_id=patient_id))
    
            

@app.route('/doctors', methods=['GET'])
def doctors():
    r = requests.get(f'{rest_link}/doctors')
    if r.status_code != 200:
        abort(500)
    doctor_list = r.json()
    return render_template('doctors.html',title='Doctors',page_title='Doctors',breadcrumb_title='Doctors',doctor_list=doctor_list, time_con=time_con,rest_link=rest_link)

@app.route('/doctors/<doctor_id>', methods=['GET','POST'])
def doctor(doctor_id):
    if request.method == 'GET':
        r = requests.get(f'{rest_link}/doctors/{doctor_id}')
        if r.status_code == 404:
            abort(404)
        if r.status_code != 200:
            abort(500)
        doctor_data = r.json()
        try:
            address = doctor_data['address']
            address = f'{address["country"]} {doctor_data["city"]} {doctor_data["street"]}'
        except:
            address = ""
        return render_template('doctor.html', doctor_data=doctor_data, title=f'{doctor_data["name"]} {doctor_data["surname"]}', rest_link=rest_link, time_con=time_con, address=address, breadcrumb_title=f'{doctor_data["name"]} profile')
    
    elif request.method == 'POST':
        payload = dict(request.form)
  
        for pl in list(payload.keys()):
            if payload[pl] == '':
                payload.pop(pl, None)

        r = requests.put(f'{rest_link}/doctors/{doctor_id}', json=payload)
        if r.status_code != 200:
            print(f'{r.status_code} {payload}')
            flash('Profile update failed', 'danger')
            return redirect(url_for('doctor',doctor_id=doctor_id))
        else:
            flash('Profile successfully updated', 'success')
            return redirect(url_for('doctor',doctor_id=doctor_id))

@app.route('/documents', methods=['GET'])
def documents():
    r = requests.get(f'{rest_link}/documents')
    if r.status_code != 200:
        abort(500)
    document_list = r.json()
    return render_template('documents.html',title='documents',page_title='documents',breadcrumb_title='documents',document_list=document_list, time_con=time_con,rest_link=rest_link)

@app.route('/doctors/<doctor_id>/documents/<document_id>', methods=['GET','POST'])
def document(document_id, doctor_id):
    if request.method == 'GET':
        r = requests.get(f'{rest_link}/doctors/{doctor_id}/documents/{document_id}')
        if r.status_code == 404:
            abort(404)
        if r.status_code != 200:
            abort(500)
        document_data = r.json()
        return render_template('document.html', document_data=document_data, title=f'{document_data["title"]}', rest_link=rest_link, time_con=time_con, breadcrumb_title=f'{document_data["title"]}')