import pandas as pd
import random
import time

#Creating dataBLE file

def createBLE():
   while True: 
        time.sleep(3)   
        dataBLE = pd.DataFrame({
            'MAC': str(random.randint(1000,10000)),
            'Heart Rate':random.randint(60,300),
            'Temp':random.randint(34,42),
            'Saturation':random.randint(140,210)
            }, index=[0])
        dataBLE = dataBLE.set_index('MAC')
        dataBLE.to_csv('dataBLE.csv')

     
createBLE()
