# -*- coding: utf-8 -*-
"""
File: SerialServer.py
Authors: Théo Deffrennes, Charles Moulin, Benoît Vidotto
Date: Q1 2021
"""


import serial

def nsplit(s, n):  # Split a list into sublists of size "n"
    return [s[k:k + n] for k in range(0, len(s), n)]

def bit_array_to_string(array):  # Recreate the string from the bit array
    res = ''.join([chr(int(y, 2)) for y in [''.join([str(x) for x in bytes]) for bytes in nsplit(array, 8)]])
    return res

ser = serial.Serial("/dev/ttyO5", 9600)
while(True):
	s = ser.read(100)       # read up to one hundred bytes
	
	print(bit_array_to_string(s))
	ser.write('Salut')     # write a string
