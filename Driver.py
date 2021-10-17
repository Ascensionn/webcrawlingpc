import MemoryExpress as me
import Newegg as egg
import PCPartPicker as pcpp
import json

def printData(data):
    for i in data:
        print(i + ' ' + str(data[i]))
    print()


search = input("Enter your desired product: ")

dataMemoryExpress = me.getDataMemoryExpress(search)
dataNewegg = egg.getDataNewegg(search)
dataPCPartPicker = pcpp.getDataPCPartPicker(search)

print('Your input, ' + search + ', returned the following results for the lowest prices: \n')

printData(dataMemoryExpress)
printData(dataNewegg)
printData(dataPCPartPicker)

with open('StorageMemoryExpress.json','w') as file:
    json.dump(dataMemoryExpress, file, indent=4, sort_keys=True)
    file.close()

with open('StorageNewegg.json','w') as file:
    json.dump(dataNewegg, file, indent=4, sort_keys=True)
    file.close()

with open('StoragePCPartPicker.json','w') as file:
    json.dump(dataPCPartPicker, file, indent=4, sort_keys=True)
    file.close()