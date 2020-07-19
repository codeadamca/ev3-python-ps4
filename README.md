# python-connect-ps4
Using Python to connect to a PS4 and a map of all identified events.

This code was written to connect a LEGO EV3 Brick to a PS4 controller. The EV3 is running [ev3dev](https://www.ev3dev.org/) and running a version of Python called [Pybricks](https://github.com/pybricks/pybricks-micropython). However, the code reacting to the PS4 controller events and the mapping of different buttons should apply to any Python/PS4 project.

This code assumes that the PS4 controller has already been paired. 

## Event Files
When the PS4 is paried with the device it creates three event files. These files are updated when the PS4 controller experiecnes an event (such as a button press). 

Using a terminal check out the contents of the /dev/input folder before and after you pair the Bluetooth device. You should notice three new event files. On my device these files where:

* /dev/input/event2 (touchpad events)
* /dev/input/event3 (controller movement, like tilting, etc...)
* /dev/input/event4 (buttons, sticks, etc...)

Each event provides five values, but we only need the event ID, code, and value. Here is a list of all events I could find:

** Touchpad Events

For me touchpad events were found in /dev/input/event2.

<table>
<tr><th>Event</th><th>Code</th><th>Possible Values</th><th>Description</th></tr>
</table>

<a href="https://codeadam.ca">
<img src="https://codeadam.ca/images/code-block.png" width="100">
</a>