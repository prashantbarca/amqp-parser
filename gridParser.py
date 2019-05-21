import json
from pprint import pprint
import hammer as h
import scapy.all as scapy


def openPayloadData(payload_data):
    with open(payload_data) as json_data:
        data = json.load(json_data)
        return data

def sampleEvents_parser():
    parser = h.sequence(

    )
    return parser

def pollingEngine_parser():
    parser = h.sequence(

    )
    return parser

def envelope_parser():
    parser = h.sequence(

    )
    return parser

def measurementDevice_parser():
    parser = h.sequence(

    )
    return parser

def sensors_parser():
    parser = h.sequence(

    )
    return parser

def schemaVersion_parser():
    parser = h.sequence(
        h.token('0.6'),  #SchemaVersion
        h.end_p()
    )
    return parser

def init_parser():
    return h.sequence(h.many1(h.choice(
        #sampleEvents_parser,
        #pollingEngine_parser,
        #envelope_parser,
        #measurementDevice_parser,
        #sensors_parser,
        schemaVersion_parser()
    )))

def parse(string):
    parser = init_parser()
    print(repr(string))
    result = parser.parse(string)
    print(result)
    if result != None:
        return True
    else:
        return False

def main():
    payload_list = openPayloadData('jsonpayloaddata.json')
    print(repr(payload_list["schemaVersion"]))
    if (parse(str(payload_list["schemaVersion"]))):
        print("\n!------ success! checking next one... ----!\n")
        #continue
    else:
        print("\ndid not pass. Checking next one..\n")
        #continue
    print("All strings went through Hammers check!")
    return

main()