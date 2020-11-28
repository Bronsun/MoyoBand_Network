
#Piotr Radecki 2020
#This program is responsible for detecting devices, connecting with one BLE module and getting a few consecutive values of characteristics 0-7(all)
#Characteristics are saved in Data.txt output file
#Program can be opened from raspbian shell with command "sudo python3 ble_python_test0.py " 
#default values: scanning time=2s,number of gotten values in one characteristic=5
#bluepy library for python3 is necessary for the script to work

 

import struct
import bluepy.btle as bl
MAC="FA:FB:EC:C9:CF:90"

#scanning
scanner = bl.Scanner()
devices = scanner.scan(0.5)
#table of available devices
dev_table = [[] for k in range (len(devices))]
for count,k in enumerate(devices):
        dev_table[count]=["device "+str(count),k.getScanData()[-1][2],k.addr]
print("Detected Devices:" )
#print(dev_table)
#mac address choice
#TESTING#MAC=dev_table[int(input("Type index of selected device: "))][2] #index of device is represented by a number of device(f.e Device 0 has index 0)
con = bl.Peripheral(MAC,bl.ADDR_TYPE_RANDOM)
#data list
data = [[] for k in range(9)]
#getting characteristics
chstic = con.getCharacteristics()
#loading descriptors of charactertics to data list
for count,k in enumerate(chstic):
        data[count].append(str(chstic[count]))
#loading characteristics to data list
for k in range (7):
        for count,i in enumerate(chstic):
                try:

                        data[count].append(i.read())
                except:
                        data[count].append("error")
#closing connection
con.disconnect()
#writing data to file
writing_to_file = open("Data.txt","w+")
for kcount,k in enumerate(data):
        for count,i in enumerate(k):
                if (count!=0 and (kcount==3 or kcount==5 or kcount==6) ):
                        writing_to_file.write(str(struct.unpack('b',i)[0])+"\n")


                elif(count!=0 and kcount==2):
                        writing_to_file.write(str(struct.unpack('d',i)[0])+"\n")
                elif(count!=0 and kcount==1):
                        writing_to_file.write(str(struct.unpack('h',i)[0])+"\n")

                else:
                        writing_to_file.write(str(i)+"\n") #uncommenting above section will cause decription of data(works properly only with sdk example)
        writing_to_file.write("\n")


