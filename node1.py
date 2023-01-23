from nodeClass import Node

node1 = Node('182.26.0.1', 5012, 0.25, 10240, ('182.27.0.2', 5012))
node1.start()
print(node1)

# Node1 has address '182.26.0.1', 5012
# Router1 has address '182.27.0.2', 5012 and listens to Node1
