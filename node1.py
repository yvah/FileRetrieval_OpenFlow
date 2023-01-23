from nodeClass import Node

node1 = Node('182.25.0.2', 16, 0.25, 10240, ('182.25.0.3', 16))
node1.start()
print(node1)

# Node1 has address '182.25.0.2', 16
# Router1 has address '182.25.0.3', 16 and listens to Node1
