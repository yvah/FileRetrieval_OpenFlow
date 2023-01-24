from routerClass import Router

router1 = Router('182.25.0.3', 16, 0.25, 10240,
                 # node1:
                 ('182.25.0.2', 16),
                 # controller:
                 ('182.25.0.5', 16),
                 # known receivers:
                 {'R1': ('182.25.0.4', 16)})
router1.start()
print(router1)

# Controller is on '182.25.0.5', 16
# unknown receivers:
# Receiver2 = '182.25.0.7', 16
# Receiver3 = '182.25.0.9', 16
