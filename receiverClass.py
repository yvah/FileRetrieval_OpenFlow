import queue
import socket
import threading
import time


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
        while self.continue_listen:
            time.sleep(self.delay)
            buffer, _ = self.socket.recvfrom(self.buffer_size)
            self.queue.put(buffer)
            print('Receiver1 listens to the Router1 on 182.27.0.2:5012')
            print(f'New message: {buffer.decode("utf-8")}. ')
        print('Stopped listening. ')
