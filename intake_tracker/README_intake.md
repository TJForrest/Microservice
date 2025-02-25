# Utilizing the stats to graph intake tracker
## Sending 
Socket connection needs to be established utilizing zmq structure 
- Must include 
```python
import zmq
```
- Establish socket using 
  ```python
socket = context.socket(zmq.REQ)`
```
- Connect socket to localhost and free port 
  ```python
socket.connect("tcp://localhost:5557")
```

Sent data needs to be in JSON format matching the following structure 
1. Labels - Days of the week or months
2. Protein - Quantity of intake (per day, per month)
3. Water - Quantity of intake (per day, per month)
4. Pre workout - Quantity of intake (per day, per month)

The JSON formatting can be built in program or be pulled from an existing file 
- To use an existing file 
	- Open file to read and store the data in a variable
```python
with open("test.json", "r") as file:
	json_data = json.load(file)
```
- To build in program 
	- Set the variable to be in JSON format
```python
json_data = {
        "labels": ["Monday", "Tuesday", "Wednesday"],
    "protein": [50, 60,45],
    "water": [100,110,99],
    "pre": [5, 7, 4]
}
```

Send the data via socket to the microservice 
```python 
socket.send_json(json_data)
```


## Receiving the graph 
While maintaining the same socket connection 
Receive via socket connection the .png data
```python 
png_data = socket.recv() 
```
Once the data has been received it can be saved to the local directory or used as needed
Ex. - Saved to dir 
```python 
with open("graph.png", "wb") as file:
	file.write(png_data)
print("File saved as 'graph.png'")
```



# UML Diagram 
![[UML.png|600]]



## Mitigation Plan 
**Microservice built for**: Kaija Shreeve 
**Current Status**: Working. At time of submission the API response time are >20 mins to receive a graph. When initially built and tested response times were <5 seconds
**Parts not done:** Color pallet selection. Colors are hard coded and need to be adjusted to match a main programs theme. 
**Access:** From git hub repo INSERT LINK HERE. 
**Issues:** Can message on discord any time and will get back to you in under 24hrs. With the exception of 02/26 after 6pm, and 03/01 all day. 
**Issues timeline:** As soon as you run into any issues. 
**Other issues:** If there continues to be issues with quickgraphs.io I've found a few alternatives to try but the turn around on this size of a rework this week will not be the fastest. 