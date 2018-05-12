import requests
import time
import hashlib
import os

BASE_FILES = dict()
scan = 'https://www.virustotal.com/vtapi/v2/file/scan'
report = 'https://www.virustotal.com/vtapi/v2/file/report'
apikey = '<KEY GOES HERE>'
max_percentage = 50
server = "http://0.0.0.0:8080/api/add"

#Baseline
for fname in os.listdir("."):
    if os.path.isfile(fname):
        try:
            md5 = hashlib.md5(open(fname,"rb").read()).hexdigest()
            BASE_FILES.update({fname:md5})
        except Exception as e:
            print (e)

#Scan for new BASE_FILES
while True:
    time.sleep(5)
    for fname in os.listdir("."):
        try:
            if os.path.isfile(fname):
                md5 = hashlib.md5(open(fname,"rb").read()).hexdigest()
                if md5 not in BASE_FILES.values():
                    # post scan
                    params = {'apikey': apikey}
                    files = {'file': (fname, open(fname, 'rb').read())}
                    response = requests.post(scan, files=files, params=params)
                    time.sleep(5)
                    response = response.json()
                    # Get Resource
                    resource = response["resource"]
                    # Get Report
                    params = {'apikey': apikey, 'resource': resource}
                    response = requests.get(report, params=params)
                    response = response.json()
                    # calculate percentage
                    total = response["total"]
                    positives = response["positives"]
                    percentage = positives / total * 100
                    #Delete or save
                    if percentage >= max_percentage:
                        print ("Delete")
                        os.remove(fname)
                        data = {"data": "Deleted \"{} \" with MD5 checksum {}".format(fname, md5)}
                        requests.post(server, data=data)
                    else:
                        print ("Save")
                        BASE_FILES.update({fname: md5})
                        data = {"data": "Allowed \"{} \" with MD5 checksum {}".format(fname, md5)}
                        requests.post(server, data=data)
        except:
            pass

