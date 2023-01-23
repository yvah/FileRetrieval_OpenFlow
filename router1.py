from routerClass import Router

router1 = Router('182.27.0.2', 5012, 0.25, 10240, ('182.27.0.3', 5012),
                 # known receivers:
                 {1: ('182.25.0.1', 5012),
                  2: ('182.25.0.2', 5012)})
router1.start()
print(router1)

# Controller is on '182.27.0.3', 5012
# unknown receivers:
# Receiver3 = '182.25.0.3', 5012
# Receiver4 = '182.25.0.4', 5012
# Receiver5 = '182.25.0.5', 5012

