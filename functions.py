#! /usr/bin/env python3
# coding: utf-8
import requests
import config

def get(url, returnRequests=False):
    print('functions | get URL ', url)
    r = requests.get(url, cookies={config.COOKIE_KEY:config.COOKIE_VAL})
    if returnRequests:
        return r
    else:
        return r.text
