# Google Store Nexus  Availability Checker
A simple Python 3 script that checks if you can order a specified Nexus device in the Google Store. It prints the non-availability to standard output and triggers a pushbullet notification as soon as the device is available.

## Requirements

Install from provided requirements.txt:
```
pip3 install -r requirements.txt
````

Install manually:
```
pip3 install requests lxml pushbullet.py
```

## Usage

The script is supposed to be run via systemd-timer or as a cronjob.

You need a valid Pushbullet Access Token, which you can find in the settings: https://www.pushbullet.com/#settings

Define the Nexus-device you want to buy by providing it's name. The following versions have been tested:
* 5x
* 6p
* 6
* 9

Also define the Nexus-variant (color) you'd like to order. The following variations are available:

### Nexus 6P:

English:
* Aluminium
* Frost
* Graphite

German:
* Aluminium
* Grafit
* Kristallweiß

### Nexus 5X:

English:
* Carbon
* Quartz
* Ice

German:
* Anthrazit
* Eisblau
* Quarz

Execute the script as follows:
```
PB_API_KEY=your_token NEXUS_DEVICE=your-device NEXUS_VARIANT=color ./nexus_availability.py
```

## Caveats
While availability checking is no longer based on the user's locale/country, the color/variant is. The variant/color is not optional right now, so this version of the checker no longer works for Nexus 9 and other devices, unless you also add their color.
## Todo:
* fix caveat :)
