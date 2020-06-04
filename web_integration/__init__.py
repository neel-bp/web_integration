from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ninggagaga'
rest_link = 'http://127.0.0.1:8080'

from web_integration import routes
