import socket
from nodeClass import Node

#node1 = Node(socket.gethostbyname(socket.gethostname()), 5012, 0.25, 10240, ('182.27.0.2', 5012))
node1 = Node('182.27.0.1', 5012, 0.25, 10240, ('182.27.0.2', 5012))
node1.start()
print(node1)
