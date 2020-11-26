#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: bboysoul
import requests
import json
import sys
import os

headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = sys.argv[2]

def msg(text):
    json_text= {
     "msgtype": "text",
        "at": {
            "isAtAll": True
        },
        "text": {
            "content": text
        }
    }
    print requests.post(api_url,json.dumps(json_text),headers=headers).content

if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)

