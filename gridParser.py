import json
from pprint import pprint
import socket
import hammer as h
import logging
import base64
import time
import signal
import sys

def openPayloadData(payload_data):
    with open(payload_data, encoding="utf-8-sig") as json_data:
        data = json.load(json_data)
        return data


pprint(openPayloadData('jsonpayloaddata.json'))

def init_parser():
    return h.sequence(h.many1(h.choice(
    )))

def parse(string):
    parser = init_parser()
    #print(repr(string[0:-1]))
    result = parser.parse(string[0])
    print(result)
    if result != None:
        # print(repr(result))
        # print(repr(string))
        return True
    else:
        return False

def main():
    payload_list = extract_payload()
    for i in range(len(payload_list)):
        if(parse(payload_list[i])):
            print("\n!------ success! checking next one... ----!\n")
            continue
        else:
            print("\ndid not pass. Checking next one..\n")
            continue

    print("All strings went through Hammers check!")
    return
main()