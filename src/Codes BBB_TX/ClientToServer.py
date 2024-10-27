# -*- coding: utf-8 -*-
"""
File: ClientToServer.py
Authors: Théo Deffrennes, Charles Moulin, Benoît Vidotto
Date: Q1 2021
"""


#This file is used to send via VLC to the receiver. 
#This connection is similar to an Internet connection via IP addresses.
import socket
msgFromClient       = "Hello UDP Server"
serverAddressPort   = ('192.168.0.2', 10001)
bytesToSend         = str.encode(msgFromClient)

bufferSize          = 800

for i in range(100):  		# To carry out our tests, we want to send information with each keystroke using raw_input. We can send a maximum of 100x.
    msgFromClient = "test"+ str(i)
    print(msgFromClient)

    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)    
    raw_input("Press Enter to continue...")