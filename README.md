# Google Store Nexus  Availability Checker
A simple Python 3 script that checks if you can order a specified Nexus device in the Google Store. It prints the non-availability to standard output and triggers a pushbullet notification as soon as the device is available.

## Usage

The script is supposed to be run via systemd-timer or as a cronjob. 

You need a valid Pushbullet Access Token, which you can find in the settings: https://www.pushbullet.com/#settings

Define the Nexus-variant you want to buy by providing it's name. The following versions have been tested: 
* 5x
* 6p
* 6
* 9

Execute the script as follows:
```
PB_API_KEY=your_token NEXUS_VARIANT=your_device ./nexus_availability.py
```

## Caveats
* Currently german and english responses are supported. The Google Store uses your IP address to determine your location. If you are using this script on a system that might trigger a localized response from the Google Store, please add your translation of "soon" to the script. I'll gladly accept your pull request.
* Make sure you're able to disable the checker as soon as the device is available to ensure you do not end up being spammed with availability-messages as soon as your Nexus is available. 😅

## Todo:
Check if device store availability notification has already been triggered in order to not be spammed with notifications.
