from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ninggagaga'

from web_integration import routes
