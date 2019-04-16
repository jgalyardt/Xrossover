import time
import json
import random
import re

def main():
    
    dataID = 0
    data = {}
    dataString = ''
    isNowReadingItem = False
    
    with open('data.txt') as infile:
        line = infile.readline()
        while line:
            nLoc = line.find('N')
            
            #This will raise an exception if the end of the file is reached and 'N' has not been found
            if nLoc == -1 and not isNowReadingItem:
                line = infile.readline()
                continue
            else:
                if not isNowReadingItem:
                    dataString += line[nLoc:]
                else:
                    isNowReadingItem = True
                    if nLoc != -1:
                        dataString += line[:nLoc]
                        results = re.findall(r'\w: (\d|.)+?,', dataString)
                        for i in range(0, len(results)):
                            data[dataID] = {results[i][:1]: results[i][3:]}
                            dataID += 1
                        dataString = ''
                        isNowReadingItem = False
                        continue
                    else:
                        dataString += line
            line = infile.readline()
   
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
    
    print('\nOutput json data to file.')

if __name__ == "__main__":
    main()
