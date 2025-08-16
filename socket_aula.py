import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)
try:
    client.connect(('host_adress(255.255.255.255)', 8080))
    client.send(b'Hello World\n\n')
    response = client.recv(1024).decode()
    print(response)
except Exception as e:
    print(e)