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
while event:

    # Place event data into variables
    (tv_sec, tv_usec, ev_type, code, value) = struct.unpack(FORMAT, event)

    # If a button was pressed or released
    if ev_type == 1:

        # React to the X button
        if code == 304 and value == 0:
            print("The X button was released")
        if code == 304 and value == 1:
            print("The X button was pressed")
    
    elif ev_type == 3: # Stick was moved

        # React to the left stick
        if code == 1:
            left_speed = scale(value, (0,255), (100, -100))
        
        # React to the right stick
        if code == 4:
            right_speed = scale(value, (0,255), (100, -100))
    
    # Set motor speed
    left_motor.dc(left_speed)
    right_motor.dc(right_speed)

    # Read the next event
    event = in_file.read(EVENT_SIZE)

in_file.close()