# Pyhton Libraries
That are all libraries needed to run Server and Client connection
```
socekt
time
threading
socektserver
pandas
random

```




# Server

### How to use

In directory Server we have two files. 

**MultiServer.py** and **dataRecived.csv**

#### MultiServer
This part of code is very important because we have to change our IP address. For testing we are using our localhost - your computer or raspberry PI.

```
#HOST TCP_PORT BUFFER_SIZE 

HOST = '192.168.0.101'
TCP_PORT = 60001
BUFFER_SIZE = 1024 
```

To check your ip address open CMD (on Windows) or Terminal (MAC OS). 
In CMD/terminal type this command

Windows
>ipconfig 

MacOS
>ifconfig 

First IPv4 address should be your localhost. Usually it looks like
```
192.168.0.101
or
192.168.0.4

Pattern is
192.168.X.X
```
After you find you your IP address just copy and paste it into the code. 
Now to start your server open your CMD or Terminal go to the directory your server file is and start it as normal as python app.

>cd /Your_Directory in which is MultiServer.py file

>python MultiServer.py

If you did everything as in instruction you will see in CMD/Terminal sth like this

```
Creating socket...
Socket created successfully
Binding socket to the port...
Socket binded successfully to port 60001 
Waiting for clients to join....

```
Your server is now up and running :)
To exit use CTRL+C

#### dataRecived.csv

In this file you will be collecting all data from all Raspberries. That's it.


# Client
### How to use

In Client directory we have 3 files. 

**CSVGENERATOR.py**, **multiClient.py**,**dataBLE.csv**

#### CSVGenertor
This is dummy app that simulates sendig data from BLE to server. It creates an CSV file (dataBLE.csv) which is updating every second. 

To test our connection we have to first run our CSVGenerator. 
To run it simply open another CMD Window (DO NOT CLOSE THE WINDOW WITH OUR SERVER) and type

>python CSVGenerator.py

Hurray your dummy connection is up and runnig

#### multiClient
Now we have to run our Client. It is imporant part because Client will send data to our server. 
```
#HOST PORT BUFFER_SIZE variables

HOST = '192.168.0.101'
TCP_PORT = 60001
BUFFER_SIZE = 1024
```
To test connection on our computer in HOST type the same IPv4 address as in Server side. Always type the same HOST address. Client has to know where to send files, am I right XD?

Okey now save file and run it as normal python file (open new CMD window - in total you should have three running CMD windows on your desktop)

>python multiClient.py

You shoudl now see sth like this:
```
Connecting to socket
Connected to host: 192.168.0.101   on   port: 60001
b'MAC,Heart Rate,Temp,Saturation\n6871,73,37,177\n'
.
.
.
```
And on server you should see the ip Address of Client

```
Creating socket...
Socket created successfully
Binding socket to the port...
Socket binded successfully to port 60001 
Waiting for clients to join....
192.168.0.101 "<-- New Client"
```

Your connection is now working. Check you dataRecived.csv file to see if the values are changing.



# DataBase
 I created really simple database.
 ORM to database is in models.py.
 It is not complited but works pretty well

 For easy use I created functions to add,delete and show Patients and Bands.
 
 If you want to use DataBase download models.py and moyo.db.

! **REALY IMPORTANT** !

Do not delete moyo.db

This is sqllite database in which all data is hold. If you accidently delete it nothing wrong happens however all your data will be removed. If you want to create again data base just run

>python models.py


### How to use functions
Import them from models.py

Functions:

- AddPatient (name,lastname,age,sex)

- AddBand (lastname,MAC,room,bed)

- ShowPatient()

- ShowBands()

- DeletePatient(name,lastname)


How to import them to you app:

>from models import AddPatient,AddBand,ShowPatient,ShowBands,DeletePatient
