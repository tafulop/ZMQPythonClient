import sys
import zmq
import time
import re
import json


# Socket to talk to server
port = "5557"
context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect ("tcp://localhost:%s" % port)


message = json.dumps({'JOINT_ID': 'J1', "MESSAGE_TYPE": "JOINT_DATA_REQ"})

try:
#time.sleep(0.05)
    #string = socket.recv(flags=zmq.NOBLOCK)

    # Requesting joint data
    print("Sending query...")
    string = socket.send(message)
    print("Sending hello... DONE.")

    # Get the reply
    print("Waiting for message...")
    message = socket.recv()
    print("Received: " + message)

    data = json.loads(message) 
    
    print ("ID: " + data["JOINT_ID"])
    print ("ANG: " + str(data["ANGLE"]))


except:
    i = 1
    
socket.close()