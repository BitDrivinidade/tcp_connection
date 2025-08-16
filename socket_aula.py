import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)
try:
    client.connect(('192.168.1.24', 8080))
    client.send(b'Ola Mundo\n\n')
    response = client.recv(1024).decode()
    print(response)
except Exception as e:
    print(e)