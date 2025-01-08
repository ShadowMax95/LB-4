import socket
HOST = 'localhost'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    file = open("Received File.txt", "wb")
    file.close()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            with open("Received File.txt", "ab") as file:
                while True:
                    data = conn.recv(1024)
                    file.write(data)
                    if not data:
                        conn.close()
