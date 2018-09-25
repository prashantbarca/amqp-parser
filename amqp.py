import hammer as h
import scapy.all as scapy

def extract_payload():
    pkts = scapy.rdpcap('amqp.pcap')
    pktlist = []
    for packet in pkts:
        try:
            payload = packet['TCP'].payload
            payload = str(payload)
        except:
            continue

        if (payload != "" and payload[0] == '\x01'):
            pktlist.append(payload)
        else:
            continue

    return pktlist

def init_parser():
    return h.sequence()

def parse(string):
    parser = init_parser()
    result = parser.parse(string)
    if result != None: #and result[1] == len(string):
        # print(repr(result))
        # print(repr(string))
        return True
    else:
        return False

def main():
    payload_list = extract_payload()
    for i in range(len(payload_list)):
        if(parse(payload_list[i])):
            print("success! checking next one...")
            continue
        else:
            print("Parser() returned false; the pcap file is not valid.")
            return
    print("All strings passed Hammers check!")
    return
main()