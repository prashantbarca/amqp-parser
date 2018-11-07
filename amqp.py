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

def length_block():

    parser = h.sequence(h.and_(h._h_length_value(h.uint8(), h.many(h.ch_range('\x00', '\xff')))))
    return parser

def sequence_parser():
    parser = h.sequence(
        h.ch('\x01'),
        h.uint16(),
        h.uint32(),
        h.uint16(),
        h.uint16(),
        h.many1(h.ch_range('\x00', '\xff')),
        h.end_p()
    )
    return parser

def init_parser():
    return h.sequence(h.many1(h.choice(sequence_parser(), length_block())))

def parse(string):
    parser = init_parser()
    print(repr(string))
    result = parser.parse(string)
    print(result)
    if result != None and result[-1][-1] == '\xce':
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

    print("All strings passed Hammers check!")
    return
main()
