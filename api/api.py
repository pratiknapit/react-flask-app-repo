from flask import Flask 
import time 
from datetime import date

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': date.today()}

    