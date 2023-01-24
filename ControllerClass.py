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

        self.router_queue = queue.Queue()
        self.router_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.router_listen_thread = threading.Thread(target=self.__router_listen)

        self.table_check_thread = threading.Thread(target=self.__table_check)

    def start(self):
        self.router_listen_thread.start()
        self.table_check_thread.start()

    # receiving the message from router
    def __router_listen(self):
        print(f'Controller is listening to routers. ')
        while True:
            try:
                time.sleep(self.delay)
                self.receiver_name = self.router_socket.recvfrom(self.buffer_size)
                print(self.receiver_name)
                self.__table_check()
            except KeyError:
                print('KeyError happened. ')
        print('Stopped listening to routers.')

# checking if the needed receiver is in the dictionary
    def __table_check(self):
        time.sleep(self.delay)
        try:
            if self.receiver_name in self.receivers:
                print('looking for receiver in table...')
                self.receiver_address = self.receivers.get(self.receiver_name)
                self.__send(self.receiver_address)
            print(f'Receiver address found: {self.receiver_address}.')
        except Exception as e:
            print(f'A problem occurred: {e}.')
        print('Finished checking the table.')

# sending the needed receiver address from the table to the router that requested it
    def __send(self, buffer: bytes):
        try:
            self.router_socket.sendto(self.receiver_address, self.routers_addresses[0])
        except Exception as e:
            print(f'Problem occurred while getting the receiver address: {e}.')
