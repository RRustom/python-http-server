import socket

class TCPServer:
    def __init__(self, host = '127.0.0.1', port = 8888):
        self.host = host
        self.port = port

    def start(self):
        # socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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

            response = self.handle_request(data)

            # send back data to client
            conn.sendall(data)

            # close the connection
            conn.close()

    def handle_request(self, data):
        return data

class HTTPServer(TCPServer):
    def handle_request(self, data):
        response_line = b"HTTP/1.1 200 OK\r\n"

        blank_line = b"\r\n"

        response_body = b"Request received!"

        return b"".join([response_line, blank_line, response_body])

if __name__ == '__main__':
    server = HTTPServer()
    server.start()
