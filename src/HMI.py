"""
File: HMI.py
Authors: Théo Deffrennes, Charles Moulin, Benoît Vidotto
Date: Q1 2021
"""


import PySimpleGUI as sg
import socket
import time
import numpy as np
from math import sin

sg.theme('DarkTeal7')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...

host = "192.168.7.2"  # the BBB TX connected via USB
port = 10001
username = "debian"
password = "temppwd"
buffersize = 800

def CtoS(sz1, sz2, sz3, sz4, sz5, sz6, sz7):
    
    # Equation to avoid the limit cases
    limit = 6.5 + 12.5 * sin((np.pi/180) * sz2) + 12.5 * sin((np.pi/180) * (sz2 + sz3 - 90)) + 19.5 * sin((np.pi/180) * (sz4 + sz2 + sz3 - 180))
    
    if limit >= 0:
        message = str(sz7) + "," + str(sz1) + "," + str(sz2) + "," + str(sz3) + "," + str(sz4) + "," + str(sz5) + "," + str(sz6) + "b"
        serverAddressPort = (host, port)
        bytesToSend = str.encode(message)
        print(message)
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)  
    else:
        print("The selected values do not allow making an authorized movement")

def open_window5():
    layout5 = [[sg.Text('Save your values')],
               [sg.Text('Base of the robot')],
               [sg.Spin([sz for sz in range(0, 180)], initial_value=0, size=(20, 1), change_submits=True, key='spin11')],
               [sg.Text('Shoulder of the robot')],
               [sg.Spin([sz for sz in range(15, 165)], initial_value=40, size=(20, 1), change_submits=True, key='spin12')],
               [sg.Text('Elbow of the robot')],
               [sg.Spin([sz for sz in range(0, 180)], initial_value=180, size=(20, 1), change_submits=True, key='spin13')],
               [sg.Text('Vertical wrist of the robot')],
               [sg.Spin([sz for sz in range(0, 180)], initial_value=170, size=(20, 1), change_submits=True, key='spin14')],
               [sg.Text('Horizontal wrist of the robot')],
               [sg.Spin([sz for sz in range(0, 180)], initial_value=0, size=(20, 1), change_submits=True, key='spin15')],
               [sg.Text('Gripper of the robot')],
               [sg.Spin([sz for sz in range(10, 73)], initial_value=73, size=(20, 1), change_submits=True, key='spin16')],
               [sg.Text('Speed')],
               [sg.Spin([sz for sz in range(10, 30)], initial_value=10, size=(20, 1), change_submits=True, key='spin17')],
               [sg.Text('Delay before the next movement (Enter 0 if last movement)')],
               [sg.Spin([sz for sz in range(0, 30)], initial_value=0, size=(20, 1), change_submits=True, key='spin18')],
               [sg.Button("Ok")]]
    win5 = sg.Window('Save Movement', layout5)
    while True:
        event, values = win5.read()
        if event == "Ok":
            sz_slider11 = int(values['spin11'])
            sz_slider12 = int(values['spin12'])
            sz_slider13 = int(values['spin13'])
            sz_slider14 = int(values['spin14'])
            sz_slider15 = int(values['spin15'])
            sz_slider16 = int(values['spin16'])
            sz_slider17 = int(values['spin17'])
            sz_slider18 = int(values['spin18'])
            win5.close()
            window.UnHide()
            return (sz_slider11, sz_slider12, sz_slider13, sz_slider14, sz_slider15, sz_slider16, sz_slider17, sz_slider18)

        if event == sg.WINDOW_CLOSED:
            win5.close()
            window.UnHide()
            break
        
def open_window4():
    layout = [[sg.Text("How many movements do you want?")],
              [sg.Spin([sz for sz in range(0, 6)], initial_value=1, size=(20, 1), change_submits=True, key='Spin Movement'), sg.Button("Ok")],
              [sg.Button("Back")]]
    win4 = sg.Window("Second Window", layout, modal=True)
    while True:
        event, values = win4.read()
        if event == "Ok":
            j = int(values['Spin Movement'])
            Sauv = np.zeros((j, 8))
            win4.close()
            window.UnHide()
            for i in range(j):
                Sauv[i, :] = open_window5()
            return Sauv[:, :]
        if event == sg.WINDOW_CLOSED or event == "Back":
            win4.close()
            window.UnHide()
            break

