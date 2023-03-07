from concurrent import futures
import grpc 
import csv 
import electricityConsumption_pb2_grpc
from electricityConsumption_pb2 import(
    EConsumptionData,
    EConsumptionResponse
)

econsumption_timeseries = []
with open('meterusage.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader, None)
    for row in reader:
        econsumption_timeseries.append(EConsumptionData(
            timeofConsumption=row[0], meterusage=row[1]))

class ElectricityConsumptionService(
    electricityConsumption_pb2_grpc.ElectricityConsumptionServicer
):
    def GetEConsumptionData(self, request, context):
        return EConsumptionResponse(electricityConsumption=econsumption_timeseries)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    electricityConsumption_pb2_grpc.add_ElectricityConsumptionServicer_to_server(
        ElectricityConsumptionService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination() 

if __name__ == "__main__":
    serve()

    