from receiverClass import Receiver

receiver3 = Receiver('182.25.0.6', 16, 0.25, 10240, ('182.27.0.3', 16))
receiver3.start()
print(receiver3)

# Receiver3 listens to the Router2 on '182.27.0.2', 5012
# Receiver3 is known by Router2 & Controller
# Controller is on '182.27.0.3', 5012
