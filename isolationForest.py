from flask import jsonify

def get_model_output():
    data = jsonify(time = '-', sensor = '-', value = '-', probability = '-')
    return data


