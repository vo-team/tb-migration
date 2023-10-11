import requests
import json

import loginthingsboard as lt

def getcustomerassets(tburl,customerid,username,password):
    token = lt.gettoken(tburl,username,password)
    print (token)
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/customer/{}/assets".format(tburl,customerid), params={'limit': 1000}, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data['data']
    else:
        print("GetCustomerAssets error " + r.text)
        return False

def getcustomerassetsbytoken(tburl,customerid, token):
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/customer/{}/assets".format(tburl,customerid), params={'limit': 1000}, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data['data']
    else:
        print("GetCustomerAssets error " + r.text)
        return False

def gettenatntassets(tburl,customerid,username,password):
    token = lt.gettoken(tburl,username,password)
    print (token)
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/tenant/assets".format(tburl,customerid), params={'limit': 1000}, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data['data']
    else:
        print("GetTenantAssets error " + r.text)
        return False
        
def gettenatntassetsbytoken(tburl,customerid, token):
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/tenant/assets".format(tburl,customerid), params={'limit': 1000}, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data['data']
    else:
        print("GetTenantAssetsByToken error " + r.text)
        return False        
        
def getassetsrelationfrom(tburl,entityid,username,password,relationtype = 'to'):
    token = lt.gettoken(tburl,username,password)
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/relations/info".format(tburl ), params={"{}Id".format(relationtype) :entityid, "{}Type".format(relationtype): 'ASSET' },  headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        print("getassetsrelationfrom error " + r.text)
        return False

def getassetsrelationfrombytoken(tburl,entityid,token,relationtype = 'to'):
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/relations/info".format(tburl ), params={"{}Id".format(relationtype) :entityid, "{}Type".format(relationtype): 'ASSET' },  headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data
    else:
        print("getassetsrelationfrombytoken error " + r.text)
        return False
                
if __name__ == "__main__":
    #assets = getcustomerassets("https://esc.isi.gr/","0c23fb60-5b65-11e9-aa94-d766101f1d53s","alexakos@isi.gr","ei5kGK1*9q1oUoT*")
    assets = gettenatntassets("https://esc.isi.gr/","0c23fb60-5b65-11e9-aa94-d766101f1d53s","alexakos@isi.gr","ei5kGK1*9q1oUoT*")
    #with open('./output/assets.json', 'w', encoding='utf-8') as f:
    #    json.dump(assets, f, ensure_ascii=False, indent=4)    
    print(json.dumps(assets))
