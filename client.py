# klien tu merequest lo
# terus server merespon
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.12.53"  # ini alamat server

port = 5199

# connection to hostname on the port.
s.connect((host, port))
s.sendall(b'coba kirim > Hello, world')
# Receive no more than 1024 bytes
# tm = s.recv(1024)

s.close()

print("Berhasil konect ke server")
