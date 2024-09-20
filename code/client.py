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

display.config(background='#121212')
display.attributes('-fullscreen', True)
display.attributes('-topmost', True)
display.mainloop()