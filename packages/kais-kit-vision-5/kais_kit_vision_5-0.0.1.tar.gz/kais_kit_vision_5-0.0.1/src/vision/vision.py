""" Vision System interface - main
 
 
@author:    kais, misil.
@created:   2024-07-03

"""
import package.common
import package.roblang as rob
import package.visionfunc
import package.socketfunc

def attr_names():
    """Returns the names of the attributes to be exposed."""
    return ("ip_addr", "port")


def CalibStart():
    rob.CalibStart()
    
def CalibX():
    rob.CalibX()

def CalibEnd():
    rob.CalibEnd()

def ModelLeg():
    rob.ModelLeg()
    
def ModelPos():
    rob.ModelPos()
    
def Trigger():
    rob.Trigger()
    
    
print(CalibStart())