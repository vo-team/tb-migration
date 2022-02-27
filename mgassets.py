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


if __name__ == "__main__":
    assets = getcustomerassets("http://iot.voteam.gr:8080","13814000-1dd2-11b2-8080-808080808080","chris.alexakos@gmail.com","kolt46ft")
    print(json.dumps(assets))