import socket

class TCPServer:
    host = '127.0.0.1'  # server address
    port = 8000 # server port

    def start(self):
        # socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # bind the socket object to the address and port
        s.bind((self.host, self.port))

        # start listening for connections
        s.listen(5)

        print("Listening at", s.getsockname())

        while True:
            # accept new connections
            conn, addr = s.accept()

            print("Connected by", addr)

            # read first 1024 bytes sent by client
            data = conn.recv(1024)

            print(data)

            # send back data to client
            conn.sendall(data)

            # close the connection
            conn.close()

if __name__ == '__main__':
    server = TCPServer()
    server.start()
