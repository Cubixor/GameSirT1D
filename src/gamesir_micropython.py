import struct

import bluetooth
import uasyncio as asyncio

import aioble

_DEVICE_INFO_SERVICE_UUID = bluetooth.UUID(0x180a)
_MODEL_NBR_UUID = bluetooth.UUID(0x2a24)
_GAMEPAD_SERVICE_UUID = bluetooth.UUID(0x8650)
_GAMEPAD_CHARACTERISTICS_UUID = bluetooth.UUID(0x8651)


class GamepadState:
    def __init__(self, data: bytearray):
        self.l1 = bool(data[9] & 0x40)
        self.l2 = int(data[7])  # int 0-255
        self.r1 = bool(data[9] & 0x80)
        self.r2 = int(data[8])

        self.x = bool(data[9] & 0x08)
        self.y = bool(data[9] & 0x10)
        self.a = bool(data[9] & 0x01)
        self.b = bool(data[9] & 0x02)
        self.menu = bool(data[9] & 0x04)
        self.c1 = bool(data[10] & 0x04)
        self.c2 = bool(data[10] & 0x08)
        self.pwr = bool(data[10] & 0x10)

        self.down = bool(data[11] == 0x05)
        self.up = bool(data[11] == 0x01)
        self.left = bool(data[11] == 0x07)
        self.right = bool(data[11] == 0x03)

        self.lx = int(((data[2]) << 2) | (data[3] >> 6))
        self.ly = int(((data[3] & 0x3f) << 4) + (data[4] >> 4))
        self.rx = int(((data[4] & 0xf) << 6) | (data[5] >> 2))
        self.ry = int(((data[5] & 0x3) << 8) + (data[6]))

    def print(self):
        print(
            "l1: {}\nl2: {}\nr1: {}\nr2: {}\nx: {}\ny: {}\na: {}\nb: "
            "{}\nc1: {}\nc2: {}\nmenu:  {}\npwr: {} \ndown:  {}\nup:    "
            "{}\nleft:  {}\nright: {}\nlx: {}\nly: {}\nrx: {}\nry: {}\n".format(
                self.l1, self.l2, self.r1, self.r2, self.x, self.y, self.a, self.b, self.c1, self.c2,
                self.menu, self.pwr, self.down, self.up, self.left, self.right, self.lx, self.ly, self.rx, self.ry
            ))


async def connect(address: str, function):
    device = aioble.Device(1, address)

    try:
        connection = await device.connect(timeout_ms=5000)
        print("CONNECTED!")

        service = await connection.service(_DEVICE_INFO_SERVICE_UUID)
        model_characteristic = await service.characteristic(_MODEL_NBR_UUID)
        model_number = await model_characteristic.read()
        print("Model Number: {0}".format("".join(map(chr, model_number))))

        previous_state = bytearray()
        service = await connection.service(_GAMEPAD_SERVICE_UUID)
        characteristic = await service.characteristic(_GAMEPAD_CHARACTERISTICS_UUID)

        while True:
            data = await characteristic.read()
            status_code = struct.unpack('H', data[:2])[0]

            if status_code != 50593:
                continue
            if data[0] == 0xc9:
                continue
            if previous_state == data:
                continue

            previous_state = data
            gamepad_state = GamepadState(data)
            gamepad_state.print()
            function(gamepad_state)

    except asyncio.TimeoutError:
        print('Timeout')
    except aioble.GattError:
        print('Disconnected')

