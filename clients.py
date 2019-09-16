import socket

while True:
    sock = socket.socket()
    sock.connect(("127.0.0.1", 10001))
    command = input("Введите номер одной из комманд: \n1) hour\n2) minutes\n3) seconds\n4) stop\n")
    if command == 1:
        sock.sendall("1".encode("utf-8"))
    elif command == 2:
        sock.sendall("2".encode("utf-8"))
    elif command == 3:
        sock.sendall("3".encode("utf-8"))
    elif command == 4:
        sock.sendall("4".encode("utf-8"))
    else:
        sock.sendall("5".encode("utf-8"))


sock.close()
