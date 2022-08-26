import socket
import time


def start_client_socket():

    ClientMultiSocket = socket.socket()
    host = '127.0.0.1'
    port = 2004
    print('Waiting for connection response')
    try:
        ClientMultiSocket.connect((host, port))
    except socket.error as e:
        print(str(e))

    res = ClientMultiSocket.recv(1024)
    for i in range(10):
        Input = str(i)
        ClientMultiSocket.send(str.encode(Input))
        res = ClientMultiSocket.recv(1024)
        print(res.decode('utf-8'))
        time.sleep(1)
    ClientMultiSocket.close()


if __name__ == '__main__':
    start_client_socket()
