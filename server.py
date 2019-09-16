import socket

sock = socket.socket()

sock.bind(("127.0.0.1", 10001))
sock.listen(socket.SOMAXCONN)

