#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#
"""
Helpers to recognize packets as valid Goose frames
"""
import socket
import hammer as h
import logging
import base64
import time
import signal
import sys

LOG_FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
# change level to logging.DEBUG if you need debugging output
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)

def act_join(p, user_data=None):
    return p


def relay_operate_configuration():
    header = h.token('\xa5\xce')
    length = h.uint8()
    breaker_bits = h.uint8()
    remote_bits = h.uint16()
    remote_pulse = h.uint8()
    reserved = h.uint8()

    parser = h.sequence(header,
                        length,
                        breaker_bits,
                        remote_bits,
                        remote_pulse,
                        reserved,
                        h.repeat_n(h.uint8(), 2),
                        h.repeat_n(
                            h.sequence(h.uint8(), 
                                       h.uint8(), 
                                       h.uint8()), 
                                       32),
                        h.uint8())
    return parser

def relay_definition_message():
    header = h.token('\xa5\xc0')
    any_char = h.ch_range('\x00', '\xff')

    parser = h.sequence(header,
                        h.uint8(),
                        h.uint8(),
                        h.uint8(),
                        h.uint8(),
                        h.many1(any_char))
 
    return parser

def fast_message_block():
    header = h.token('\xa5\x46')
    length = h.uint8()
    routing_address = h.repeat_n(h.uint8(), 5)
    status = h.uint8()
    function_code = h.uint8()
    sequence_byte = h.uint8()
    response_number = h.uint8()
    any_value = h.many1(h.ch_range('\x00', '\xff'))
    crc = h.uint16()
    
    parser = h.sequence(header,
                        length,
                        routing_address,
                        status,
                        function_code,
                        sequence_byte,
                        response_number,
                        any_value)

    return parser


def demand_fast_meter_configuration_block():
    header = h.token("\xa5\xc2")
    length = h.uint8()
    scale_factors = h.uint8()
    analog = h.uint8()
    samples = h.uint8()
    digital = h.uint8()
    analog_offset = h.uint16()
    timestamp_offset = h.uint16()
    digital_offset = h.uint16()
    analog_signal = h.repeat_n(h.uint8(), 10)
    all_signals = h.repeat_n(analog_signal, 5)
    checksum = h.ch_range('\x00', '\xff')
    calculation_blocks = h.uint8()
    parser = h.sequence(header, 
                        length,
                        h.uint8(),
                        h.uint8(),
                        scale_factors,
                        analog,
                        samples,
                        digital,
                        calculation_blocks,
                        analog_offset,
                        timestamp_offset,
                        digital_offset,
                        all_signals,
                        checksum)


    return parser

def peak_fast_meter_configuration_block():
    header = h.token("\xa5\xc3")
    length = h.uint8()
    scale_factors = h.uint8()
    analog = h.uint8()
    samples = h.uint8()
    digital = h.uint8()
    analog_offset = h.uint16()
    timestamp_offset = h.uint16()
    digital_offset = h.uint16()
    analog_signal = h.repeat_n(h.uint8(), 10)
    all_signals = h.repeat_n(analog_signal, 5)
    checksum = h.ch_range('\x00', '\xff')
    calculation_blocks = h.uint8()
    parser = h.sequence(header, 
                        length,
                        h.uint8(),
                        h.uint8(),
                        scale_factors,
                        analog,
                        samples,
                        digital,
                        calculation_blocks,
                        analog_offset,
                        timestamp_offset,
                        digital_offset,
                        all_signals,
                        checksum)

    return parser

def fast_meter_configuration_block():
    header = h.token("\xa5\xc1")
    length = h.uint8()
    scale_factors = h.uint8()
    analog = h.uint8()
    samples = h.uint8()
    digital = h.uint8()
    analog_offset = h.uint16()
    timestamp_offset = h.uint16()
    digital_offset = h.uint16()
    analog_signal = h.repeat_n(h.uint8(), 10)
    all_signals = h.repeat_n(analog_signal, 7)
    checksum = h.ch_range('\x00', '\xff')
    calculation_blocks = h.uint8()
    parser = h.sequence(header, 
                        length,
                        h.uint8(),
                        h.uint8(),
                        scale_factors,
                        analog,
                        samples,
                        digital,
                        calculation_blocks,
                        analog_offset,
                        timestamp_offset,
                        digital_offset,
                        all_signals,
                        checksum)


    return parser

def fast_meter_message():
    header = h.token('\xa5\xd1')
    any_char = h.ch_range('\x00', '\xff')

    parser = h.sequence(header,
                        h.uint8(),
                        h.ch('\x00'),
                        h.repeat_n(h.uint32(), 7),
                        h.uint64(),
                        h.repeat_n(any_char, 167),
                        any_char)
    return parser



def init_parser():
    return h.sequence(h.many1(h.choice(relay_definition_message(), fast_meter_configuration_block(), fast_meter_message(), demand_fast_meter_configuration_block(), peak_fast_meter_configuration_block(), fast_message_block(), relay_operate_configuration())), h.end_p())

def parse(string):
    parser = init_parser()
    result = parser.parse(string)
    if result != None: #and result[1] == len(string):
        print(repr(result))
        #print(len(result[5]))
        print(repr(string))
        return True
    else:
        return False
#
def signal_handler(sig, frame):
    s.close()
    print('You pressed Ctrl+C!')
    sys.exit(0)


def main():

    signal.signal(signal.SIGINT, signal_handler)
    s.bind(("0.0.0.0", 9005))
    s.listen(5)
    count = 0
    #while count<1000:
    while True:
        (client, address) = s.accept()
        response = str(parse(base64.b64decode(client.recv(65535))))
        print(response)
        client.sendall(base64.b64encode(response))
        print("====="+str(count)+"=====")
        count = count+1
    s.close()

#
if __name__ == '__main__':
    import sys
    s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    main()
