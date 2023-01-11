import queue
import socket
import threading
import time
import uuid


class Controller:

    def __init__(self, buffer_size, router_ip, router_port, router_id, receivers_dict: dict,
                 routers_addresses: list, delay: int = 0.01):
        self.router_queue = queue.Queue()
        self.receiver_address = None
        self.buffer_size = buffer_size
        self.delay = delay
        self.receivers = receivers_dict
        self.routers = routers_addresses
        self.router_ip = router_ip
        self.router_port = router_port
        self.router_id = router_id

        self.router_address_and_port = (router_ip, router_port)

        self.router_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.router_listen_thread = threading.Thread(target=self.__router_listen)
        self.router_process_thread = threading.Thread(target=self.__check_table)

    def start(self):
        self.router_socket.bind((self.router_ip, self.router_port))
        self.router_listen_thread.start()
        self.router_process_thread.start()
        print(f'Server socket up and listening for clients at {self.router_ip}:{self.router_port}. ')

    # receiving the message from router
    def __router_listen(self):
        print('Router listener started. ')
        while True:
            try:
                time.sleep(self.delay)
                router_buffer, router_address_and_port = self.router_socket.recvfrom(self.buffer_size)
                self.__check_table(router_buffer)
            except KeyError:
                print('KeyError happened. ')
        print('Stopped listening to routers.')

    def __check_table(self, receiver_name, receiver_ip=None, receiver_port=None):
        time.sleep(self.delay)
        try:
            if self.receivers.__contains__(receiver_name):
                self.receiver_address = self.receivers.get(receiver_name)
            print(f'Receiver address found: {self.receiver_address}.')
        except Exception as e:
            print(f'A problem occurred: {e}.')
        print('Finished checking the table.')

# sending the needed receiver address from the table to the router that requested it
    def __send(self, buffer: bytes):
        try:
            receiver_info = self.receiver_address[0] + self.receiver_address[1]
        except Exception as e:
            print(f'Problem occurred while getting the receiver address: {e}.')
        self.
        self.router_socket.sendto(self.receiver_info, self.router_address_and_port)
