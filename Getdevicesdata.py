import json
import loginthingsboard as lt
import mgassets
import mgcustomers
import mgdevices
import time
import json
import os

_TBURL = "http://iot.voteam.gr:8080"
_TBUSER = "user@isi.gr"
_TBPWD = "****************"

def getdeviceparamdata(deviceid, devicetype,paramkey):
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
        time.sleep(20)
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
        print(latest)
        newendts = int(latest['ts'])-1000
        print(newendts)
        time.sleep(10)
        data = mgdevices.getdevicetelemetryforkeybytoken(
            _TBURL,
            devicetype,
            deviceid,
            token,
            paramkey,
            newendts)
        while data is False:
            time.sleep(20)
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
            print(reqindex)     
            with open('./output/datatest_{}_{}-{}.json'.format(paramkey,deviceid,reqindex), 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)    


    #while flagEndTs:

def getdevicedata(deviceid,deviceType):
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
            
    for device in devices:
        time.sleep(10)
        getdevicedata(device['id']['id'],device['id']['entityType'])
    

if __name__ == '__main__':
    #getdevicedata('159cd550-7926-11eb-a9da-9d23daefb115','DEVICE')
    getdatafromalldevices()
