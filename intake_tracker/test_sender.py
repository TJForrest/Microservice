# test_sender.py 
# Sends a test file to intake_to_graph

# Imports ZeroMQ library for socket conection functions
import zmq  
# Imports JSON library for json connection functions 
import json 

# Set up socket 
context = zmq.Context() 

# socket to server (micro) 
print("Connecting to Server...")
socket = context.socket(zmq.REQ) 

# Socket port change as needed if port is in use. 
socket.connect("tcp://localhost:5557")

# Opens JSON file to read data
with open("test.json","r") as file: 
	json_data = json.load(file)

# Send the data from the JSON via zmq 	
print("Sending JSON date over") # Status message 
socket.send_json(json_data) 


# Get PNG back from the server
png_data = socket.recv()


# Check file was received else show error
if png_data != b"ERROR":
	with open("graph.png", "wb") as file: 
		file.write(png_data) 
	print("File saved as 'graph.png'") 
else: 
	print("Error -- this aint working!") 

