from receiverClass import Receiver

receiver2 = Receiver('182.25.0.6', 16, 0.25, 10240, ('182.27.0.3', 16))
receiver2.start()
print(receiver2)

# Receiver2 listens to the Router1 on '182.27.0.2', 5012
# Receiver2 is known by Router1 & Controller
# Controller is on '182.27.0.3', 5012
