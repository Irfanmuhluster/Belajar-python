import socket
# intinya berkomunikasi dg 2 komputer/lebih
# bind = Method ini digunakan untuk menghubungkan alamat ip dengan
# nomor port ke
# socket. Socket harus dibuka dahulu sebelum terhubung dengan alamat tersebut.

# bind digunakan untuk menghubungkan socket dengan alamat server

server = socket.socket()
server.bind(('192.168.12.53', 5199))  # ini alamat ip komputer
server.listen(1)  # jumlah koneksi maksimum yg dpt ditangani server
while True:
    client_socket, client_address = server.accept()
    print(client_address, "has connected")
    # iki menerima
    recvieved_data = client_socket.recv(1024).decode()
    print(recvieved_data)

    # # Get the content of htdocs/index.html
    # fin = open('htdocs/index.html')
    # content = fin.read()
    # fin.close()

    # # Send HTTP response
    # response = 'HTTP/1.0 200 OK\n\n' + content
    # client_socket.sendall(response.encode())

    # response
    # hello world ditampilkan di web
    response = 'HTTP/1.0 200 OK\n\nHello World'
    client_socket.sendall(response.encode())
    client_socket.close()

server.close()
