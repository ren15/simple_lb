"""
the client should be a ping-pong client

"""
import socket
import time


def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = "ping"

    for i in range(10):
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print('Received from server: ' + data)  # show in terminal
        time.sleep(1)

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
