import struct

import bleak

_MODEL_NBR_UUID = "00002a24-0000-1000-8000-00805f9b34fb"
_CHARACTERISTICS_UUID = "00008651-0000-1000-8000-00805f9b34fb"


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


async def connect(bt_address: str, function=None):
    try:
        async with bleak.BleakClient(bt_address, timeout=5) as client:
            print("CONNECTED!")
            model_number = await client.read_gatt_char(_MODEL_NBR_UUID)
            print("Model Number: {0}".format("".join(map(chr, model_number))))

            previous_state = bytearray()

            while True:
                data = await client.read_gatt_char(_CHARACTERISTICS_UUID)
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

                if function is not None:
                    function(gamepad_state)
    except bleak.BleakError:
        print('Timeout')
    except OSError:
        print('Disconnected')
