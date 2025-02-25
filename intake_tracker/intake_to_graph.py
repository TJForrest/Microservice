''' 
Microservice for assignment 8
Receives json file with info, compiles the info into a new file,
sends the file to quick chart API, recevies back a png send the png
to the microservice caller. 

Built Tyler Knudson Forrest 
For
Kaija
'''


'----Imported libraries----'
import time    	# Time Library for time function
import zmq     	# ZeroMQ Library for zmq socket conections 
import json 	# JSON library for json file managment  
import requests # Request lib to send http requests to API 


# zmq socket set up
context = zmq.Context() 
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")


# Server status message
print("-- Server is on and waiting for instructions --") 


while True:
	# Get JSON file from client 
	json_d_recv  = socket.recv_json()
	print(f"Received JSON Data:", json_d_recv)
	
	# http link to send api request
	chart_url = "https://quickchart.io/chart"
	
	# Sets the background color of the whole graph cur white
	bg_color = json_d_recv.get("backgroundColor", "#ffffff")	

	''' Pre builds the structure of the graph
		"Type" = Type of graph
		"Labels" = The title of the graph
		"Datasets" = The data vaules of each level tracked
		"label" = Name of the bar for associated level 
		"Data" = Numerical data value
		"backgroundColor" = Color of the body of the bar 
        "borderColor" = Color of the bars boarder 
        "borderWidth" = size of boarder
	'''	
	chart_config = {
		"type": "bar", 
		"data": {
			"labels": json_d_recv["labels"], 
			"datasets": [{
				"label": "Protein(g)", 
				"data": json_d_recv["protein"],
				"backgroundColor": "rgba(255, 99, 132, 0.2)",
                "borderColor": "rgba(255, 99, 132, 1)",
                "borderWidth": 1
			}, 
			{		
				"label": "Water(oz)", 
				"data": json_d_recv["water"]
			}, 
			{		
				"label": "Pre Workout(Scoops)", 
				"data": json_d_recv["pre"]
			}, 
			
			] 
		},
		"options": {
			"scales": {
				"y": {
					"beginAtZero": True
				}
			}
		}
	}
	
	# Send and get back from api  
	response = requests.get(chart_url, params={
		"c": json.dumps(chart_config)})
 
	# Check that api call is good  
	if response.status_code == 200: 
		print("Graph was built successfully") 
		the_chart = response.content 
		socket.send(the_chart)
		print("File sent") 
	
	 
	else:
		print(f"Error building graph: {response.status_code}") 
		print(response.text) 
		socket.send(b"ERROR") 
 
