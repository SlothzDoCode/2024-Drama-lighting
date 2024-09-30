import socket
import tkinter as tk
from tkinter import *

#?functions

def call_set1():
    msg_set1 = 'setLights_green'
    client.send(msg_set1.encode())
    
def call_set2():
    msg_set2 = 'setLights_gold'
    client.send(msg_set2.encode())    

def call_killLights():
    msg_killLights = 'kill_lights'
    client.send(msg_killLights.encode())
    
def call_testBoard():
    msg_testBoard = 'test_board'
    client.send(msg_testBoard.encode())

#?server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 333)) # Change localhost to ip of lights server
print("CLIENT: connected")

#?display

display = tk.Tk()

#?buttons

btn1 = tk.Button(
    text="Green",
    width=9,
    height=4,
    command=call_set1)
btn1.place(x=100,y=100)
btn1.config(bg='#404040',fg='#FFFFFF')

btn2 = tk.Button(
    text="Gold",
    width=9,
    height=4,
    command=call_set2)
btn2.place(x=200,y=100)
btn2.config(bg='#404040',fg='#FFFFFF')

btnKill_lights = tk.Button(
    text="kill lights",
    width=9,
    height=4,
    command=call_killLights)
btnKill_lights.place(x=300,y=100)
btnKill_lights.config(bg='#404040',fg='#FFFFFF')

btnTest_board = tk.Button(
    text="Test Lights",
    width=9,
    height=4,
    command=call_testBoard)
btnKill_lights.place(x=400,y=100)
btnKill_lights.config(bg='#404040',fg='#FFFFFF')


#?display config

display.config(background='#121212')
display.attributes('-fullscreen', True)
#!display.attributes('-topmost', True)
display.mainloop()
