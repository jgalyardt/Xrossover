import time
import json
import keyboard
import random

def main():
    dataID = 0
    with open('data.json', 'w') as outfile:
        data = {} 
        while not keyboard.is_pressed('q'):
            data[dataID] = {  
                'x': random.uniform(1,10),
                'y': random.uniform(1,10),
                'z': random.uniform(1,10),
                'xa': random.uniform(1,10),
                'ya': random.uniform(1,10),
                'za': random.uniform(1,10)
            }
            dataID += 1
            time.sleep(1)
        json.dump(data, outfile)
    s = open("data.json").read()[1:-1]
    open('data.txt', 'w').write(s)
    print('\nOutput data to file.')

if __name__ == "__main__":
    main()
