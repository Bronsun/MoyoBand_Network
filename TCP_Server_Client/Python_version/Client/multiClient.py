import socket
import time

#HOST PORT BUFFER_SIZE variables (can be change to input if we will be implemnting to system (more universal option))

HOST = '192.168.0.101'
TCP_PORT = 60001
BUFFER_SIZE = 1024

#Creating socket for TCP client

socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Connecting to socket')
socket.connect((HOST,TCP_PORT))
print(f'Connected to host: {HOST}   on   port: {TCP_PORT}')

#Openning csv file




#Loop for sending files (I HAVE NO IDEA HOW TO FIX IT XD)
while True:
    filename = 'dataBLE.csv'
    f = open(filename,'rb')
    data = f.read(BUFFER_SIZE)
    if not data:
        print ("File transfered completed")
        f.close()
    else:
        time.sleep(3)
        socket.send(data)
        print(data)
        
socket.close()


print('connection closed')


