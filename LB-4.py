import socket
HOST = 'localhost'
PORT = 50007

file = open("Received File.txt", "wb")
file.close()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        x = 0
        with conn:
            print('Connected by', addr)
            while True:
                with open("Received File.txt", "ab") as file:
                    while True:
                        data = conn.recv(1024)
                        file.write(data)
                        if not data:
                            conn.close()
                            break