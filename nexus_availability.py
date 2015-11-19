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
nexus_device = os.getenv('NEXUS_DEVICE', 0)
nexus_variant = os.getenv('NEXUS_VARIANT', 0)
store_url = "https://store.google.com/product/nexus_"

def main():

    while True:
        store_content = requests.get(store_url+nexus_device)
        store_tree = html.fromstring(store_content.text)
        notification_title = "Google Store Checker"
        notification_body = "Order your Nexus {} now!".format(nexus_device.upper())
        for e in store_tree.xpath('//*[@data-variation-name="{}"]'.format(nexus_variant)):
            print(e.getparent().attrib["data-available"])
            if e.getparent().attrib["data-available"] == "true":
                print(notification_body)
                push = pb.push_note(notification_title,  notification_body)
                return
        print("Google Store Checker: Not available yet.")
        time.sleep(120)

main()
