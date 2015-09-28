import relayDriver
import time

print "Starting up..."
relayDriver.initRelayBoard()

print "Close relay 1"
relayDriver.closeRelay(1)
time.sleep(.5)

print "Open relay 1"
relayDriver.openRelay(1)
print "Close relay 2"
relayDriver.closeRelay(2)
time.sleep(.5)

print "Open relay 2"
relayDriver.openRelay(2)
print "Close relay 3"
relayDriver.closeRelay(3)
time.sleep(.5)

print "Open relay 3"
relayDriver.openRelay(3)
print "Close relay 4"
relayDriver.closeRelay(4)
time.sleep(.5)

print "Open relay 4"
relayDriver.openRelay(4)

time.sleep(1)

print "All on..."

relayDriver.closeRelay(1)
time.sleep(.2)
relayDriver.closeRelay(2)
time.sleep(.2)
relayDriver.closeRelay(3)
time.sleep(.2)
relayDriver.closeRelay(4)

time.sleep(1)

print "Pulse each relay"
relayDriver.pulseRelay(1)
relayDriver.pulseRelay(2)
relayDriver.pulseRelay(3)
relayDriver.pulseRelay(4)

print "All off..."

relayDriver.openRelay(4)
time.sleep(.2)
relayDriver.openRelay(3)
time.sleep(.2)
relayDriver.openRelay(2)
time.sleep(.2)
relayDriver.openRelay(1)

print "Pulse each relay"
relayDriver.pulseRelay(1)
relayDriver.pulseRelay(2)
relayDriver.pulseRelay(3)
relayDriver.pulseRelay(4)

print "shutting down relay board..."
relayDriver.shutdownRelayBoard()

print "DONE"

