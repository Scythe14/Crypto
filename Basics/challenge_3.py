#!/usr/bin/env python
# coding: utf8

# Cryptopals Challenges - Dany Bouca Nova
# https://cryptopals.com/sets/1/challenges/3

import codecs


def decode_hex_string(hex_string):
    return codecs.decode(hex_string, 'hex')


def decrypt(cipher, key):
    return ''.join([chr(i ^ key).lower() for i in cipher])


def get_score_eng_plaintext(s):
    letter_frequency = "ETAOIN SHRDLU"
    total = 0

    for c in s:
        if c in letter_frequency:
            total += 1
    return total


def single_char_xor(s):
    max_score = 0
    character = ''

    for i in range(0, 255):
        tmp = decrypt(decode_hex_string(s), i)
        score = get_score_eng_plaintext(tmp)
        if score > max_score:
            max_score = score
            character = i
    return chr(character) + " : " + decrypt(decode_hex_string(s), character)

print(single_char_xor("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"))