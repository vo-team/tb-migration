import requests
import json

import loginthingsboard as lt

def getcustomers(tburl,username,password):
    token = lt.gettoken(tburl,username,password)
    print (token)
    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/customers".format(tburl), params={'limit': 1000}, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data['data']
    else:
        print("GetCustomers error " + r.text)
        return False

def getcustomersbytoken(tburl,token):

    headers = {'Accept': 'application/json', 'X-Authorization' : token}
    r = requests.get( "{}/api/customers".format(tburl), params={'limit': 1000}, headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return data['data']
    else:
        print("GetCustomers error " + r.text)
        return False


if __name__ == "__main__":
    customers = getcustomers("http://iot.voteam.gr:8080","chris.alexakos@gmail.com","kolt46ft")
    print(json.dumps(customers))
