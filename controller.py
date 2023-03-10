from ControllerClass import Controller

controller = Controller('182.25.0.5', 16, 16, 0.25, 10240,
                        # receivers:
                        {'R1': ('182.25.0.4', 16),
                         'R2': ('182.25.0.6', 16),
                         'R3': ('182.25.0.9', 16)},
                        # routers:
                        [('182.25.0.3', 16),
                         ('182.25.0.8', 16)])

controller.start()
print(controller)

# Controller is on '182.25.0.3', 5012

# list of receivers controller knows:
# Receiver1 = '182.25.0.4', 16
# Receiver2 = '182.25.0.6', 16
# Receiver3 = '182.25.0.9', 16

# list of connected routers:
# Router1 = '182.25.0.3', 16
# Router2 = '182.27.0.8', 16


