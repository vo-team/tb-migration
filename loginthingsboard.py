import requests
import json


def gettoken(tburl,username,password):
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    r = requests.post( "{}/api/auth/login".format(tburl), data=json.dumps({'username': username, 'password': password}), headers=headers)
    if r.status_code == 200:
        data = json.loads(r.text)
        return "Bearer {}".format(data['token'])
    else:
        print("GetToke error " + r.text)
        return False


if __name__ == "__main__":
    token = gettoken("http://iot.voteam.gr:8080","chris.alexakos@gmail.com","kolt46ft")
    print(token)

