#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os
import time

from sys import exit
from lxml import html
from pushbullet import Pushbullet

api_key = os.getenv('PB_API_KEY', 0)
pb = Pushbullet(api_key)
nexus_device = os.getenv('NEXUS_VARIANT', 0)
store_url = "https://store.google.com/product/nexus_"
store_content = requests.get(store_url+nexus_device)
store_tree = html.fromstring(store_content.text)
notification_title = "Google Store Checker"
notification_body = "Order your Nexus "+nexus_device.upper()+" now!"
notification_triggered = 0
availability = store_tree.xpath('//p[@class="out-of-stock-text"]/text()')

while notification_triggered == 0:
    if len(availability) > 0 and "Bald" in availability[0]:
        print("Google Store Checker: Not available yet.")
        time.sleep(120)
    elif len(availability) > 0 and "soon" in availability[0]:
        print("Google Store Checker: Not available yet.")
        time.sleep(120)
    else:
        # make sure to only notify once
        print(notification_body)
        push = pb.push_note(notification_title, notification_body)
        notification_triggered = 1
