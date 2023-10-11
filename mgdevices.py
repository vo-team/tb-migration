import requests
import json

import loginthingsboard as lt

def getdevices(tburl,username,password):
    token = lt.gettoken(tburl,username,password)
    print (token)
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/tenant/devices".format(tburl), params={'limit': 1000}, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data['data']
    else:
        print("GetDevices error " + r.text)
        return False

def getdevicesbytoken(tburl,token):
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/tenant/devices".format(tburl), params={'limit': 1000}, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data['data']
    else:
        print("GetDevices error " + r.text)
        return False

def getdevicecredentials(tburl,deviceid,username,password):
    token = lt.gettoken(tburl,username,password)
    print (token)
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/device/{}/credentials".format(tburl,deviceid), params={'limit': 1000}, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        print("getdevicecredentials error " + r.text)
        return False

def getdevicecredentialsbytoken(tburl,deviceid,token):
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/device/{}/credentials".format(tburl,deviceid), params={'limit': 1000}, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        print("getdevicecredentialsbytoken error " + r.text)
        return False


def getdeviceattributes(tburl,entitytype,entityid,username,password,scope=None):
    token = lt.gettoken(tburl,username,password)
    print (token)
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    if scope is None:
       r = requests.get( "{}/api/plugins/telemetry/{}/{}/values/attributes".format(tburl,entitytype,entityid ),  headers=headers)
    else:
       r = requests.get( "{}/api/plugins/telemetry/{}/{}/values/attributes/{}".format(tburl,entitytype,entityid,scope ),  headers=headers)
       
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        print("getdeviceattributes error " + r.text)
        return False

def getdeviceattributesbytoken(tburl,entitytype,entityid,token,scope=None):
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    if scope is None:
       r = requests.get( "{}/api/plugins/telemetry/{}/{}/values/attributes".format(tburl,entitytype,entityid ),  headers=headers)
    else:
       r = requests.get( "{}/api/plugins/telemetry/{}/{}/values/attributes/{}".format(tburl,entitytype,entityid,scope ),  headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        print("getdeviceattributes error " + r.text)
        return False

def getdevicetelementrykeys(tburl,entitytype,entityid,username,password):
    token = lt.gettoken(tburl,username,password)
    print (token)
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/plugins/telemetry/{}/{}/keys/timeseries".format(tburl,entitytype,entityid ),  headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        print("getdevicetelementrykeys error " + r.text)
        return False

def getdevicetelementrykeysbytoken(tburl,entitytype,entityid,token):
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/plugins/telemetry/{}/{}/keys/timeseries".format(tburl,entitytype,entityid ),  headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        print("getdevicetelementrykeys error " + r.text)
        return False

def getdevicesrelationfrom(tburl,entitytype,entityid,username,password):
    token = lt.gettoken(tburl,username,password)
    print (token)
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/relations/info".format(tburl ), params={'toId' :entityid, 'toType': entitytype},  headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        print("getdevicesrelationfrom error " + r.text)
        return False

def getdevicesrelationfrombytoken(tburl,entitytype,entityid,token):
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/relations/info".format(tburl ), params={'toId' :entityid, 'toType': entitytype},  headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        print("getdevicesrelationfrom error " + r.text)
        return False


def getdevicetelemetrybytoken(tburl,entitytype,entityid,token):
    
    devicekeys = getdevicetelementrykeysbytoken(tburl,entitytype,entityid,token)
    
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/plugins/telemetry/{}/{}/values/timeseries".format(tburl,entitytype,entityid), params={'keys' : ",".join(devicekeys), 'startTs': "1614432188000", 'endTs' : "1645968188000", 'limit':'500', 'agg' : 'NONE'},  headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        print("getdevicetelemetrybytoken error " + r.text)
        return False     

# def getdevicetelemetryforkeybytoken(tburl,entitytype,entityid,token,key):
#     headers = {'Accept': 'application/json', 'X-Authorization' : token}
#     r = requests.get( "{}/api/plugins/telemetry/{}/{}/values/timeseries".format(tburl,entitytype,entityid), params={'keys' : key, 'startTs': "1614432188000", 'endTs' : "1614442188000", 'limit':'5000', 'agg' : 'NONE'},  headers=headers)
#     if r.status_code == 200:
#         data = json.loads(r.text)
#         return data
#     else:
#         print("getdevicetelemetrybytoken error " + r.text)
#         return False 

def getdevicetelemetryforkeybytoken(tburl,entitytype,entityid,token,key,endTs,startTs=1514764800000,limit=3000):
    
    queryparams = {
        'keys' : key, 
        'startTs': startTs, 
        'endTs' : endTs, 
        'limit': limit, 
        'agg' : 'NONE'
    }
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get(
         "{}/api/plugins/telemetry/{}/{}/values/timeseries".format(tburl,entitytype,entityid), 
        params=queryparams,  
        headers=headers)
    
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        print("getdevicetelemetrybytoken error " + r.text)
        return False 


if __name__ == "__main__":
    #devices = getdevices("http://iot.voteam.gr:8080","chris.alexakos@gmail.com","kolt46ft")
    #print(json.dumps(devices))
    #device_credentials = getdevicecredentials("http://iot.voteam.gr:8080","316bb820-206c-11e8-b0fa-0b62ec816f21","chris.alexakos@gmail.com","$rBGw1YW8$p8K0^K")
    #print(json.dumps(device_credentials))
    #device_attrs = getdeviceattributes("http://iot.voteam.gr:8080","DEVICE","316bb820-206c-11e8-b0fa-0b62ec816f21","chris.alexakos@gmail.com","$rBGw1YW8$p8K0^K")
    #print(json.dumps(device_attrs))
    #telemetry_keys = getdevicetelementrykeys("http://iot.voteam.gr:8080","DEVICE","316bb820-206c-11e8-b0fa-0b62ec816f21","chris.alexakos@gmail.com","$rBGw1YW8$p8K0^K")
    #print(json.dumps(telemetry_keys))
    #device_rels = getdevicesrelationfrom("http://iot.voteam.gr:8080","DEVICE","316bb820-206c-11e8-b0fa-0b62ec816f21","chris.alexakos@gmail.com","$rBGw1YW8$p8K0^K")
    #print(json.dumps(device_rels))
    keys = getdevicetelemetrybytoken("http://iot.voteam.gr:8080","DEVICE","5b0358f0-2867-11ea-94e9-8536a03505c7","chris.alexakos@gmail.com","$rBGw1YW8$p8K0^K")


