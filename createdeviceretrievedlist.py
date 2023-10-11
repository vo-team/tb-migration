import glob
import os
import argparse
import json


def readfiles(path):
  deviceids = []
  pattern = "./{}/datatest*.json".format(path)
  for datasetfile in glob.iglob(pattern):
     filename = os.path.basename(datasetfile)
     filename = os.path.splitext(filename)[0]
     deviceid = filename[filename.rindex('_')+1:]
     deviceid = deviceid[:deviceid.rindex('-')]
     if deviceid not in deviceids:
        deviceids.append(deviceid)
  print(deviceids)
  with open("./{}/tmp_parsed_devices.json".format(path), 'w', encoding='utf-8') as f:
     json.dump(deviceids, f, ensure_ascii=False, indent=4)

def main():
   argParser = argparse.ArgumentParser()
   argParser.add_argument("-p", "--path", help="Path with dataset files")
   args = argParser.parse_args()
   path = args.path
   print(path)
   readfiles(path)
   
if __name__ == '__main__':
   main()
