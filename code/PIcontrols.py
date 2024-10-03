import socket
import threading
import board, neopixel
import time

dim = 1.0

pixels1 = neopixel.NeoPixel(board.D18, 144, brightness=dim)

def server_start():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('localhost', 333))
    serv.listen(1)
    print("SERVER: started")

    while True:
        # establish connection
        try:
            conn, addr = serv.accept()
            from_client = ''
            print("SERVER: connection to Client established")
        except:
            print("SERVER: there was an error establishing a conection to Client")
        
        while True:
            
            #clear from_client
            from_client = ""
            
            # receive data and print
            data = conn.recv(4096).decode()
            if not data: break
            from_client += data
            print(f"You have called: {from_client}")

            if from_client == "setLights_green":
                pixels1.fill((9,140,4))
            
            elif from_client == "setLights_gold":
                pixels1.fill((212,175,55))
            
            elif from_client == "kill_lights":
                while dim != 0.0:
                    dim = dim - 0.1
                    dim = round(dim,1)
                pixels1.fill((0,0,0))
                
            elif from_client == "test_board": 

                x=0
                pixels1.fill((0, 220, 0))
                pixels1[10] = (0, 20, 255)
                time.sleep(4)
                
                while x<35:
                    pixels1[x] = (255, 0, 0)
                    pixels1[x-5] = (255, 0, 100)
                    pixels1[x-10] = (0, 0, 255)
                    x=x+1
                    time.sleep(0.05)

                while x>-15:
                    pixels1[x] = (255, 0, 0)
                    pixels1[x+5] = (255, 0, 100)
                    pixels1[x+10] = (0, 255, 0)
                    x=x-1
                    time.sleep(0.05)
  
                time.sleep(4)

                pixels1.fill((0, 0, 0))  
                
        # close connection and exit
        conn.close()
        break

server_start()
