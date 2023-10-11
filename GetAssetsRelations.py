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

relationstypes = ["to","from"]

def updateassets(assets):
    token = lt.gettoken(_TBURL,_TBUSER,_TBPWD)
    for asset in assets:
        time.sleep(2)
        assetrelations = {}
        for relationtype in relationstypes:
           data = mgassets.getassetsrelationfrombytoken(
               _TBURL,
               asset['id']['id'],
               token,
               relationtype)
           while data is False:
               time.sleep(1)
               token = lt.gettoken(_TBURL,_TBUSER,_TBPWD)
               data = mgassets.getassetsrelationfrombytoken(
                   _TBURL,
                   asset['id']['id'],
                   token,
                   relationtype)  
           if data != {}:        
              assetrelations[relationtype] = data
        asset['relations'] = assetrelations
        print(assetrelations)            
        
    with open('./output/assets_relations.json', 'w', encoding='utf-8') as f:
        json.dump(assets, f, ensure_ascii=False, indent=4)


def getrelations():
    
    with open('./output/assets.json', 'r', encoding='utf-8') as f:
        assets = json.load(f)
    #print(devices)    
    updateassets(assets)
 
 
if __name__ == '__main__':
    getrelations()   
    
