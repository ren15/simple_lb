import socket
from _thread import start_new_thread

import sys

g_num = 0


def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048).decode()
        if not data:
            break
        # print(data)
        global g_num
        g_num += 1
        print(f"g_num : {g_num}")
        sys.stdout.flush()
        response = 'Server message: ' + str(int(data)+1)
        connection.sendall(str.encode(response))
    connection.close()


def start_server_socket():
    ServerSideSocket = socket.socket()
    host = '127.0.0.1'
    port = 2004
    ThreadCount = 0
    try:
        ServerSideSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print('Socket is listening..')
    ServerSideSocket.listen(5)

    for i in range(100):
        Client, address = ServerSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(multi_threaded_client, (Client, ))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    ServerSideSocket.close()


if __name__ == '__main__':
    start_server_socket()
