import json
import loginthingsboard as lt
import mgassets
import mgcustomers
import mgdevices
import time
import json
import os

_TBURL = "https://esc.isi.gr/"
_TBUSER = "alexakos@isi.gr"
_TBPWD = "ei5kGK1*9q1oUoT*"

attributescopes = ["CLIENT_SCOPE","SHARED_SCOPE","SERVER_SCOPE"]
def updatedevices(devices):
    token = lt.gettoken(_TBURL,_TBUSER,_TBPWD)
    for device in devices:
        time.sleep(2)
        devicedata = {}
        for scope in attributescopes:
           data = mgdevices.getdeviceattributesbytoken(
              _TBURL,
              device['id']['entityType'],
              device['id']['id'],
              token,
              scope)
           while data is False:
              time.sleep(5)
              token = lt.gettoken(_TBURL,_TBUSER,_TBPWD)
              data = mgdevices.getdeviceattributesbytoken(
                 _TBURL,
                 device['id']['entityType'],
                 device['id']['id'],
                 token,
                 scope)  
           if data != {}:        
              devicedata[scope] = data
        
        device['attributes'] = devicedata
        print(devicedata)            
        
    with open('./output/devices_credentials_attributes.json', 'w', encoding='utf-8') as f:
        json.dump(devices, f, ensure_ascii=False, indent=4)


def getattributes():
    
    with open('./output/devices_credentials.json', 'r', encoding='utf-8') as f:
        devices = json.load(f)
    #print(devices)    
    updatedevices(devices)
 
 
if __name__ == '__main__':
    getattributes()   
    
