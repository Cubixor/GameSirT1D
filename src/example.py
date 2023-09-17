import asyncio

import gamesir

# EDIT THIS LINE TO MATCH YOUR GAMEPAD MAC ADDRESS
ADDRESS = "C6:86:A1:04:52:48"


# This method will be called after a new state is received from gamepad
def on_state_update(state: gamesir.GamepadState):
    # Check if button is pressed
    if state.x:
        print("X button is pressed!")

    # Get joystick values (value from 0 to 1024, with the middle in 512)
    print("Left joystick X axis: " + state.lx)

    # Get trigger values (value from 0 to 255)
    print("Right trigger value: " + state.r2)


# Run the connect method on another thread
asyncio.run(gamesir.connect(ADDRESS, on_state_update))
