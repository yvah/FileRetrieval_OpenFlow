import os
import queue
import socket
import sys
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


class Node:

    def __init__(self, ipv4: str, port: int, delay: float, buffer_size: int, router_ip_and_port: tuple):
        self.node_ip: str = ipv4
        self.node_port: int = port
        self.node_ip_and_port: tuple = (ipv4, port)
        self.delay: float = delay
        self.buffer_size: int = buffer_size
        self.router = router_ip_and_port

        self.socket: socket.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        self.thread_listen: threading.Thread = None
        self.thread_input: threading.Thread = None
        self.continue_listen: bool = True
        self.continue_process: bool = True
        self.continue_input: bool = True

        self.queue: queue.Queue = queue.Queue()

# 'start' and 'stop' are used for threading
    def start(self):
        self.socket.bind(self.node_ip_and_port)
        self.continue_listen = True
        self.thread_listen = threading.Thread(target=self.__listen)
        self.thread_listen.start()
        print(f'Socket up and listening at {self.node_ip}:{self.node_port}.')
        self.continue_input = True
        self.thread_input = threading.Thread(target=self.__input)
        self.thread_input.start()

    def stop(self):
        self.continue_listen = False
        self.continue_input = False
        time.sleep(self.delay)
        if self.thread_listen is not None and self.thread_listen.is_alive():
            self.thread_listen.join(1)
        if self.thread_input is not None:
            self.thread_listen.join(1)
        exit()

# checking the buffer for received bytes
    def __listen(self):
        while self.continue_listen:
            time.sleep(self.delay)
            buffer, _ = self.socket.recvfrom(self.buffer_size)
            self.queue.put(buffer)
            print(f'Message came from sender {_[0]}:{_[1]} with content: '
                  + color.PURPLE + f' {buffer[32:].decode("utf-8")}. ')
        print('Stopped listening. ')

# listening to input commands and calling according functions
    def __input(self):
        print('Started listening for input. ')
        try:
            while self.continue_input:
                receiver_destination = input('Where do you want to send the message? ').upper()
                if receiver_destination.startswith('R'):
                    message = input('What is your message? ')
                    transmission = receiver_destination + ":" + message
                    self.__send(transmission)
                else:
                    print('Wrong address transcription.')
        except Exception as e:
            print('An error occurred: ', e)
            self.__input()
        print('Not listening for input anymore. ')

    def __send(self, message):
        message_bytes = None
        if type(message) is bytes:
            message_bytes = message
        elif type(message) is str:
            message_bytes = message.encode('ascii')
        self.socket.sendto(message_bytes, self.router)
