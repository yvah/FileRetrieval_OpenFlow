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


class Router:

    def __init__(self, ipv4: str, port: int, delay: float, buffer_size: int, node1: tuple, Controller: tuple, receivers):
        self.router_ip: str = ipv4
        self.router_port: int = port
        self.router_ip_and_port: tuple = (ipv4, port)
        self.delay: float = delay
        self.buffer_size: int = buffer_size
        self.node1 = node1
        self.Controller = Controller
        self.receivers_dict = receivers
        self.receiver_address = None
        
        self.socket: socket.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        self.thread_listen: threading.Thread = None
        self.continue_listen: bool = True
        self.continue_process: bool = True
        self.queue: queue.Queue = queue.Queue()

    # 'start' and 'stop' are used for threading
    def start(self):
        self.socket.bind(self.router_ip_and_port)
        self.continue_listen = True
        self.thread_listen = threading.Thread(target=self.__listen)
        self.thread_listen.start()
        print(f'Socket up and listening at {self.router_ip}:{self.router_port}.')

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
            # separating the message
            node_data = buffer.decode("utf-8").split(":")
            receiver_address = node_data[0]
            message = node_data[1]
            # checking if the receiver address is in the dictionary of receivers
            try:
                if receiver_address not in self.receivers_dict:
                    self.__update_table(receiver_address)
                    print(f'Unknown address {receiver_address}. Updating the table...')
                self.__send_message(receiver_address, message)
                print(f'Sending the message to receiver {receiver_address}.')
            except Exception as e:
                print(f'Unsolved problem: {e}')
            print(f'Message came from node {_[0]}:{_[1]} with content: '
                  + color.PURPLE + f' {message}. ')
        print('Stopped listening.')
        print('Stopped listening.')

    # sending the unknown address to the Controller,
    # receiving update about this address,
    # adding the address to table.
    def __update_table(self, receiver_address):
        try:
            self.socket.sendto(receiver_address, self.Controller)
            time.sleep(self.delay)
            buffer, _ = self.socket.recvfrom(self.buffer_size)
            self.queue.put(buffer)
            self.receivers_dict.update(buffer.decode('utf-8'))
        except Exception as e:
            print(f'Problem occurred while updating table: {e}.')

    # sending the message to the receiver
    def __send_message(self, receiver_address, message):
        message_bytes = None
        if type(message) is bytes:
            message_bytes = message
        elif type(message) is str:
            message_bytes = message.encode('ascii')
        self.socket.sendto(message_bytes, receiver_address)
