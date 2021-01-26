import socket

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# list for incoming connections
sock.listen(1)

while True:
    # wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print('received {!r}'.format(data))
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break
    finally:
        # clean up the connection
        connection.close()