layout = [  [sg.Text("For more information on robot control, visit the robot information page: "), sg.Button('Information', size=(10, 1))],
            [sg.Text("Robot control:")],
            [sg.Text('Base of the robot')],
            [sg.Slider(range=(0, 180), orientation='h', default_value=0, tick_interval=60, change_submits=True, key='slider1'), sg.Text('Manual Input:'), sg.Spin([sz for sz in range(0, 180)], initial_value=0, size=(20, 1), change_submits=True, key='spin1')],
            [sg.Text('Shoulder of the robot')],
            [sg.Slider(range=(15, 165), orientation='h', default_value=40, tick_interval=50, change_submits=True, key='slider2'), sg.Text('Manual Input:'), sg.Spin([sz for sz in range(15, 165)], initial_value=40, size=(20, 1), change_submits=True, key='spin2')],
            [sg.Text('Elbow of the robot')],
            [sg.Slider(range=(0, 180), orientation='h', default_value=180, tick_interval=60, change_submits=True, key='slider3'), sg.Text('Manual Input:'), sg.Spin([sz for sz in range(0, 180)], initial_value=180, size=(20, 1), change_submits=True, key='spin3')],
            [sg.Text('Vertical wrist of the robot')],
            [sg.Slider(range=(0, 180), orientation='h', default_value=170, tick_interval=60, change_submits=True, key='slider4'), sg.Text('Manual Input:'), sg.Spin([sz for sz in range(0, 180)], initial_value=170, size=(20, 1), change_submits=True, key='spin4')],
            [sg.Text('Horizontal wrist of the robot')],
            [sg.Slider(range=(0, 180), orientation='h', default_value=0, tick_interval=60, change_submits=True, key='slider5'), sg.Text('Manual Input:'), sg.Spin([sz for sz in range(0, 180)], initial_value=0, size=(20, 1), change_submits=True, key='spin5')],
            [sg.Text('Gripper of the robot')],
            [sg.Slider(range=(10, 73), orientation='h', default_value=73, tick_interval=20, change_submits=True, key='slider6'), sg.Text('Manual Input:'), sg.Spin([sz for sz in range(10, 73)], initial_value=73, size=(20, 1), change_submits=True, key='spin6')],
            [sg.Text('Speed')],
            [sg.Slider(range=(10, 30), orientation='h', tick_interval=10, change_submits=True, key='slider7'), sg.Text('Manual Input:'), sg.Spin([sz for sz in range(10, 30)], initial_value=10, size=(20, 1), change_submits=True, key='spin7')],
            [sg.Text("                                                                         "), sg.Button('Send', size=(10, 1))],
            [sg.Text(" ")],
            [sg.Text("To directly send the robot's resting position:")],
            [sg.Text("                                                                         "), sg.Button('Rest', size=(10, 1))],
            [sg.Text(" ")],
            [sg.Text("Do you want to save the above positions?:"), sg.Button("Save Position")],
            [sg.Text("To apply a predefined movement, select movement 1, 2, 3:")],
            [sg.Button("Position 1"), sg.Text("                                                             "), sg.Button("Position 2"), sg.Text("                                                             "), sg.Button("Position 3")],
            [sg.Text("Do you want to record a movement?:"), sg.Button("Save Movement")],
            [sg.Button("Movement 1"), sg.Text("                                                       "), sg.Button("Movement 2"), sg.Text("                                                       "), sg.Button("Movement 3")],
            [sg.Button("Quit")]
        ]

# Create the Window
window = sg.Window('Robot Braccio').Layout([[sg.Column(layout, size=(750,1000), scrollable=True)]])
win2_active=False
win3_active=False

# Event Loop to process "events"

class control:
    def __init__(self, i, values, fontsize):
        self.fontsize = fontsize
        self.spin = int(values['spin' + str(i)])
        self.slider = int(values['slider' + str(i)])
        self.sz = self.spin if self.spin != self.fontsize else self.slider
        
    def slide(self, i):
        self.fontsize = self.sz
        window['slider' + str(i+1)].update(self.sz)
        window['spin' + str(i+1)].update(self.sz)
        return self.fontsize

