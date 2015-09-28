# relayDriver
Raspberry Pi python driver for relay board

This module provides routines for driving a relay module through a Raspberry Pi. For testing a 
Sainsmart 4-Channel 5V Relay Module was used. This module uses the RPi.GPIO module to drive
the GPIO pins.

Module setup/teardown modules
- Init/Shutdown Module
    initRelayBoard()
      Set up the GPIO library and set the GPIO pins for the relay board

    shutdownRelayBoard()
      Shutdown the GPIO complex
      
- Query operations
    getRelayState(channel)
      return state of the relay. Possible values are relay_open and relay_closed.

    isRelayOpen(channel)
      return true if relay is open, false if relay is closed
      
    isRelayClosed(channel)
      return true if relay is closed, false if relay is open

- Update operations
- Open Relay
    openRelay(channel)
      Set the relay at channel to an open state. If already open, this will do nothing.

- Close Relay
    closeRelay(channel)
      Set the relay at channel to an closed state. If already closed, this will do nothing.
       
- Pulse Relay
     pulseRelay(channel)

