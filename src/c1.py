from s1 import getLogger
import socket
import time

logger = getLogger(__name__)


def start_client_socket():

    ClientMultiSocket = socket.socket()
    host = '127.0.0.1'
    port = 2004
    logger.info('Waiting for connection response')
    try:
        ClientMultiSocket.connect((host, port))
    except socket.error as e:
        logger.error(str(e))

    _res = ClientMultiSocket.recv(1024)
    i = 0
    while True:
        i += 1
        Input = str(i)
        try:
            ClientMultiSocket.send(str.encode(Input))
            _res = ClientMultiSocket.recv(1024)
        except:
            break
        # time.sleep(0.1)
    ClientMultiSocket.close()
    logger.info("ClientSucceeded")


if __name__ == '__main__':
    start_client_socket()
