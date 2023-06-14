# LEGO Mindstorms EV3, Pthon, and a PS4 Controller

A basic snippet to use vanillia Python to react to a PS4 controller events.

This code was written to connect a LEGO EV3 Brick to a PS4 controller. The EV3 is running [ev3dev](https://www.ev3dev.org/) and running a version of Python called [Pybricks](https://github.com/pybricks/pybricks-micropython). However, the code reacting to the PS4 controller events and the mapping of different buttons should apply to any Python/PS4 project.

This code assumes that the PS4 controller has already been paired. 

## Event Files
When the PS4 is paried with the device it creates three event files. These files are updated when the PS4 controller experiecnes an event (such as a button press). 

Using a terminal check out the contents of the /dev/input folder before and after you pair the Bluetooth device. You should notice three new event files. On my device these files where:

* /dev/input/event2 (touchpad events)
* /dev/input/event3 (controller movement, like tilting, shaking, etc...)
* /dev/input/event4 (buttons, sticks, etc...)

Each event provides five values, but we only need the event ID, code, and value. Here is a list of all events I could map:

## Button and Stick Events

With my device, the button and stick events were found in /dev/input/event4. If you're working on a PS4 project, these are probably the events you're looking for.

<table>
<tr><th>Event</th><th>ID</th><th>Code</th><th>Possible Values</th><th>Description</th></tr>
<tr><td>X Button</td><td>4</td><td>304</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>Circle Button</td><td>4</td><td>305</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>Triangle Burron</td><td>4</td><td>307</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>Square Button</td><td>4</td><td>308</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>Share Button</td><td>4</td><td>314</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>Options Button</td><td>4</td><td>315</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>PS Button</td><td>4</td><td>316</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>Left Stick Push</td><td>4</td><td>317</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>Right Stick Push</td><td>4</td><td>318</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>L1</td><td>4</td><td>310</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>R1</td><td>4</td><td>311</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>L2</td><td>4</td><td>312</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>R2</td><td>4</td><td>313</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>Left Stick Horizontal Axis</td><td>3</td><td>0</td><td>0 to 255</td><td>0 Left/127 Middle/255 Right</td></tr>
<tr><td>Left Stick Vertical Axis</td><td>3</td><td>1</td><td>0 to 255</td><td>0 Top/127 Middle/255 Bottom</td></tr>
<tr><td>L2 Axis</td><td>3</td><td>2</td><td>0 to 255</td><td>0 Released/255 Completely Pressed</td></tr>
<tr><td>Right Stick Horizontal Axis</td><td>3</td><td>3</td><td>0 to 255</td><td>0 Left/127 Middle/255 Right</td></tr>
<tr><td>Right Stick Vertical Axis</td><td>3</td><td>4</td><td>0 to 255</td><td>0 Top/127 Middle/255 Bottom</td></tr>
<tr><td>R2 Axis</td><td>3</td><td>4</td><td>0 to 255</td><td>0 Left/127 Middle/255 Right</td></tr>
<tr><td>Directional Pad Horizontal</td><td>3</td><td>16</td><td>-1, 0 or 1</td><td>-1 Right/0 Released, 1 Left</td></tr>
<tr><td>Directional Pad Vertical</td><td>3</td><td>17</td><td>-1, 0 or 1</td><td>-1 Right/0 Released, 1 Left</td></tr>
</table>

Note that the left and right sticks often trigger ongoing events if the controller has any drift. My controller would continuously send events for left horizontal stick movememt alternating between 127 and 128. 

## Controller Movement

Movement events were found in /dev/input/event3.

These events are triggered by physically moving or tilting the controller. I'm not as confident with these. I could not tell the difference with codes one and two. 

<table>
<tr><th>Event</th><th>ID</th><th>Code</th><th>Possible Values</th><th>Description</th></tr>
<tr><td>Left/Right Tilt</td><td>3</td><td>0</td><td>8192 to -8192</td><td>8192 Tilted as Far Left/0 No Tilt/-8192 Tilted As Far Right</td></tr>
<tr><td>Towards/Away Tilt</td><td>3</td><td>1</td><td>8192 to -8192</td><td>8192 Tilted as Far Towards/0 No Tilt/-8192 Tilted As Far Away</td></tr>
<tr><td>Towards/Away Tilt</td><td>3</td><td>2</td><td>8192 to -8192</td><td>8192 Tilted as Far Towards/0 No Tilt/-8192 Tilted As Far Away</td></tr>
<tr><td>Vertical Speed</td><td>3</td><td>3</td><td>Any Number</td><td>Negative is Down, Positive is Up</td></tr>
<tr><td>Accelleration</td><td>3</td><td>4</td><td>Any Number</td><td>Negative is Slowing Down, Positive is Speeding Up</td></tr>
<tr><td>Timer</td><td>4</td><td>5</td><td>Any Positive Number</td><td>This seems to be the time in micro seconds that the controller has been turned on</td></tr>
</table>

## Touch Pad Events

Movement events were found in /dev/input/event2.

These events are triggered by using or pressing the touchpad on the PS4 controller. I could not figure out the difference between codes 252 and 230 or 333 and 47.

<table>
<tr><th>Event</th><th>ID</th><th>Code</th><th>Possible Values</th><th>Description</th></tr>
<tr><td>Touchpad Press</td><td>1</td><td>272</td><td>0 or 1</td><td>0 Released/1 Pressed</td></tr>
<tr><td>Touchpad Touch</td><td>1</td><td>325</td><td>0 or 1</td><td>0 Finger Removed/1 Finger Touched</td></tr>
<tr><td>Touchpad Touch</td><td>1</td><td>330</td><td>0 or 1</td><td>0 Finger Removed/1 Finger Touched</td></tr>
<tr><td>Two Finger Touch</td><td>1</td><td>333</td><td>0 or 1</td><td>0 Second Finger Removed/1 Second Finger Touched</td></tr>
<tr><td>Two Finger Touch</td><td>3</td><td>47</td><td>0 or 1</td><td>0 Second Finger Removed/1 Second Finger Touched</td></tr>
<tr><td>Touchpad X</td><td>3</td><td>53</td><td>1 to 1919</td><td>Horizontal location of the finger, 0 Left/1919 Right</td></tr>
<tr><td>Touchpad Y</td><td>3</td><td>54</td><td>1 to 941</td><td>Vertical location of the finger, 0 Top/941 Bottom</td></tr>
<tr><td>Touch Counter</td><td>3</td><td>57</td><td>Any Positive Number</td><td>0+ The number of times the touch pas has been touched/-1 Not currently touched</td></tr>
</table>

## Sample Code

Reacting to an event would look like this:

```python
# If a button was pressed or released
if ev_type == 1:

    # React to the X button
    if code == 304 and value == 0:
        print("The X button was released")
    elif code == 304 and value == 1:
        print("The X button was pressed")
```

This is assuming the events file has been opened and a while loop has been initiated (see [main.py](main.py) or [tank.py](tank.py)).

---

## Repo Resources

- [Pybricks](https://docs.pybricks.com/en/latest/ev3devices.html)
- [Python for EV3](https://education.lego.com/en-us/product-resources/mindstorms-ev3/teacher-resources/python-for-ev3)

<a href="https://codeadam.ca">
<img src="https://codeadam.ca/images/code-block.png" width="100">
</a>
