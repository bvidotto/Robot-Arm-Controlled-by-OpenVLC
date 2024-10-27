# -*- coding: utf-8 -*-
"""
File: testBBB_TX.py
Authors: Théo Deffrennes, Charles Moulin, Benoît Vidotto
Date: Q1 2021
"""


import socket
import sys 
import time

localIP     = "192.168.7.2"
localPort   = 10001
bufferSize  = 800

"""Server part for HMI"""

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

serverAddressPort   = ('192.168.0.2', 10001)

"""Client part for RX BBB"""

# Listen for incoming datagrams

messagePrecedent = 0
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    messageCurrent = bytesAddressPair[0]
    for i in range(10):
        UDPClientSocket.sendto(messageCurrent, serverAddressPort) # MessageCurrent == bytes
    	time.sleep(.05)
    print(format(messageCurrent))
   	
    
    