import queue
import socket
import threading
import time


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Receiver:

    def __init__(self, ipv4: str, port: int, delay: float, buffer_size: int, router_ip_and_port: tuple):
        self.receiver_ip: str = ipv4
        self.receiver_port: int = port
        self.receiver_ip_and_port: tuple = (ipv4, port)
        self.delay: float = delay
        self.buffer_size: int = buffer_size
        self.router = router_ip_and_port

        self.socket: socket.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        self.thread_listen: threading.Thread = None
        self.continue_listen: bool = True
        self.queue: queue.Queue = queue.Queue()

# 'start' and 'stop' are used for threading
    def start(self):
        self.socket.bind(self.receiver_ip_and_port)
        self.continue_listen = True
        self.thread_listen = threading.Thread(target=self.__listen)
        self.thread_listen.start()
        print(f'Socket up and listening at {self.receiver_ip}:{self.receiver_port}.')

    def stop(self):
        self.continue_listen = False
        time.sleep(self.delay)
        if self.thread_listen is not None and self.thread_listen.is_alive():
            self.thread_listen.join(1)
        exit()

# checking the buffer for received bytes
    def __listen(self):
        print('Receiver1 listens to the Router1.')
        while self.continue_listen:
            time.sleep(self.delay)
            buffer, _ = self.socket.recvfrom(self.buffer_size)
            self.queue.put(buffer)
            print('New message:')
            print(color.PURPLE + buffer.decode("utf-8") + color.END)
        print('Stopped listening. ')
