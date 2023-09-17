# GameSirT1D API and emulator


## What is it?
This project was created to enable the use of a GameSirT1D gamepad 
(made specifically for the DJI Ryze Tello drone) as a normal game controller. 
You can use it either to create your own software and implement support for this gamepad or emulate it
so that your computer "thinks" it's a Xbox360 controller.

## Source
Reading button values from the controller was based on a
[`Diallomm/hack_GamesirT1d`](https://github.com/Diallomm/hack_GamesirT1d) project.

## Requirements and limitations
The project was tested on a Windows PC running Python 3.10.
It requires `asyncio`, `bleak` and optionally `vgamepad` to use emulator feature.
Install all these dependencies using `pip3 install -r requirements.txt` command.

## Usage

### API
To use the project as an API, simply copy `gamesir.py` file to your project and use it as shown
in the example (`example.py`). Remember that you need to use your controller's MAC address, instead
of the provided one.

### Emulate
To use your controller for playing games on your PC you need `gamesir.py` and `emulator.py` files.
You will need to edit `emulator.py` file and put your controller's MAC address into the `ADDRESS` variable.
You can find it on the sticker on your gamepad. After you do it, simply launch `emulator.py` file.
<br><b>REMEMBER TO INSTALL THE REQUIRED PACKAGES BEFOREHAND!</b>

