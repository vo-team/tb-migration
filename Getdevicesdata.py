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

def getdeviceparamdata(deviceid, devicetype,paramkey):
    print("-- Retrieve data for device {} for parameter {}".format(deviceid,paramkey))
    currentTS = int(time.time() * 1000)
    token = lt.gettoken(_TBURL,_TBUSER,_TBPWD)

    data = mgdevices.getdevicetelemetryforkeybytoken(
        _TBURL,
        devicetype,
        deviceid,
        token,
        paramkey,
        currentTS)
    while data is False:
        time.sleep(1)
        token = lt.gettoken(_TBURL,_TBUSER,_TBPWD)
        data = mgdevices.getdevicetelemetryforkeybytoken(
            _TBURL,
            devicetype,
            deviceid,
            token,
            paramkey,
            currentTS)
        
              
    
    reqindex = 1

    with open('./output/datatest_{}_{}-{}.json'.format(paramkey,deviceid,reqindex), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    flagEndTs = True
    while flagEndTs:
        latest=min(data[paramkey], key=lambda d: int(d['ts']))
        #print(latest)
        newendts = int(latest['ts'])-1000
        #print(newendts)
        time.sleep(1)
        data = mgdevices.getdevicetelemetryforkeybytoken(
            _TBURL,
            devicetype,
            deviceid,
            token,
            paramkey,
            newendts)
        while data is False:
            time.sleep(1)
            token = lt.gettoken(_TBURL,_TBUSER,_TBPWD)
            data = mgdevices.getdevicetelemetryforkeybytoken(
                _TBURL,
                devicetype,
                deviceid,
                token,
                paramkey,
                newendts)    
        if data == {}:
            flagEndTs = False
        else:
            reqindex +=1
            #print(reqindex)     
            with open('./output/datatest_{}_{}-{}.json'.format(paramkey,deviceid,reqindex), 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)    


    #while flagEndTs:

def getdevicedata(deviceid,deviceType):
    print("-- Initialise data retrieval for device {}".format(deviceid))
    token = lt.gettoken(_TBURL,_TBUSER,_TBPWD)

    device_telkeys = mgdevices.getdevicetelementrykeysbytoken(_TBURL,deviceType,deviceid,token)
    time.sleep(10)
    for telkey in device_telkeys:
        getdeviceparamdata(deviceid, deviceType, telkey)


def getdatafromalldevices():
    token = lt.gettoken(_TBURL,_TBUSER,_TBPWD)
    
    customers = mgcustomers.getcustomersbytoken(_TBURL,token)
    with open('./output/customers.json', 'w', encoding='utf-8') as f:
        json.dump(customers, f, ensure_ascii=False, indent=4)
    

    devices = mgdevices.getdevicesbytoken(_TBURL,token)
    with open('./output/devices.json', 'w', encoding='utf-8') as f:
        json.dump(devices, f, ensure_ascii=False, indent=4)
    blacklistdevices = []
    if os.path.isfile("./output/tmp_parsed_devices.json"):
      print("-- Loading already retrieved device data from temporary file ./output/tmp_parsed_devices.json")
      with open("./output/tmp_parsed_devices.json") as tmp_file:
         blacklistdevices = json.load(tmp_file)
            
    for device in devices:
        if device['id']['id'] not in blacklistdevices:
           time.sleep(10)
           getdevicedata(device['id']['id'],device['id']['entityType'])
           with open("./output/tmp_parsed_devices.json", 'w', encoding='utf-8') as f:
              blacklistdevices.append(device['id'])
              json.dump(blacklistdevices, f, ensure_ascii=False, indent=4)
        else:
           print("-- Data for device {} already retrieved".format(device['id']['id']))           
           
    

if __name__ == '__main__':
    #getdevicedata('220b6d80-028d-11ea-856a-83c3f676babf','DEVICE')
    getdatafromalldevices()
