# -*- coding: utf-8 -*-
"""
File: TestLEDRobot.py
Authors: Théo Deffrennes, Charles Moulin, Benoît Vidotto
Date: Q1 2021
"""


import serial

#host = "192.168.7.2" #la BBB TX connectée par usb
#port = 10001
#username = "debian"
#password = "temppwd"
#buffersize=800

#serverAddressPort   = (host, port)
#bytesToSend         = str.encode(message)
#UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#UDPClientSocket.sendto(bytesToSend, serverAddressPort)
while True:
    message = "60, 54, 65, 12, 54, 45, 45b"
    
    serial_port = serial.Serial( port="COM10", baudrate=9600, timeout=1 )
    serial_port.write(bytes(message, 'utf-8'))
    #serial_port.write(message)
    input("Press enter to continue...")