fontsize = [12,12,12,12,12,12,12]
#fontsize = 12
#szs=np.zeros(7)
szs=[]
for i in range(7):
    szs.append(-1)
    
while True:             
    
    event, values = window.read()
    
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    
    for i in range(7):
        szs[i]=control(i+1, values, fontsize[i])
    
    for i in range(7):
        if szs[i].sz != fontsize[i]:
            fontsize[i] = szs[i].slide(i)
#            szs[i].fontsize = szs[i].sz
#            fontsize[i] = szs[i].sz
##            font = "Helvetica "  + str(self.fontsize)
#            window['spin' + str(i+1)].update(szs[i].sz)
#            window['slider' + str(i+1)].update(szs[i].sz)
##            print(fontsize[i])
            CtoS(szs[0].sz,szs[1].sz,szs[2].sz,szs[3].sz,szs[4].sz,szs[5].sz,szs[6].sz)
            
    
    if event == 'Information'  and not win2_active:
        win2_active = True
        window.Hide()
        layout2 = layoutbis = [[sg.Image(r'C:\Users\ttdef\OneDrive\Documents\Ma1 Smart Communication & IA\Projet\Braccio.png')],[sg.Text("Here is some information about the robot to read before you start using it:")],
[sg.Text("- Motor 1 controls the base of the robot")],
[sg.Text("- Motor 2 controls the shoulder of the robot")],
[sg.Text("- Motor 3 controls the elbow of the robot")],
[sg.Text("- Motor 4 controls the vertical wrist of the robot")],
[sg.Text("- Motor 5 controls the horizontal wrist of the robot")],
[sg.Text("- Motor 6 controls the gripper of the robot")],
[sg.Text("Note that the physical limits of the motors are already indicated on the sliders. Do not try to enter values outside these limits.")],

        win2 = sg.Window('Information', layout2)
        while True:
            ev2, vals2 = win2.read()
            if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
                win2.close()
                win2_active = False
                window.UnHide()
                break
   
    if event == 'Send':
        for i in range (5):
            CtoS(szs[0].sz,szs[1].sz,szs[2].sz,szs[3].sz,szs[4].sz,szs[5].sz,szs[6].sz)

    if event == 'Rest':
        
        window['slider1'].update(0)
        window['spin1'].update(0)
        window['slider2'].update(40)
        window['spin2'].update(40)
        window['slider3'].update(180)
        window['spin3'].update(180)
        window['slider4'].update(170)
        window['spin4'].update(170)
        window['slider5'].update(0)
        window['spin5'].update(0)
        window['slider6'].update(73)
        window['spin6'].update(73)
        
        #send in bursts of 5 when rest and send buttons are pressed only
        for i in range (5):
            CtoS(0,40,180,170,0,73,10)

    if event == "Save Position"and not win3_active:
            Demo = np.zeros(7)
#            Demo[6] = str(sz7)
#            Demo[6] = str(szs[6].sz)
            for i in range(7):
                Demo[i] = int(szs[i].sz)
#            Demo[0] = str(sz1)
#            Demo[1] = str(sz2)
#            Demo[2] = str(sz3)
#            Demo[3] = str(sz4)
#            Demo[4] = str(sz5)
#            Demo[5] = str(sz6)
            win3_active = True
            window.Hide()
            layout3 = [[sg.Text("Which movement would you like to save your values to?")],
                    [sg.Button("Position 1"), sg.Button("Position 2"), sg.Button("Position 3"), sg.Text("                                 "), sg.Button("Back")]]
            win3 = sg.Window('Save Position', layout3)
            while True:
                ev3, vals3 = win3.read()
                if ev3 == sg.WINDOW_CLOSED or ev3 == "Position 1":
                    Demo1 = Demo
                    win3.close()
                    win3_active = False
                    window.UnHide()
                    break
                if ev3 == sg.WINDOW_CLOSED or ev3 == "Position 2":
                    Demo2 = Demo
                    win3.close()
                    win3_active = False
                    window.UnHide()
                    break
                if ev3 == sg.WINDOW_CLOSED or ev3 == "Position 3":
                    Demo3 = Demo
                    win3.close()
                    win3_active = False
                    window.UnHide()
                    break
                if ev3 == sg.WINDOW_CLOSED or ev3 == "Back":
                    win3.close()
                    win3_active = False
                    window.UnHide()
                    break

    if event == 'Save Movement':
        layout = [[sg.Text('Which Movement would you like to save to?')],
                [sg.Button('Movement No. 1'), sg.Text("                                                             "), 
                sg.Button('Movement No. 2'), sg.Text("                                                             "), 
                sg.Button("Movement No. 3")]]

        winq = sg.Window('Save Movement', layout)
        while True:
            event, values = winq.read()
            if event == 'Movement No. 1':
                winq.close()
                window.UnHide()
                Movement1 = open_window4()
                break
            if event == 'Movement No. 2':
                winq.close()
                window.UnHide()
                Movement2 = open_window4()
                break
            if event == 'Movement No. 3':
                winq.close()
                window.UnHide()
                Mouvement3 = open_window4()
                break
            if event == sg.WINDOW_CLOSED:
                winq.close()
                window.UnHide()
                break
            
    if event == 'Position 1':
        CtoS(int(Demo1[0]),int(Demo1[1]),int(Demo1[2]),int(Demo1[3]),int(Demo1[4]),int(Demo1[5]),int(Demo1[6]))
        for i in range(7):    
                        window['slider' + str(i+1)].update(int(Demo1[i]))
                        window['spin' + str(i+1)].update(int(Demo1[i]))
    if event == 'Position 2':
        CtoS(int(Demo2[0]),int(Demo2[1]),int(Demo2[2]),int(Demo2[3]),int(Demo2[4]),int(Demo2[5]),int(Demo2[6]))
        for i in range(7):    
                        window['slider' + str(i+1)].update(int(Demo2[i]))
                        window['spin' + str(i+1)].update(int(Demo2[i]))
    if event == 'Position 3':
        CtoS(int(Demo3[0]),int(Demo3[1]),int(Demo3[2]),int(Demo3[3]),int(Demo3[4]),int(Demo3[5]),int(Demo3[6]))
        for i in range(7):    
                        window['slider' + str(i+1)].update(int(Demo3[i]))
                        window['spin' + str(i+1)].update(int(Demo3[i]))
        
    if event == "Mouvement 1":
        ligne, colonne = np.shape(Mouvement1)
        for i in range(ligne):
            for j in range(10):
                CtoS(int(Mouvement1[i,0]),int(Mouvement1[i,1]),int(Mouvement1[i,2]),int(Mouvement1[i,3]),int(Mouvement1[i,4]),int(Mouvement1[i,5]),int(Mouvement1[i,6]))
            time.sleep(Mouvement1[i,7])
            
    if event == "Mouvement 2":
        ligne, colonne = np.shape(Mouvement2)
        
        # First send for the number of movements
        serverAddressPort   = (host, port)
        bytesToSend         = str.encode("a" + ligne + ",") # The 'a' will indicate to the Arduino how many movements are in the sequence
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)

        for i in range(ligne):
            CtoS(int(Mouvement2[i,0]), int(Mouvement2[i,1]), int(Mouvement2[i,2]), int(Mouvement2[i,3]), int(Mouvement2[i,4]), int(Mouvement2[i,5]), int(Mouvement2[i,6]))
            time.sleep(Mouvement2[i,7])

    if event == "Movement 3":
        ligne, colonne = np.shape(Mouvement3)

        # First send for the number of movements
        serverAddressPort   = (host, port)
        bytesToSend         = str.encode("a" + ligne + ",") # The 'a' will indicate to the Arduino how many movements are in the sequence
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)

        for i in range(ligne):
            CtoS(int(Mouvement3[i,0]), int(Mouvement3[i,1]), int(Mouvement3[i,2]), int(Mouvement3[i,3]), int(Mouvement3[i,4]), int(Mouvement3[i,5]), int(Mouvement3[i,6]))
            time.sleep(Mouvement3[i,7])

window.close()

# Between 15 and 27 characters are sent

# Technique for the LEDs: put a letter at the end of the movements sent, make a counter in the Arduino loop, and compare the number of times this letter is sent with the predefined number of movements


window.close()
