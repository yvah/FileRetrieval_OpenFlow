from nodeClass import Node

node2 = Node('182.25.0.7', 16, 0.25, 10240, ('182.25.0.8', 16))
node2.start()
print(node2)

# Node2 has address '182.25.0.7', 16
# Router2 has address '182.25.0.8', 16 and listens to Node2
