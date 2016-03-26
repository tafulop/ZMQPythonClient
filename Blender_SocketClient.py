import sys
import zmq
import time
import json
import bge


# sets the target angle to the value
def setTarAng(value):
    cont = bge.logic.getCurrentController()
    own = cont.owner
    own["tarAng"] = value

# returns the ID of the joint
def getJointId():
    cont = bge.logic.getCurrentController()
    own = cont.owner
    return own["joint"]


# Joint data query function
def requestJointData(socket, joint_id):

    # create JSON
    req = json.dumps({'JOINT_ID': joint_id, "MESSAGE_TYPE": "JOINT_DATA_REQ"})

    # send the request to the server
    socket.send_string(req)

    # waiting for response
    resp = socket.recv()

    # convert byte data to string
    str_resp = resp.decode("utf-8")

    # get data from the JSON response
    resp_data = json.loads(str_resp)

    return resp_data


# Reads the angle from the given JSON formatted response data
def getAngleFromResponseData(resp_data):

    angle = resp_data["ANGLE"]

    return angle



# Socket to talk to server
port = "5557"
context = zmq.Context()
socket = context.socket(zmq.REQ)

socket.connect ("tcp://localhost:%s" % port)

# get joint id
joint_id = getJointId()

print("Requesting joint data for " + joint_id)

# Requesting joint data
resp_data = requestJointData(socket, joint_id)

print ("ID: " + resp_data["JOINT_ID"])
print ("ANG: " + str(getAngleFromResponseData(resp_data)))

setTarAng(getAngleFromResponseData(resp_data))
    
socket.close()