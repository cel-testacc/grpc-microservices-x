import os 
import grpc
import json
from flask import Flask
from flask_cors import CORS
from electricityConsumption_pb2_grpc import ElectricityConsumptionStub
from electricityConsumption_pb2 import EConsumptionRequest

app = Flask(__name__)
CORS(app)

econsumption_host = os.getenv("ECONSUMPTION_PLACEHOLDER_HOST", "localhost")
econsumption_channel = grpc.insecure_channel(f"{econsumption_host}:50051")
econsumption_channel = ElectricityConsumptionStub(econsumption_channel)

@app.route("/getECData")
def render_json_response():
    econsumption_response = econsumption_channel.GetEConsumptionData(EConsumptionRequest())
    
    econsumption_arr = []
    for ecr in econsumption_response.electricityConsumption:
        econsumption_arr.append([ecr.timeofConsumption, ecr.meterusage])

    return json.dumps(econsumption_arr)

@app.route("/")
def render_homepage():
    return "<h1>Hello, there's nothing here; <br />if you're looking for the usage data, it's located at <a/>http://127.0.0.1:5000/getECData</a></h1>"
