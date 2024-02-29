from flask import Flask, jsonify, request

from main import DetectionAnalysis, Diabetes, BoneDiseases, BloodTests, Hormones

import os

app = Flask(__name__)


@app.route('/diabetes', methods=['POST'])
def diabetes():
    result=[]
    if os.path.exists("result.txt"):
        os.remove("result.txt")
        # print("done")
    else:
        print("The file does not exist")
    ke = DetectionAnalysis()
    ke.reset()
    req=request.json
    ke.declare(Diabetes(Ph=float(req['Ph'])), Diabetes(PaO2=int(req['PaO2'])), Diabetes(HCO3=int(req['HCO3'])),
               Diabetes(PCO2=int(req['PCO2'])))
    ke.run()
    readfile = open("result.txt", "r")
    for line in readfile:
        line.replace('\n', '')
        result.append(line.replace('\n', ''))
    readfile.close()
    return jsonify({'result': result})

@app.route('/bone', methods=['POST'])
def bone():
    result = []
    if os.path.exists("result.txt"):
        os.remove("result.txt")
        print("done")
    else:
        print("The file does not exist")
    ke=DetectionAnalysis()
    ke.reset()
    req=request.json
    ke.declare(BoneDiseases(VitD=int(req['VitD'])), BoneDiseases(Caly=int(req['Caly'])), BoneDiseases(Pth=int(req['Pth'])))
    ke.run()
    readfile = open("result.txt", "r")
    for line in readfile:
        line.replace('\n', '')
        result.append(line.replace('\n', ''))
    readfile.close()
    return jsonify({'result': result})

@app.route('/blood', methods=['POST'])
def blood():
    result = []
    if os.path.exists("result.txt"):
        os.remove("result.txt")
        print("done")
    else:
        print("The file does not exist")
    ke=DetectionAnalysis()
    ke.reset()
    req=request.json
    if(req['type']=="Male"):
        ke.declare(BloodTests(HemoglobinM=int(req['Hemoglobin'])), BloodTests(Platelets=int(req['Platelets'])),
                     BloodTests(Leukocyte=int(req['Leukocyte'])))
    elif(req['type'] == "Female"):
        ke.declare(BloodTests(HemoglobinF=int(req['Hemoglobin'])), BloodTests(Platelets=int(req['Platelets'])),
                   BloodTests(Leukocyte=int(req['Leukocyte'])))
    ke.run()
    readfile = open("result.txt", "r")
    for line in readfile:
        line.replace('\n', '')
        result.append(line.replace('\n', ''))
    readfile.close()
    return jsonify({'result': result})

@app.route('/hormones', methods=['POST'])
def hormones():
    result = []
    if os.path.exists("result.txt"):
        os.remove("result.txt")
        print("done")
    else:
        print("The file does not exist")
    ke=DetectionAnalysis()
    ke.reset()
    req=request.json
    if(req['type']=="Children"):
        ke.declare(Hormones(IGFc=float(req['IGF'])), Hormones(FT4=float(req['FT4'])),
                     Hormones(ADH=float(req['ADH'])), Hormones(TSH=float(req['TSH'])), Hormones(PRL=float(req['PRL'])),
                     Hormones(KLS=float(req['KLS'])))
    elif(req['type'] == "Female"):
        ke.declare(Hormones(IGFf=float(req['IGF'])), Hormones(FT4=float(req['FT4'])),
                   Hormones(ADH=float(req['ADH'])), Hormones(TSH=float(req['TSH'])), Hormones(PRL=float(req['PRL'])),
                   Hormones(KLS=float(req['KLS'])))
    elif (req['type'] == "Male"):
        ke.declare(Hormones(IGFm=float(req['IGF'])), Hormones(FT4=float(req['FT4'])),
                   Hormones(ADH=float(req['ADH'])), Hormones(TSH=float(req['TSH'])), Hormones(PRLm=float(req['PRL'])),
                   Hormones(KLS=float(req['KLS'])))
    ke.run()
    readfile = open("result.txt", "r")
    for line in readfile:
        line.replace('\n', '')
        result.append(line.replace('\n', ''))
    readfile.close()
    return jsonify({'result': result})


# web : gunicorn flaskConnect:app
