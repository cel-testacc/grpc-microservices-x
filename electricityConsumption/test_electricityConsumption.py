import unittest
from electricityConsumption import ElectricityConsumptionService
from electricityConsumption_pb2 import EConsumptionRequest 

class TestElectricConsumptionData(unittest.TestCase):
    def test_grpc_response(self):
        service = ElectricityConsumptionService()
        ecresponse = service.GetEConsumptionData(EConsumptionRequest(), None)
        econsumption_arr = []
        for ecr in ecresponse.electricityConsumption:
            econsumption_arr.append([ecr.timeofConsumption, ecr.meterusage])
        checkrow = ['2019-01-31 23:45:00', '54.36']
        self.assertIn(checkrow, econsumption_arr)
        
if __name__ == '__main__':
    unittest.main()