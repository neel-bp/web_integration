from web_integration import app
from flask import render_template

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('hello.html')

@app.route('/starter',methods=['GET','POST'])
def starter():
    return render_template('starter-kit.html', title='Starter', page_title='Starter Page', breadcrumb_title='starter')