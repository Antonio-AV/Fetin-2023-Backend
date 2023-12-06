from flask import Flask, request, jsonify, make_response
import bd
import main

app = Flask(__name__)

dataInput = []
dataInputBD = []

@app.route('/input', methods=['POST'])
def input_data():
    dataInput = request.json
    response = main.calculo(dataInput)
    return response

#
app.run(host='0.0.0.0', port=8080, debug=True)
