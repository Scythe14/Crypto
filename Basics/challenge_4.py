#!/usr/bin/env python
# coding: utf8

# Cryptopals Challenges - Dany Bouca Nova
# https://cryptopals.com/sets/1/challenges/4

import codecs


def decode_hex_string(hex_string):
    return codecs.decode(hex_string, 'hex')


def decrypt(cipher, key):
    return ''.join([chr(i ^ key).lower() for i in cipher])


def get_score_eng(s):
    letter_frequency = {
        'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966,
        'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987,
        's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074, ' ': 1
    }
    total = 0

    for c in s:
        if c in letter_frequency:
            total += letter_frequency[c.lower()]
    return total


def single_char_xor_in_file(s):
    max_score = 0
    character = ''
    target_line = ''

    file = open(s, "r")
    for line in file.read().split('\n'):
        for i in range(0, 255):
            tmp = decrypt(decode_hex_string(line), i)
            score = get_score_eng(tmp)
            if score > max_score:
                max_score = score
                character = i
                target_line = line
    file.close()
    return chr(character) + " : " + decrypt(decode_hex_string(target_line), character)


print(single_char_xor_in_file("IN/challenge_4.txt"))
