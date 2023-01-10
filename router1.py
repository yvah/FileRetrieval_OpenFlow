import socket
from routerClass import Router

# node1 = Node(socket.gethostbyname(socket.gethostname()), 5012, 0.25, 10240, ('182.27.0.2', 5012))
# Controller is on '182.27.0.3', 5012
receivers_file = open('receivers_list.txt', 'r')
router1 = Router('182.27.0.2', 5012, 0.25, 10240, ('182.27.0.3', 5012), receivers_file)
router1.start()
print(router1)

# [('182.25.0.1', 5012, 1), ('182.25.0.2', 5012, 2)] -- known receivers
# [('182.25.0.3', 5012, 3), ('182.25.0.4', 5012, 4), ('182.25.0.4', 5012, 5)] -- unknown receivers
