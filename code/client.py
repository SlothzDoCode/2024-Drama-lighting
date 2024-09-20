import socket
import threading


def server_start():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind(('localhost', 333))
    serv.listen(1)
    print("SERVER: started")

    while True:
        # establish connection
        conn, addr = serv.accept()
        from_client = ''
        print("SERVER: connection to Client established")

        while True:
            # receive data and print
            data = conn.recv(4096).decode()
            if not data: break
            from_client += data
            print("Recieved: " + from_client)

            # send message back to client
            msg = "I am SERVER"
            conn.send(msg.encode())

        # close connection and exit
        conn.close()
        break

server_start()