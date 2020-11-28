import socket
from threading import Thread
from socketserver import ThreadingMixIn
import pandas as pd

#HOST TCP_PORT BUFFER_SIZE 

HOST = '192.168.0.101' # Here you put IP address of your computer
TCP_PORT = 60001 # leave that without change
BUFFER_SIZE = 1024 

# Creating Client Class for multithreading

class ClientThread(Thread):
    
    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
    def run(self):
        
        while True:
            filename = 'dataRecived.csv'
            f = open(filename, 'w+b')
            data = self.sock.recv(1024)
            if not data:
                f.close()
                #self.sock.close()
                break
            f.write(data)
        self.sock.sendall("File received")
        self.sock.close()

# Creating socket for TCP connection
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Creating socket...')
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print('Socket created successfully')
print('Binding socket to the port...')
tcpsock.bind((HOST, TCP_PORT))
print(f'Socket binded successfully to port {TCP_PORT} ')
print('Waiting for clients to join....')

#Creating list of threads (clients in english XD)
threads = []

while True:
    tcpsock.listen(5)
    (conn, (ip, port)) = tcpsock.accept()
    #conn.settimeout(7)
    newthread = ClientThread(ip, port, conn)
    print(ip)
    newthread.start()
    threads.append(newthread)
for t in threads:
    t.join()
