#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os

from sys import exit
from lxml import html
from pushbullet import Pushbullet

api_key = os.getenv('PB_API_KEY', 0)
pb = Pushbullet(api_key)
phone = os.getenv('NEXUS_VARIANT', 0)
store_url = "https://store.google.com/product/nexus_"
store = requests.get(store_url+phone)
tree = html.fromstring(store.text)
notification_title = "Google Store Checker"
notification_body = "Order your Nexus "+phone.upper()+" now!"
availability = tree.xpath('//p[@class="out-of-stock-text"]/text()')

if len(availability) > 0 and "Bald" in availability[0]:
    print("Google Store Checker: Not available yet.")
elif len(availability) > 0 and "soon" in availability[0]:
    print("Google Store Checker: Not available yet.")
else:
    push = pb.push_note(notification_title, notification_body)
