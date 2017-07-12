#!/usr/bin/python2
# coding : utf8

"""
The cryptopals crypto challenges
Challenge: Single-byte XOR cipher
url: https://cryptopals.com/sets/1/challenges/4
"""

import sys
import codecs


def decode_hex_string(hex_string):
    """
    Decodes hex string
    """
    return codecs.decode(hex_string, 'hex')


def decipher_text(cipher_text, xor_key):
    """
    Recover the plaintext from the ciphertext
    """
    text = ""
    for i in cipher_text:
        text += chr(ord(i) ^ xor_key)
    return text.lower()


def score(cipher_text):
    """
    Iterates on each word and try to find a match in a language dictionary.
    """
    frequent_characters = "etaoin shrdlu"
    number_of_match = sum(letter in frequent_characters for letter in cipher_text)
    return float(float(number_of_match) / float(len(cipher_text)))


if __name__ == '__main__':
    SOURCE_FILE = open(sys.argv[1], "r")
    CIPHER_TEXT = SOURCE_FILE.read().strip()
    LINES_FROM_CIPHER_TEXT = CIPHER_TEXT.split('\n', CIPHER_TEXT.count('\n'))
    BEST_SCORE = 0.0
    KEY = ""
    CLEAR_TEXT = ""
    for current_line in LINES_FROM_CIPHER_TEXT:
        current_line = decode_hex_string(current_line.translate(None, ' \n\r\t').lower())
        for key_element in range(0, 256):
            plaintext = decipher_text(current_line, key_element).strip()
            score_character = float(score(plaintext))
            if BEST_SCORE < score_character:
                BEST_SCORE = score_character
                KEY = str(key_element)
                CLEAR_TEXT = plaintext
    print "Key: " + KEY + "\nplaintext: " + "\"" + CLEAR_TEXT + "\""
    print 'Score: %.2f/1' % BEST_SCORE
