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


def updatedeviced(devices):
    token = lt.gettoken(_TBURL,_TBUSER,_TBPWD)
    for device in devices:
        time.sleep(2)
        data = mgdevices.getdevicecredentialsbytoken(
            _TBURL,
            device['id']['id'],
            token)
        while data is False:
            time.sleep(5)
            token = lt.gettoken(_TBURL,_TBUSER,_TBPWD)
            data = mgdevices.getdevicecredentialsbytoken(
                _TBURL,
                device['id']['id'],
                token)  
        if data != {}:        
           device['credentials'] = data
        print(data)            
        
    with open('./output/devices_credentials.json', 'w', encoding='utf-8') as f:
        json.dump(devices, f, ensure_ascii=False, indent=4)


def getgredentials():
    
    with open('./output/devices.json', 'r', encoding='utf-8') as f:
        devices = json.load(f)
    #print(devices)    
    updatedeviced(devices)
 
 
if __name__ == '__main__':
    getgredentials()   
    
