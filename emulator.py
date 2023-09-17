import asyncio

import vgamepad as vg

import gamesir

# EDIT HERE
ADDRESS = "C6:86:A1:04:52:48"


def press_release(button: vg.XUSB_BUTTON, press: bool):
    if press:
        gamepad.press_button(button)
    else:
        gamepad.release_button(button)


def on_state_update(state: gamesir.GamepadState):
    press_release(vg.XUSB_BUTTON.XUSB_GAMEPAD_X, state.x)
    press_release(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y, state.y)
    press_release(vg.XUSB_BUTTON.XUSB_GAMEPAD_A, state.a)
    press_release(vg.XUSB_BUTTON.XUSB_GAMEPAD_B, state.b)
    press_release(vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK, state.c1)
    press_release(vg.XUSB_BUTTON.XUSB_GAMEPAD_START, state.c2)
    press_release(vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE, state.menu)
    press_release(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN, state.down)
    press_release(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP, state.up)
    press_release(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT, state.left)
    press_release(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT, state.right)
    press_release(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER, state.l1)
    press_release(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER, state.r1)

    gamepad.left_trigger(state.l2)
    gamepad.right_trigger(state.r2)
    gamepad.left_joystick_float(state.lx / 512 - 1, 1 - state.ly / 512)
    gamepad.right_joystick_float(state.rx / 512 - 1, 1 - state.ry / 512)

    gamepad.update()


try:
    gamepad = vg.VX360Gamepad()
    asyncio.run(gamesir.connect(ADDRESS, on_state_update))
except KeyboardInterrupt:
    pass
