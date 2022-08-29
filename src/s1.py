import socket
from _thread import start_new_thread
import sys
import logging
import time


def getLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    streamHandler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '[%(asctime)s] - %(filename)s - %(message)s')
    streamHandler.setFormatter(formatter)

    logger.addHandler(streamHandler)
    return logger


logger = getLogger(__name__)

g_num = 0


class QpsReporter:
    def __init__(self):
        self.t_last = time.time()
        self.g_last = 0

    @staticmethod
    def create_thread(period: float):
        def qps_reporter_thread():
            qps_reporter = QpsReporter()
            while True:
                qps_reporter.update(g_num)
                time.sleep(period)

        start_new_thread(qps_reporter_thread, ())

    def update(self, var):
        # if var % self.period == 0:

        t_this = time.time()
        t_diff = t_this - self.t_last
        self.t_last = t_this

        g_diff = var - self.g_last
        self.g_last = var

        qps = g_diff / t_diff
        logger.info(f'QPS : {qps}')
        sys.stdout.flush()


def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))

    while True:
        data = connection.recv(2048).decode()
        if not data:
            break

        global g_num
        g_num += 1

        # logger.info(f"g_num : {g_num}")

        response = 'Server message: ' + str(int(data)+1)
        connection.sendall(str.encode(response))

    connection.close()


def start_server_socket(host, port, max_clients):
    ServerSideSocket = socket.socket()

    ThreadCount = 0
    try:
        ServerSideSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print(f'Socket is listening at {host}:{port}')
    ServerSideSocket.listen(max_clients)

    QpsReporter.create_thread(1)

    while True:
        Client, address = ServerSideSocket.accept()
        logger.info('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(multi_threaded_client, (Client, ))
        ThreadCount += 1
        logger.info('Thread Number: ' + str(ThreadCount))

    ServerSideSocket.close()
    logger.info('Server Closed')


if __name__ == '__main__':

    start_server_socket(host='127.0.0.1', port=2004, max_clients=100)