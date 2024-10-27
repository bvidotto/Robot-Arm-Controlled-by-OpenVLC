# -*- coding: utf-8 -*-
"""
File: UDP-Server.py
Authors: Théo Deffrennes, Charles Moulin, Benoît Vidotto
Date: Q1 2021
"""


import socket
import time 
import serial

localIP     = "192.168.0.2"
localPort   = 10001
bufferSize  = 800

msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)


# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))


serial_port = serial.Serial( port="/dev/ttyACM0", baudrate=9600, timeout=1 )

print("UDP server up and listening")
 

# Listen for incoming datagrams

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    
    print(clientMsg)
    
    serial_port.write(format(message))
    
# Delay to avoid buffer saturation
    time.sleep(0.1)
   
