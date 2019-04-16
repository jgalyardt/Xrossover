import azure.storage.blob
from azure.storage.blob import BlockBlobService
import time
import re
import csv

STORAGEACCOUNTNAME= 'test2gen2dl'
STORAGEACCOUNTKEY= 'Ax++7k4z5ejajdmx9lqYrDcFMrMxWeiEINbd5SBPUhJ1FRie+rTdidXHRuhpX5vcTp8HeCoH1thTZhelRXtemw=='
LOCALFILENAME= 'download.csv'   
CONTAINERNAME= 'testingconatiner'

#Change this to the file path of the blob you want to download
#This could be automated to run on every blob
BLOBNAME= 'XrossoverIOT/01/2019/04/07/22/48'

#download from blob
t1=time.time()
blob_service=BlockBlobService(account_name=STORAGEACCOUNTNAME,account_key=STORAGEACCOUNTKEY)
blob_service.get_blob_to_path(CONTAINERNAME,BLOBNAME,LOCALFILENAME)
t2=time.time()
print(("It took %s seconds to download "+BLOBNAME) % (t2 - t1))

matches = []
with open(LOCALFILENAME) as fp:  
    line = fp.readline()
    cnt = 1
    print('Parsing the file...')
    while line:
        lineMatches = re.findall(r'"\w+":.+?(?=,|})',line)
        matches.append(lineMatches)
        line = fp.readline()
        cnt += 1


lineNumber = 0
cols = []
with open('parsed.csv', mode='w', newline='') as outfile:
    csv_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for match in matches:
        if lineNumber == 0:
            lineNumber += 1
            continue
        row = []
        for item in match:
            result = re.search(r'"\w+":', item)
            column = result.group(0)
            value = item[len(column):]
            column = column[1:-2]
            if value[0] == '"':
                value = value[1:-1]
            if lineNumber == 1:
                cols.append(column)
            row.append(value)
        if lineNumber == 1:
            csv_writer.writerow(cols)
        else:
            csv_writer.writerow(row)
        lineNumber += 1
print('Parsing complete.')

