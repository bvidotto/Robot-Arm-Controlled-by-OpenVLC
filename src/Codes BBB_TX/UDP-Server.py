# -*- coding: utf-8 -*-
"""
File: UDP-Server.py
Authors: Théo Deffrennes, Charles Moulin, Benoît Vidotto
Date: Q1 2021
"""


#_______________________________________________________
#This first section is used to initiate serial transfer to the Arduino board connected via usb. 
#This usb port is located on the BeagleBone at the port labelled “/dev/ttyACM0”. 
#The default baud rate is 9600.
import serial

serial_port = serial.Serial( port="/dev/ttyACM0", baudrate=9600, timeout=1 )

#_______________________________________________________
#This second section initiates the transfer via IP address to create the connection via VLC.

import socket

 

localIP     = "192.168.0.1"

localPort   = 10001

bufferSize  = 800


msgFromServer       = "Hello UDP Client"

bytesToSend         = str.encode(msgFromServer) 

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

#_________________________________________________________
#This section runs indefinitely and listens to the VLC connection.  
#Once a VLC packet has been received, it is printed for viewing via PuTTY.
#After this confimation, the received message is sent to the serial port defined earlier.

# Listen for incoming datagrams

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)


    serial_port.write(format(message))