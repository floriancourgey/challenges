#! /usr/bin/env python3
# coding: utf-8
import requests
import config

def get(url):
    print('functions | get URL ', url)
    r = requests.get(url, cookies={config.COOKIE_KEY:config.COOKIE_VAL})
    return r.text
