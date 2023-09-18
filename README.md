# GameSirT1D API and emulator


## What is it?
This project was created to enable the use of a GameSirT1D gamepad 
(made specifically for the DJI Ryze Tello drone) as a normal game controller. 
You can use it either to create your own software and implement support for this gamepad or emulate it
so that your computer "thinks" it's a Xbox360 controller.

## Source
Reading button values from the controller was based on a
[Diallomm/hack_GamesirT1d](https://github.com/Diallomm/hack_GamesirT1d) project.

## Requirements and limitations

### Windows
The project was tested on a Windows PC running Python 3.10, but it will also work on Linux.
It requires [bleak](https://pypi.org/project/bleak/) and optionally [vgamepad](https://pypi.org/project/vgamepad/) 
to use emulator feature.
Install all these dependencies using `pip3 install -r requirements.txt` command.

### ESP32
You can use the micropython version of the API (`gamesir_micropython.py`) on any ESP32 device.
It was tested on a RaspberryPi Pico W. It requires 
[aioble](https://github.com/micropython/micropython-lib/tree/master/micropython/bluetooth/aioble)
module (you need to download it to your device). 

## Usage

### API (Windows and Linux)
To use the project as an API, simply copy `gamesir.py` file to your project and use it as shown
in the example (`example.py`). Remember that you need to use your controller's MAC address, instead
of the provided one.

### API (Micropython)
Use the project as described in the Windows and Linux section. Just instead of `gamesir.py` use 
`gamesir_micropython.py`


### Emulate
To use your controller for playing games on your PC you need `gamesir.py` and `emulator.py` files.
You will need to edit `emulator.py` file and put your controller's MAC address into the `ADDRESS` variable.
You can find it on the sticker on your gamepad. After you do it, simply launch `emulator.py` file.

<br>

##### REMEMBER TO INSTALL THE REQUIRED PACKAGES BEFOREHAND!

