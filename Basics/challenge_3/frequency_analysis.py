#!/usr/bin/python
# coding: utf8

"""
The cryptopals crypto challenges
Challenge: Single-byte XOR cipher
url: https://cryptopals.com/sets/1/challenges/3
"""

import sys
import codecs
import collections
import string


def decode_hex_string(hex_string):
    """
    Decodes hex string
    """
    return codecs.encode(codecs.decode(hex_string, 'hex'))


def find_most_frequent_character(ciphertext):
    """
    Find and return the character with the maximum occurrences
    """
    return collections.Counter(ciphertext).most_common(1)[0][0]


def decipher_text(ciphertext, xor_key):
    """
    Recover the plaintext from the ciphertext
    """
    text = ""
    for i in ciphertext:
        text += chr(ord(i) ^ xor_key)
    return text.lower()


def find_key_from_frequent_characters(character):
    """
    Key = cipher_character xor character_in_clear
    We create a list of potential Keys for each character in frequent_character
    """
    frequent_characters = "etaoin shrdlu"
    keys = list()
    for i in frequent_characters:
        keys.append(ord(character) ^ ord(i))
    return keys


def score(word_list, language_dictionary):
    """
    Iterates on each word and try to find a match in a language dictionary.
    """
    number_of_match = sum(word in language_dictionary for word in word_list)
    return float(float(number_of_match) / float(len(word_list)))


if __name__ == '__main__':
    SOURCE_FILE = open(sys.argv[1], "r")
    CIPHER_TEXT = decode_hex_string(SOURCE_FILE.read().translate(None, ' \n'))
    MOST_FREQUENT_CHARACTER = find_most_frequent_character(CIPHER_TEXT)
    KEY_LIST = find_key_from_frequent_characters(MOST_FREQUENT_CHARACTER)
    BEST_SCORE = 0
    KEY = ""
    CLEAR_TEXT = ""
    ENGLISH_DICTIONARY = open("words.txt").read()
    for key_element in KEY_LIST:
        plaintext = decipher_text(CIPHER_TEXT, key_element)
        words = plaintext.split()
        current_key_score = score(words, ENGLISH_DICTIONARY)
        if BEST_SCORE < current_key_score:
            BEST_SCORE = current_key_score
            KEY = str(key_element)
            CLEAR_TEXT = plaintext
    print("Key: " + KEY + "\nplaintext: " + "\"" + CLEAR_TEXT + "\"")
    print('Score: %.2f/1' % BEST_SCORE)
