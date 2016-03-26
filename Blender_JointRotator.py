import bge
import math


# returns the name of the motor
def getMotorName():
    m = getOwner()["joint"]
    return m

# sets the current angle property for debug purposes
def setCurrAng(ang):
    getOwner()["currAng"] = ang

# get local rot axis
def getRotAxis(own):
    axs = own["rotAxis"]
    
    if(axs == "x"):
        return 0
    elif(axs == "y"):
        return 1
    elif(axs == "z"):
        return 2
    else:
        return -1
    
# returns the precision
def getPrecision():
    prec = getOwner()["precision"]
    prec = prec / 2
    return prec
    

# returns the current angle
def getCurrAng():
    jVector = getOwner().localOrientation.to_euler()
    ang = math.degrees(jVector[getRotAxis(getOwner())])
    setCurrAng(ang)
    return ang
          
# returns the target angle
def getTarAng():
    owner = bge.logic.getCurrentController().owner
    ang = owner["tarAng"]
    return ang

# return the owner of the script
def getOwner():
    cont = bge.logic.getCurrentController()
    own = cont.owner
    return own

# rotate in positive direction
def rotPos(xyz):
    xyz = getOwner().localOrientation.to_euler()
    coor = getRotAxis(getOwner())
    if(math.degrees(xyz[0]) < getMaxAng() - 1 ):
        xyz[coor] += math.radians(0.25)
        getOwner().localOrientation = xyz.to_matrix()
    
# rotate in negative direction
def rotNeg(xyz):
    xyz = getOwner().localOrientation.to_euler()
    coor = getRotAxis(getOwner())
    if(math.degrees(xyz[0]) > getMinAng() + 1):
        xyz[coor] -= math.radians(0.25)
        getOwner().localOrientation = xyz.to_matrix()


# get current vector
jVector = getOwner().localOrientation.to_euler()

# get max angle
def getMaxAng():
    ang = getOwner()["maxAng"]
    return ang

# get max angle
def getMinAng():
    ang = getOwner()["minAng"]
    return ang

# get current vector
jVector = getOwner().localOrientation.to_euler()

# getting precision
prec = getPrecision()

# physical constraint
if(getCurrAng() >= getMinAng() and getCurrAng() <= getMaxAng()):
    if(getTarAng() < getCurrAng() - prec):
        rotNeg(jVector)
        print("Current: ", getCurrAng())
    elif(getTarAng() > getCurrAng() + prec):
        rotPos(jVector)
    else:
        print("Position has been set for ", getMotorName())    