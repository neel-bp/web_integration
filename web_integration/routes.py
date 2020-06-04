from web_integration import app, rest_link
from flask import render_template, abort
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