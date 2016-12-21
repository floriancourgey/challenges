#! /usr/bin/env python3
# coding: utf-8

import requests

def get(url):
    print("Appel GET "+url)
    r = requests.get(url, cookies=cookies)
    html = r.text
    print("html reçu", html)
    return html
def post(url, data):
    print("Appel POST "+url, data)
    r = requests.post(url, cookies=cookies, data=data)
    html = r.text
    print("html reçu", html)
    return html
