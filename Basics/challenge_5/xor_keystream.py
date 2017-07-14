#!/usr/bin/python2


"""
The cryptopals crypto challenges
Challenge: Single-byte XOR cipher
url: https://cryptopals.com/sets/1/challenges/5
"""


import sys
import codecs

def xor_key_stream(text, key_stream, flag):
    """
    Ciphers text with key_stream if flag == 'cipher'
    Deciphers text with key_stream if flag == 'decipher'
    """
    output_text = ""
    length_key_stream = len(key_stream)
    i = 0
    for character in text:
        output_text += chr(ord(character) ^ ord(key_stream[i]))
        i = (i + 1) % length_key_stream
    if flag == 'cipher':
        return codecs.encode(output_text, 'hex')
    elif flag == 'decipher':
        return output_text


if __name__ == '__main__':
    SOURCE_TEXT = open(sys.argv[1], "r").read()
    CIPHER_TEXT = xor_key_stream(SOURCE_TEXT, "ICE", 'cipher')
    print "CIPHER -- Plaintext: " + SOURCE_TEXT + "\nCipher_text: " + CIPHER_TEXT + '\n'
    PLAINTEXT = xor_key_stream(codecs.decode(CIPHER_TEXT, 'hex'), "ICE", 'decipher')
    print "DECIPHER -- Cipher_text: " + CIPHER_TEXT + "\nplaintext: " + PLAINTEXT
