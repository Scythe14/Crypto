#!/usr/bin/env python

import codecs


def hex_2_b64(s):
    return codecs.encode(codecs.decode(s, 'hex'), 'base64').decode()


if __name__ == '__main__':
   print(hex_2_b64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")),
