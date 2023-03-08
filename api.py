from flask import Flask
from isolationForest import *

app = Flask(__name__)

@app.route('/')
def status():
    return jsonify(status = 200)

@app.route('/output')
def get_output():
    return get_model_output()
