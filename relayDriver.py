#
# relayDriver
#  - 2015 Brent Petit
#
#   routines for controlling a relay board throug RPi
#   GPIO pins. 
#
import time
import RPi.GPIO as GPIO

# DEBUGGING
debug = 0

# Mapping of relay channels to GPIO pins
# channel: GPIO pin
# Add entries for more relays
relay_pins = {
	1: 11,
	2: 12,
	3: 13,
	4: 15
}

# Helpers
relay_open = GPIO.HIGH
relay_closed = GPIO.LOW

# Pulse time - how long to hold pulseRelay
pulse_time = .2

# Global status flag
relayBoardInitialized = 0

#
#   initRelayBoard
#     Fire up GPIO library and set the GPIO pins 
#     up for the relay board
#   This must be run prior to accessing the relays
#
def initRelayBoard(): 
    global relayBoardInitialized
    if relayBoardInitialized == 1:
        print "Error: Board already initialized" 
	return -1

    GPIO.setmode(GPIO.BOARD)

    # Iterate through pin map and init each pin
    # set each relay to open
    for relay, pin in relay_pins.iteritems():
        if debug:
	    print "Setting up GPIO pin ", pin
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)

    relayBoardInitialized = 1

    return 0

def shutdownRelayBoard():
    global relayBoardInitialized
    if relayBoardInitialized == 0:
        print "Error: Board not initialized"
        return -1

    if debug:
        print "calling cleanup on GPIO"
    GPIO.cleanup()

    relayBoardInitialized = 0;

    return 0

#    getRelayState
#      return the state of the queried relay
#
def getRelayState(channel):
    pin = relay_pins[channel]
    return GPIO.input(pin)

#    setRelayState
#      set the state to the passed in state
def setRelayState(channel, state):
    pin = relay_pins[channel]
    GPIO.output(pin, state)

#
#    isRelayOpen
#      return true if queried relay is in open
#      state
def isRelayOpen(channel):
    return (getRelayState(channel) == relay_open)

#
#    isRelayClosed
#      return true if queried relay is in closed
#      state
def isRelayClosed(channel):
    return (getRelayState(channel) == relay_closed)

#
#   openRelay
#    flip the channel state to open
def openRelay(channel):
    # Check pin state
    if isRelayClosed(channel):
        setRelayState(channel, relay_open)
    else:
        if debug:
            print "open_relay ", pin, " already open"

#
#   closeRelay
#    flip the channel state to closed
def closeRelay(channel):
    # Check pin state
    if isRelayOpen(channel):
        setRelayState(channel, relay_closed)
    else:
        if debug: 
            print "close_relay ", pin, " already closed"

#
#    pulseRelay
#      flip the state of relay for a short time
#
def pulseRelay(channel):
   toggleRelay(channel)
   time.sleep(pulse_time)
   toggleRelay(channel) 


#
#   toggleRelay
#    flip the channel state from the current
#    state to the opposite state.
def toggleRelay(channel):
    if isRelayClosed(channel):
        openRelay(channel)
    else:
        closeRelay(channel)

# END
