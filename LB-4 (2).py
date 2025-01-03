import socket

HOST = 'localhost'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    file_path = "Send File.txt"
    with open(file_path, "rb") as file:
        s.sendfile(file)
    print(f"Файл '{file_path}' успішно відправлено.")