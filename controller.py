from ControllerClass import Controller

controller = Controller('182.27.0.3', 5012, 5012, 0.25, 10240,
                        # receivers:
                        {1: ('182.25.0.1', 5012),
                         2: ('182.25.0.2', 5012),
                         3: ('182.25.0.3', 5012),
                         4: ('182.25.0.4', 5012),
                         5: ('182.25.0.4', 5012)},
                        # routers:
                        [('182.27.0.2', 5012),
                         ('182.27.0.9', 5012),
                         ('182.27.0.15', 5012)])
controller.start()
print(controller)

# Controller is on '182.27.0.3', 5012

# list of receivers controller knows:
# Receiver1 = '182.25.0.1', 5012
# Receiver2 = '182.25.0.2', 5012
# Receiver3 = '182.25.0.3', 5012
# Receiver4 = '182.25.0.4', 5012
# Receiver5 = '182.25.0.5', 5012

# list of connected routers:
# Router1 = '182.27.0.2', 5012
# Router2 = '182.27.0.9', 5012
# Router3 = '182.27.0.15', 5012


