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

def connection_start_parser():
    parser = h.sequence(
        h.ch('\x01'),  # type
        h.uint16(),  # Channel
        h.uint32(),  # Length
        h.token("\x00\x0a"),  # Class
        h.token("\x00\x0a"),  # Method
        h.end_p()
    )
    return parser


def connection_start_ok_parser():
    parser = h.sequence(
        h.ch('\x01'),  # type
        h.uint16(),  # Channel
        h.uint32(),  # Length
        h.token("\x00\x0a"),  # Class
        h.token("\x00\x0b"),  # Method
        h.end_p()
    )
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
        h.token("\x00\x00"), # most likely going to change this according to the message
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
        h.ch('\x00'),# Known-Host # most likely going to change this according to the message
        h.end_p()
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
        h.ch('\x00'), # Out-of-bounds
        h.end_p()
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
        h.uint32(), # Channel-Id
        h.end_p()
    )
    return parser

def queue_declare_parser():
    parser = h.sequence(
        h.ch('\x01'), # type
        h.uint16(), # Channel
        h.uint32(), # Length
        h.token("\x00\x32"), # Class
        h.token("\x00\x0a"), # Method

        # Arguments
        h.uint16(), # Ticket
        # how do you parse that long message?#Queue
        h.many(h.ch_range('\x00', '\xff')),
        #When you parse this out... (, ,, , 0L, ('','','',''))
        h.end_p()
    )
    return parser

def queue_declare_ok_parser():
    parser = h.sequence(
        h.ch('\x01'), # type
        h.uint16(), # Channel
        h.uint32(), # Length
        h.token("\x00\x32"), # Class
        h.token("\x00\x0b"), # Method

        # Arguments
        #how do you parse that long message? #Queue
        h.many(h.ch_range('\x00', '\xff')),
        #h.uint32(), # message-count
        #h.uint32(), # consumer-count
        h.end_p()
    )
    return parser

def basic_consume_parser():
    parser = h.sequence(
        h.ch('\x01'), # type
        h.uint16(), # Channel
        h.uint32(), # Length
        h.token("\x00\x3c"), # Class
        h.token("\x00\x14"), # Method

        # Arguments
        h.uint16(), # Ticket
        # how do you parse that long message? #Queue
        h.many(h.ch_range('\x00', '\xff')),
        # consumer-tag
        h.end_p()
    )
    return parser

def basic_consume_ok_parser():
    parser = h.sequence(
        h.ch('\x01'), # type
        h.uint16(), # Channel
        h.uint32(), # Length
        h.token("\x00\x3c"), # Class
        h.token("\x00\x15"), # Method

        # Arguments
        # consumer-tag
        h.end_p()
    )
    return parser

def basic_publish_parser():
    parser = h.sequence(
        h.ch('\x01'),  # type
        h.uint16(),  # Channel
        h.uint32(),  # Length
        h.token("\x00\x3c"),  # Class
        h.token("\x00\x28"),  # Method
        h.end_p()
    )
    return parser

def basic_deliver_parser():
    parser = h.sequence(
        h.ch('\x01'),  # type
        h.uint16(),  # Channel
        h.uint32(),  # Length
        h.token("\x00\x3c"),  # Class
        h.token("\x00\x3c"),  # Method
        h.end_p()
    )
    return parser


def channel_close_parser():
    parser = h.sequence(
        h.ch('\x01'), # type
        h.uint16(), # Channel
        h.uint32(), # Length
        h.token("\x00\x14"), # Class
        h.token("\x00\x28"), # Method

        # Arguments
        h.uint16(), # Replay-code
        #Replay-text
        h.uint16(), # Class-Id
        h.uint16(), # Method-Id
        h.end_p()
    )
    return parser

def channel_close_ok_parser():
    parser = h.sequence(
        h.ch('\x01'), # type
        h.uint16(), # Channel
        h.uint32(), # Length
        h.token("\x00\x14"), # Class
        h.token("\x00\x29"), # Method

        # No arguments
        h.end_p()
    )
    return parser


def connection_close_parser():
    parser = h.sequence(
        h.ch('\x01'),  # type
        h.uint16(),  # Channel
        h.uint32(),  # Length
        h.token("\x00\x0a"),  # Class
        h.token("\x00\x32"),  # Method

        # Arguments
        h.uint16(), # Replay-code
        #Replay-text
        h.uint16(), # Class-Id
        h.uint16(), # Method-Id
        h.end_p()
    )
    return parser

def connection_close_ok_parser():
    parser = h.sequence(
        h.ch('\x01'),  # type
        h.uint16(),  # Channel
        h.uint32(),  # Length
        h.token("\x00\x0a"),  # Class
        h.token("\x00\x33"),  # Method

        # No arguments
        h.end_p()
    )
    return parser

def init_parser():
    return h.sequence(h.many1(h.choice(
        length_block(),
        connection_start_parser(),
        connection_start_ok_parser(),
        connection_tune_parser(),
        connection_tune_ok_parser(),
        connection_open_vhost_parser(),
        channel_open_parser(),
        channel_open_ok_parser(),
        queue_declare_parser(),
        queue_declare_ok_parser(),
        basic_consume_parser(),
        basic_consume_ok_parser(),
        basic_publish_parser(),
        basic_deliver_parser(),
        channel_close_parser(),
        channel_close_ok_parser(),
        connection_close_parser(),
        connection_close_ok_parser()
    )))

def parse(string):
    parser = init_parser()
    result = parser.parse(string[0:-1])
    if result != None:
        if result[0][0][2] >= 10 and result[0][0][2] <= 500:
           for i in range(len(result[0][0][3])):
            if result[0][0][3][i]:
                print(result[0][0][3][i])
                continue
            else:
                return False
        return True
    else:
        return False

def main():
    payload_list = extract_payload()
    for i in range(len(payload_list)):
        if(parse(payload_list[i])):
            print("\n!------ success! checking next one... ----!\n")
            """** check each message for a hex code that states its gonna have a string (figure out what messages are you interested in
             and have it in a way to check the that are interesting """
            continue
        else:

            print("\ndid not pass. Checking next one..\n")
            continue

    print("All strings went through Hammers check!")
    return

main()

# the way to get into a string or a long message is to use brackets