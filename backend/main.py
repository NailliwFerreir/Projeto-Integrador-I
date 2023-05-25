from flask import Flask, jsonify, request
from flask_cors import CORS
from calc import validateQuality
from database.main import *
app = Flask(__name__)
CORS(app, origins='*')

@app.route('/samples')
def bringSamples():
    samples = printSamples()
    return jsonify({"samples": samples})


@app.route('/sample', methods=['POST'])
def addSamples():
    mp10 = request.json['mp10']
    mp25 = request.json['mp25']
    o3 = request.json['o3']
    co = request.json['co']
    no2 = request.json['no2']
    so2 = request.json['so2']
    insertSamplesDb(co, so2, no2, o3, mp25, mp10)
    print(co, so2, no2, o3, mp25, mp10)
    return {"status": "success"}

@app.route('/samples/<id>', methods=['DELETE'])
def deleteSamples(id):
    response = deleteSamplesDb(id)
    response = jsonify(response)
    return response

@app.route('/sample/<id>', methods=['PUT'])
def updateSample(id):
    mp10 = request.json['mp10']
    mp25 = request.json['mp25']
    o3 = request.json['o3']
    co = request.json['co']
    no2 = request.json['no2']
    so2 = request.json['so2']
    response = updateSamplesDb(id, co, so2, no2, o3, mp25, mp10)
    response = jsonify(response)
    return response

@app.route('/classificacao',methods=['GET'])
def getClassification():
    avg = averageSamples()
    res = validateQuality(float(avg[0]),float(avg[1]),float(avg[2]),float(avg[3]),float(avg[4]),float(avg[5]))
    res = jsonify({"result":res, "average": avg})
    return res


if __name__ == '__main__':
    app.run(debug=True)
