#! /usr/bin/env Python3

'''
Create a program that simulates a garge door opener / Finite State Machie with
6 states and 2 inputs.

There is 1 Clicker Button. If the door is open or closed it will complete it's
cycle until the door is closed or open.
Door: Closed -> Button Clicked -> Door: Opening -> Cycle Complete -> Door: Open

If the door is currently opening or closing clicking the button will make the
door stop where it is. When clicked the door will go the oposite direction,
until complete or the button is clicked again.

'''
transitions = {
    ("button_clicked", "OPEN"): "CLOSING",
    ("button_clicked", "CLOSED"): "OPENING",
    ("button_clicked", "CLOSING"): "STOPPED WHILE CLOSING",
    ("button_clicked", "OPENING"): "STOPPED WHILE OPENING",
    ("cycle_complete", "CLOSING"): "CLOSED",
    ("cycle_complete", "OPENING"): "OPEN",
    ("cycle_complete", "EMERGENCY_OPENING"): "OPEN"
}

input = '''
button_clicked
cycle_complete
button_clicked
button_clicked
button_clicked
button_clicked
button_clicked
cycle_complete
'''

state = "CLOSED"
for command in input.split():
    if (command, state) in transitions:
        state = transitions[(command, state)]
    out = ":> %s\nDoor: %s" %(command, state)
    print(out)

'''
if __name__ == "__main__":
    print('You\'re in main!')
    '''
