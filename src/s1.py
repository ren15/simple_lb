import socket
from _thread import start_new_thread
import sys
import logging


def getLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    streamHandler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '[%(asctime)s] - %(filename)s - %(message)s')
    streamHandler.setFormatter(formatter)

    logger.addHandler(streamHandler)
    return logger


def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048).decode()
        if not data:
            break
        global g_num
        g_num += 1

        logger.info(f"g_num : {g_num}")
        sys.stdout.flush()

        if g_num > 100:
            break

        response = 'Server message: ' + str(int(data)+1)
        connection.sendall(str.encode(response))

    connection.close()
    logger.info("connection closed")


def start_server_socket(host, port, max_clients):
    ServerSideSocket = socket.socket()

    ThreadCount = 0
    try:
        ServerSideSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    logger.info(f'Socket is listening at {host}:{port}')
    ServerSideSocket.listen(max_clients)

    while True:
        logger.info("Before accept")
        # TODO: in new thread the socket did close
        # but the main thread will still be waiting
        Client, address = ServerSideSocket.accept()
        logger.info("After accept")

        logger.info('Connected to: ' + address[0] + ':' + str(address[1]))

        start_new_thread(multi_threaded_client, (Client, ))
        ThreadCount += 1

        logger.info('Thread Number: ' + str(ThreadCount))

        if g_num > 100:
            break
    ServerSideSocket.close()
    logger.info('Server Closed')


if __name__ == '__main__':
    logger = getLogger(__name__)
    g_num = 0

    start_server_socket(host='127.0.0.1', port=2004, max_clients=100)
