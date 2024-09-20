import socket
import tkinter as tk
from tkinter import *
import threading

def server():

    ip = 'localhost' # IP of Raspberry Pi
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, 333))
    print("CLIENT: connected")


display = tk.Tk()

threading.Thread(target=server)

btn1 = tk.Button(
    text="set 1",
    width=9,
    height=4,
    command="")
btn1.place(x=100,y=100)
btn1.config(bg='#404040',fg='#FFFFFF')

btn2 = tk.Button(text="set 2",
    width=9,
    height=4,
    command="")
btn2.place(x=200,y=100)
btn2.config(bg='#404040',fg='#FFFFFF')

display.config(background='#121212')
display.attributes('-fullscreen', True)
display.attributes('-topmost', True)
display.mainloop()
