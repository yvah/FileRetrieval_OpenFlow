import os
import queue
import socket
import sys
import threading
import time

buffer_size = 10240
node_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print('Socket created.')
# node_socket.bind(('172.25.0.2', 4900))
# print('Socket bound.')

controller_address = ('172.25.0.3', 4900)
#  destination_message = input('Enter the message destination: ')
# destination_buffer = destination_message.encode('utf-8')
# contents_message = input('What do you want to send? ')
# contents_buffer = contents_message.encode('utf-8')
# client_socket.sendto(destination_buffer, controller_address)

def start():
    node_socket.bind(('182.25.0.2', 4900))
    print('Socket bound.')
    thread_input = threading.Thread(target=__input)
    thread_input.start()


def __input():
    continue_input: bool = True

    while continue_input:
        destination_message = input('Enter the message destination: ')
        if destination_message.startswith('FW'):
            destination_buffer = destination_message.encode('utf-8')
            node_socket.sendto(destination_buffer, controller_address)
            print(f'Destination {destination_message} was sent to controller {controller_address[0]}. ')
            contents_message = input('What do you want to send? ')
            print(f'Message {contents_message} was sent to controller {controller_address[0]}. ')
            __receive()
        else:
            print('Unknown destination. ')


def __receive():
    continue_listen: bool = True
    while continue_listen:
        time.sleep(delay)
        buffer, _ = socket.recvfrom(buffer_size)
        queue.put(buffer)
        print(f'Message came from server {_[0]}:{_[1]} with task id {buffer[:32].hex()} and content'
              + f' {buffer[32:].decode("utf-8")}. ')
    print('Stopped listening. ')

# def __input(self):
#
#     print('Started listening for input. ')
#     while self.continue_input:
#         destination_message = input('Enter the message destination: ')
#         if destination_message.startswith('R'):
#             self.__join(destination_message)
#         elif destination_message == 'LEAVE':
#             self.__leave()
#         elif destination_message == 'QUIT' or destination_message == 'EXIT' or destination_message == 'Q' \
#                 or destination_message == 'STOP' or destination_message == 'EXIT':
#             print('Not listening for input anymore. ')
#             self.__quit()
#             break
#         else:
#             self.__unknown(destination_message)
#     print('Not listening for input anymore. ')



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


while True:
    time.sleep(0.01)
    buffer, server = node_socket.recvfrom(buffer_size)
    message = None
    try:
        message = buffer.decode('ascii')
    except:
        pass
    try:
        print(f'Received part of "{contents_message}": ')
        file_path = os.path.join('/files', contents_message)
        file_object = open(file_path, 'ab')
        file_object.write(buffer)
        file_object.close()
        print(color.PURPLE + buffer.decode('utf-8') + color.END)
    except Exception as e:
        print(f'Unexpected error occurred: "{e}".')

print('Client stopped working normally. ')

    # try:
    #     if message == 'NONE':
    #         print(f'File "{contents_message}" not found. ')
    #         break
    #     elif message == 'END':
    #         print(f'File "{contents_message}" finished loading. ')
    #         break
    #     else:

            # print(f'Received part of "{contents_message}": ')
            # file_path = os.path.join('/files', contents_message)
            # file_object = open(file_path, 'ab')
            # file_object.write(buffer)
            # file_object.close()
            # print(color.PURPLE + buffer.decode('utf-8') + color.END)
    # except FileNotFoundError:
    #   print(f'No "{contents_message}" found in this directory. ')

