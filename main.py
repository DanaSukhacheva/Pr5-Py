import socket
from _thread import *

client= socket.socket()
client.connect(('192.168.26.149',12346))
def server_thr(con):
    while True:
        data = client.recv(1024)
        print("Server sent: ", data.decode())

start_new_thread(server_thr, (client, ))

while True:
    message = input("Message: ")
    client.send(message.encode())
