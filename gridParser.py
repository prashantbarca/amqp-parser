import json
import hammer as h
import scapy.all as scapy


def openPayloadData(payload_data):
    with open(payload_data, encoding="utf-8-sig") as json_data:
        data = json.load(json_data)
        return data

#def init_parser():
    #return h.sequence(h.many1(h.choice(
    #)))

def parse(string):
    #parser = init_parser()
    result = parser.parse(string[0])
    print(result)
    if result != None:
        return True
    else:
        return False

def main():
    payload_list = openPayloadData('jsonpayloaddata.json')
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