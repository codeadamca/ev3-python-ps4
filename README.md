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

## Button and Stick Events

For me button and stick events were found in /dev/input/event4. If you're working on a PS4 project, these are probably the events you're looking for.

<table>
<tr><th>Event</th><th>ID</th><th>Code</th><th>Possible Values</th><th>Description</th></tr>
<tr><td>X Button</td><td>1</td><td>304</td><td>
<tr><td>Circle Button</td><td>1</td><td>305</td><td>
<tr><td>Triangle Burron</td><td>1</td><td>307</td><td>
<tr><td>Square Button</td><td>1</td><td>308</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>Share Button</td><td>1</td><td>314</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>Options Button</td><td>1</td><td>315</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>PS Button</td><td>1</td><td>316</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>Left Stick Push</td><td>1</td><td>317</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>Right Stick Push</td><td>1</td><td>318</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>L1</td><td>1</td><td>310</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>R1</td><td>1</td><td>311</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>L2</td><td>1</td><td>312</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>R2</td><td>1</td><td>313</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
</table>
--------------
Event 3:
LEFT HORIZONTAL AXIS - 0 - 0 (top) to 255 (bottom) 
LEFT VERT AXIS - 1 - 0 (top) to 255 (bottom) 
L2 AXIS - 2 - 0 (released) to 255 (pushed) 
RIGHT HORIZONTAL AXIS - 3 - 0 (top) to 255 (bottom) 
RIGHT VERT AXIS - 4 - 0 (top) to 255 (bottom) 
R2 AXIS - 5 - 0 (released) to 255 (pushed) 
DIR HORIZONTAL - 16 - 1 (left), 0 (released), -1 (right)
DIR HORIZONTAL - 17 - 1 (left), 0 (released), -1 (right)
</table>

<a href="https://codeadam.ca">
<img src="https://codeadam.ca/images/code-block.png" width="100">
</a>