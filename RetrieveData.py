import json
import loginthingsboard as lt
import mgassets
import mgcustomers
import mgdevices
import time
import json
import os

tburl = "http://iot.voteam.gr:8080"

token = lt.gettoken(tburl,"chris.alexakos@gmail.com","$rBGw1YW8$p8K0^K")

outputpath = "./output/{}".format((time.time() * 1000))
os.mkdir(outputpath)

customers = mgcustomers.getcustomersbytoken(tburl,token)
with open('{}/customers.json'.format(outputpath), 'w', encoding='utf-8') as f:
    json.dump(customers, f, ensure_ascii=False, indent=4)

#159cd550-7926-11eb-a9da-9d23daefb115
data = mgdevices.getdevicetelemetryforkeybytoken(tburl,"DEVICE","159cd550-7926-11eb-a9da-9d23daefb115",token,'temperature-air')
print(data)
print("{} - {}".format("159cd550-7926-11eb-a9da-9d23daefb115",len(data['temperature-air'])))

with open('./output/datatest_{}_{}.json'.format("159cd550-7926-11eb-a9da-9d23daefb115","temperature-air"), 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
        
'''
devices = mgdevices.getdevicesbytoken(tburl,token)


for device in devices:
    device_attr = mgdevices.getdeviceattributesbytoken(tburl,device['id']['entityType'],device['id']['id'],token)
    device_telkeys = mgdevices.getdevicetelementrykeysbytoken(tburl,device['id']['entityType'],device['id']['id'],token)
    device_relations = mgdevices.getdevicesrelationfrombytoken(tburl,device['id']['entityType'],device['id']['id'],token)
    
    print(device)
    with open('{}/{}_device.json'.format(outputpath,device['id']['id']), 'w', encoding='utf-8') as f:
        json.dump(device, f, ensure_ascii=False, indent=4)
    
    print(device_attr)
    with open('{}/{}_device_attr.json'.format(outputpath,device['id']['id']), 'w', encoding='utf-8') as f:
        json.dump(device_attr, f, ensure_ascii=False, indent=4)    
    
    print(device_telkeys)
    with open('{}/{}_device_telkeys.json'.format(outputpath,device['id']['id']), 'w', encoding='utf-8') as f:
        json.dump(device_telkeys, f, ensure_ascii=False, indent=4)       
    
    print(device_relations)
    with open('{}/{}_device_relations.json'.format(outputpath,device['id']['id']), 'w', encoding='utf-8') as f:
        json.dump(device_relations, f, ensure_ascii=False, indent=4)  
'''