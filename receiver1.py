from receiverClass import Receiver

receiver1 = Receiver('182.25.0.4', 16, 0.25, 10240, ('182.27.0.3', 16))
receiver1.start()
print(receiver1)

# Receiver1 listens to the Router1 on '182.27.0.2', 5012
# Receiver1 is known by Router1 & Controller
# Controller is on '182.27.0.3', 5012
