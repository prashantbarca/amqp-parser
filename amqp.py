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


# h.token("\x00\x0a")
def length_block():


    parser = h.sequence(
    h.ch('\x01'),
    h.uint16(),
    h.and_(h._h_length_value(h.uint32(), h.ch_range('\x00', '\xff'))),
    h.uint32(),
    h.many(h.ch_range('\x00', '\xff')),
    h.end_p())
    return parser

def connection_tune_parser():
    parser = h.sequence(
        h.ch('\x01'), # type
        h.uint16(), # Channel
        h.uint32(), # Length
        h.token("\x00\x0a"), # Class
        h.token("\x00\x1e"), # Method

        # Arguments
        h.uint16(), # Channel max 
        h.uint32(), # Frame max
        h.uint16(), # Heartbeat
        h.end_p()
    )
    return parser

def connection_tune_ok_parser():
    parser = h.sequence(
        h.ch('\x01'), # type
        h.uint16(), # Channel
        h.uint32(), # Length
        h.token("\x00\x0a"), # Class
        h.token("\x00\x1f"), # Method

        # Arguments
        h.uint16(), # Channel max
        h.uint32(), # Frame max
        h.uint16(), # Heartbeat
        h.end_p()
    )
    return parser

def connection_open_vhost_parser():
    parser = h.sequence(
        h.ch('\x01'), # type
        h.uint16(), # Channel
        h.uint32(), # Length
        h.token("\x00\x0a"), # Class
        h.token("\x00\x28"), # Method

        # Arguments
        h.uint16(), # Virtual-Host
        h.uint32(), # Frame max
        h.uint16(), # Capabilities
        h.end_p()
    )
    return parser

def connection_open_vhost_ok_parser():
    parser = h.sequence(
        h.ch('\x01'), # type
        h.uint16(), # Channel
        h.uint32(), # Length
        h.token("\x00\x0a"), # Class
        h.token("\x00\x29"), # Method

        # Arguments
        h.uint8() # Known-Host
    )
    return parser

def channel_open_parser():
    parser = h.sequence(
        h.ch('\x01'), # type
        h.uint16(), # Channel
        h.uint32(), # Length
        h.token("\x00\x14"), # Class
        h.token("\x00\x0a"), # Method

        # Arguments
        h.uint8() # Out-of-bounds
    )
    return parser

def channel_open_ok_parser():
    parser = h.sequence(
        h.ch('\x01'), # type
        h.uint16(), # Channel
        h.uint32(), # Length
        h.token("\x16\x28"), # Class
        h.token("\x00\x0b"), # Method

        # Arguments
        h.uint32() # Channel-Id
    )
    return parser

def queue_declare_parser():
    parser = h.sequence(
        h.ch('\x01'), # type
        h.uint16(), # Channel
        h.uint32(), # Length
        h.token("\x16\x28"), # Class
        h.token("\x00\x0b"), # Method

        # Arguments
        h.uint32() # Channel-Id
    )
    return parser

def init_parser():
    #return h.sequence(h.many1(h.choice(sequence_parser(), length_block())))
    #return length_block()
    return connection_tune_parser()

def parse(string):
    parser = init_parser()
    print(repr(string[0:-1]))
    result = parser.parse(string[0:-1])
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
            print("success! checking next one...")
            continue

    print("All strings went through Hammers check!")
    return
main()
