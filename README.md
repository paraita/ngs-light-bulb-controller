# ngs-light-bulb-controller
Python wrapper to switch on/off my NGS Gleam 727C light bulbs

![IMG_4626](https://user-images.githubusercontent.com/1413759/139602781-c3f6dc80-bfab-42a3-ba67-9181dbf3771a.GIF)


## Installation

Don't forget to install the dependencies.
This script requires to set the following variables in a .env file, next to the script:

* L_DEVICE_ID
* L_IP_ADDR
* L_LOCAL_KEY
* R_DEVICE_ID
* R_IP_ADDR
* R_LOCAL_KEY

L is for the left bulb, R for the right bulb.

We assume the bulbs are already declared and configured on your machine.
To do so, go [here](https://github.com/jasonacox/tinytuya).


## Gluing

If you're using a venv and need to map this script to a stream deck, you'll need to explicitely use the python exec of the venv.
On my Mac, I use Automator to create two Applications:

* one for turning ON the lights
* one for turning OFF the lights

![image](https://user-images.githubusercontent.com/1413759/139602540-d37ffc0c-ec8f-4635-8dc2-69d16d261f74.png)

Then you just have to create a new button on your stream deck for each of these actions:

![Capture d’écran 2021-10-31 à 12 10 19](https://user-images.githubusercontent.com/1413759/139602859-13b55191-479e-4565-bbfc-707e8e696856.png)


## Usage

Assuming you've created a virtual python 3 environment named `venv`:

```bash
source venv/bin/activate
./ngs-switch.py ON
./ngs-switch.py OFF
```

