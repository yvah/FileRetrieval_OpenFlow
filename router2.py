from routerClass import Router

router2 = Router('182.25.0.8', 16, 0.25, 10240,
                 # node2:
                 ('182.25.0.7', 16),
                 # controller:
                 ('182.25.0.5', 16),
                 # known receivers:
                 {'R2': ('182.25.0.7', 16),
                  'R3': ('182.25.0.9', 16)})
router2.start()
print(router2)

# Controller is on '182.25.0.5', 16
# unknown receivers:
# Receiver1 = '182.25.0.4', 16
