import socket


class Server:
    def __init__(self):
        self.sock = socket.socket()

    def creating_connection(self):
        conn, address = self.sock.accept()
        return conn

    def servicing(self, conn):
        try:
            data = conn.recv(1024)
            if not data:
                return False
        except socket.timeout:
            print("close connection by timeout")
            return False
        print(data.decode("utf-8"))

    def hour(self):
        pass

    def minutes(self):
        pass

    def seconds(self):
        pass

    def stop(self):
        self.sock.close()

    def error(self):
        pass


def main():
    server = Server()
    with server.sock as s:
        s.bind(("127.0.0.1", 10001))
        s.listen(socket.SOMAXCONN)
        while True:
            conn = server.creating_connection()
            conn.settimeout(10)
            with conn:
                while True:
                    server.servicing(conn)

            server.stop()



if __name__ == "__main__":
    main()
