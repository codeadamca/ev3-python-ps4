#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import (Motor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog

import struct

# This program uses the two PS4 sticks to control two EV3 Large Servo Motors using tank like controls

# Create your objects here.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
left_speed = 0
right_speed = 0

# Locat the event file you want to react to, on my setup the PS4 controller button events
# are located in /dev/input/event4
infile_path = "/dev/input/event4"
in_file = open(infile_path, "rb")

# Define the format the event data will be read
# See https://docs.python.org/3/library/struct.html#format-characters for more details
FORMAT = 'llHHi'
EVENT_SIZE = struct.calcsize(FORMAT)
event = in_file.read(EVENT_SIZE)

# A helper function for converting stick values (0 to 255) to more usable numbers (-100 to 100)
def scale(val, src, dst):
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

# Create a loop to react to events
# This loop react to all main PS4 button and sstick events. I ave left out buttons like
# share and options, but can easily be added in by referring to the table on the 
# GitHub page: https://github.com/codeadamca/python-connect-ps4
while event:

    # Place event data into variables
    (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(FORMAT, event)

    # If a button was pressed or released
    if ev_type == 1:

        # React to the X button
        if code == 304 and value == 0:
            print("The X button was released")
        elif code == 304 and value == 1:
            print("The X button was pressed")

        # React to the Circle button
        elif code == 305 and value == 0:
            print("The Circle button was released")
        elif code == 305 and value == 1:
            print("The Circle button was pressed")

        # React to the Triangle button
        elif code == 307 and value == 0:
            print("The Triangle button was released")
        elif code == 307 and value == 1:
            print("The Triangle button was pressed")

        # React to the Square button
        elif code == 308 and value == 0:
            print("The Square button was released")
        elif code == 308 and value == 1:
            print("The Square button was pressed")

        # React to the L1 button
        elif code == 310 and value == 0:
            print("The L1 button was released")
        elif code == 310 and value == 1:
            print("The L1 button was pressed")

        # React to the R1 button
        elif code == 311 and value == 0:
            print("The R1 button was released")
        elif code == 311 and value == 1:
            print("The R1 button was pressed")

        # React to the L2 button
        elif code == 312 and value == 0:
            print("The L2 button was released")
        elif code == 312 and value == 1:
            print("The L2 button was pressed")

        # React to the R2 button
        elif code == 313 and value == 0:
            print("The R2 button was released")
        elif code == 313 and value == 1:
            print("The R2 button was pressed")
    
    elif ev_type == 3: # Stick was moved

        # The sticks often trigger non-stop events so I have commented this out,
        # it back in to get stick positions
        '''
        # React to the left stick vertical 
        if code == 1:
            print("The left stick vertical is at ",value)
            left_speed = scale(value, (0,255), (100, -100))
        
        # React to the left stick horizontal 
        elif code == 0:
            print("The left stick horizontal is at ",value)

        # React to the right stick vertical
        elif code == 4:
            print("The right stick vertical is at ",value)
            right_speed = scale(value, (0,255), (100, -100))

        # React to the right stick horizontal
        elif code == 3:
            print("The right stick horizontal is at ",value)
        '''

        # React to the Directional pad
        if code == 16 and value == -1:
            print("The horizontal directional pad is left")
        elif code == 16 and value == 1:
            print("The horizontal directional pad is right")
        elif code == 16 and value == 0:
            print("The horizontal directional pad is released")

        elif code == 17 and value == -1:
            print("The vertical directional pad is up")
        elif code == 17 and value == 1:
            print("The horizontal directional pad is down")
        elif code == 17 and value == 0:
            print("The horizontal directional pad is released")

    # Set motor speed
    left_motor.dc(left_speed)
    right_motor.dc(right_speed)

    # Read the next event
    event = in_file.read(EVENT_SIZE)

in_file.close()