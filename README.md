# ngs-light-bulb-controller
Python wrapper to switch on/off my NGS Gleam 727C light bulbs

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

If you're using a venv and need to map this script to a stream deck, you'll need to explicitely use the python exec of the venv.


