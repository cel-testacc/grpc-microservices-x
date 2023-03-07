# grpc-microservices-x
## Dependencies
The project requires several dependencies that can all be installed via pip:
- [grpcio] 
- [grpcio-tools] 
- [flask] 
- [flask-cors] 
## Running the project

To run the project, in a terminal window, navigate to the project directory then 
```sh
cd electricityConsumption
python electricityConsumption.py
```
In another terminal window, navigate to the project directory again then
```sh
cd requestdata
FLASK_APP=requestdata.py flask run
```
You can view the JSON output via the link
```sh
http://127.0.0.1:5000/getECData
```
To view the JSON API request in action, simply double-click the index.html file attached.
> Note: Simple unit tests have also been added to ensure that the data is passed accurately. They are located in the directories and can be called via generic python call.
## How It Was Built
- The protocol buffer facade responsible for handling the data provided is located in the protobufs folder.
- The main language used to create both the grpc client and server is Python.
- The electricityConsumption.py file begins the process by parsing the input csv and preparing the service by opening a port and waiting for data to be requested.
- The grpc client, located in the requestdata directory, is an application written using the Flask framework. It accepts the data transmitted from the open grpc server and returns the data via the /getECData endpoint as a JSON string. 
- The index.html file shows the cumulative output of the grpc client-server data transfer by displaying the structured data called from the HTTP /getECData endpoint. The file uses javascript to receive and parse the HTTP call and then dynamically append the data so it can be viewed in HTML. 
## License
GPL-3.0
