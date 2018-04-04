# Echo client program
import socket, time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "127.0.1.1"
PORT = 50000
msg = "HI"

s.connect((HOST, PORT))
print("Client started")
print("Send: ", msg)
s.send(msg.encode())

time.sleep(5)
msg = "s"
s.send(msg.encode())
print("Send: ", msg)
data = s.recv(1024)
print('Received', repr(data))


time.sleep(5)
msg = "q"
s.send(msg.encode())
print("Send: ", msg)

s.close()
