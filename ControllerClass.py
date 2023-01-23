import queue
import socket
import threading
import time


class Controller:

    def __init__(self, ipv4: str, port: int, routers_port: int, delay: float, buffer_size: int,
                 receivers_dict: dict, routers: list):
        self.controller_ip: str = ipv4
        self.controller_port: int = port
        self.routers_port: int = routers_port
        self.buffer_size = buffer_size
        self.delay = delay
        self.receivers = receivers_dict
        self.routers_addresses = routers

        # это вообще нужно?
        # self.router_address_and_port = None
        # self.router_ip = None
        # self.router_port = None
        # self.receiver_address = None

        self.router_queue = queue.Queue()
        self.router_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.router_listen_thread = threading.Thread(target=self.__router_listen)
        self.table_check_thread = threading.Thread(target=self.__table_check)

    def start(self):
        # это нужно? вопрос - как подсоединять роутеры, чтобы слушать их
        for router in self.routers_addresses:
            self.router_ip, self.router_port = router
            self.router_address_and_port = (self.router_ip, self.router_port)
        self.router_socket.bind((self.router_ip, self.router_port))
        self.router_listen_thread.start()
        self.table_check_thread.start()
        print(f'Server socket up and listening for clients at {self.router_ip}:{self.router_port}. ')

# receiving the message from router
    def __router_listen(self):
        print('Router listener started. ')
        while True:
            try:
                time.sleep(self.delay)
                router_buffer, router_address_and_port = self.router_socket.recvfrom(self.buffer_size)
                self.__table_check(router_buffer)
            except KeyError:
                print('KeyError happened. ')
        print('Stopped listening to routers.')

# checking if the needed receiver is in the dictionary
    def __table_check(self, receiver_name):
        time.sleep(self.delay)
        try:
            if receiver_name in self.receivers:
                self.receiver_address = self.receivers.get(receiver_name)
                self.__send(self.receiver_address)
            print(f'Receiver address found: {self.receiver_address}.')
        except Exception as e:
            print(f'A problem occurred: {e}.')
        print('Finished checking the table.')

# sending the needed receiver address from the table to the router that requested it
    def __send(self, buffer: bytes):
        try:
            self.router_socket.sendto(self.receiver_address, self.router_address_and_port)
        except Exception as e:
            print(f'Problem occurred while getting the receiver address: {e}.')
