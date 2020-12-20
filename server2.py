import socket 
import os
from _thread import *
import smtplib

ServerSocket = socket.socket()
host=''
port= 2525
ThreadCount = 0
sender = 'from@domain.com'
receivers = ['to@domain.com']
message = """From: From person <from@domain.com>
To: To Person <todomain.com>
Subject : SMTP PROTOCOL
This is a SMTP PROTOCOL message.
"""
try:

    ServerSocket.bind((host,port))
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)

except socket.error as e:
    print(str(e))
except SMTPException:
    print ("Error: enable to send email")

print('Waitig for a Connection..')
ServerSocket.listen(5)

def threaded_client(connection):
    connection.send(str.encode('Welcome to the SMTP\n')) 
    while True:
        data =connection.recv(2048)
        

        if not data:
	  
         break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' +address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client,(Client, ))
    ThreadCount +=1
    print('Thread Number:' +str(ThreadCount))
ServerSocket.close()
