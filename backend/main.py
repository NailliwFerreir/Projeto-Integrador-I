from flask import Flask, jsonify, request
from flask_cors import CORS
from calc import validateQuality
from crypto import crypto,descrypt
from database.main import *
app = Flask(__name__)
CORS(app, origins='*')

@app.route('/samples')
def bringSamples():
    samples = printSamples()

    # PARTE DA DESCRIPTOGRAFIA PARA ENVIO 
    mylist = []
    for i in samples:
        mylist.append(list(i))
    for i in mylist:
        quality = '' + i[7]
        quality = descrypt(quality)
        i[7] = quality
    ###########

    return jsonify({"samples": mylist})


@app.route('/sample', methods=['POST'])
def addSamples():
    mp10 = request.json['mp10']
    mp25 = request.json['mp25']
    o3 = request.json['o3']
    co = request.json['co']
    no2 = request.json['no2']
    so2 = request.json['so2']

    # CRIPTOGRAFIA PARA ENVIO AO BANCO
    classification = validateQuality(float(mp10),float(mp25),float(o3),float(co),float(no2),float(so2))
    for x in classification[0]:
        quality = '' + x
    quality = crypto(quality)
    ################

    insertSamplesDb(co, so2, no2, o3, mp25, mp10, quality)
    print(co, so2, no2, o3, mp25, mp10, quality)
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

    # CRIPTOGRAFIA PARA ENVIO AO BANCO
    classification = validateQuality(float(mp10),float(mp25),float(o3),float(co),float(no2),float(so2))
    for x in classification[0]:
        quality = '' + x
    quality = crypto(quality)
    response = updateSamplesDb(id, co, so2, no2, o3, mp25, mp10, quality)
    ################

    response = jsonify(response)
    return response

@app.route('/classificacao',methods=['GET'])
def getClassification():
    avg = averageSamples()
    
    # ADICIONADO PARA VALIDAR SE POSSUI AMOSTRAS REGISTRADAS NO BANCO PARA CALCULO DAS MÉDIAS
    if avg == False:
        avg = ['-','-','-','-','-','-']
        res = [['SEM AMOSTRAS'], ['Não há amostras registradas no banco!']]
    else:
        res = validateQuality(float(avg[0]),float(avg[1]),float(avg[2]),float(avg[3]),float(avg[4]),float(avg[5]))
    ###########################
    
    res = jsonify({"result":res, "average": avg})
    return res


if __name__ == '__main__':
    app.run(debug=True)
