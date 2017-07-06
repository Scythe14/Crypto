#!/usr/bin/python
# coding: utf8

"""
The cryptopals crypto challenges
Challenge: Single-byte XOR cipher
url: https://cryptopals.com/sets/1/challenges/3
"""

import sys


def tokenize(cipher_text):
    """
    Pack per byte
    for example: 1,b,... -> 1b,...
    """
    token_list = list()
    tmp_token = ""
    counter = 0
    for i in cipher_text:
        tmp_token += i
        if (counter % 2) != 0:
            token_list.append(int(tmp_token, 16))
            tmp_token = ""
        counter += 1
    return token_list


def find_most_frequent_token(cipher_token):
    """
    Find and return the token with the maximum occurrences
    """
    map_character = dict()
    for i in cipher_token:
        if i not in map_character.keys():
            map_character[i] = 1
        else:
            map_character[i] += 1
    return max(map_character.iterkeys(), key=(lambda key: map_character[key]))


def decipher_text(cipher_text, key):
    """
    Recover the plaintext from the cipher_text
    """
    plaintext = ""
    for i in cipher_text:
        plaintext += chr(i ^ key)
    return plaintext.lower()


def find_key_from_token(character):
    """
    Key = cipher_character xor character_in_clear
    We create a list of potential Keys for each character in frequent_character
    """
    frequent_character = "ETAOIN SHRDLU"
    keys = list()
    for i in frequent_character:
        keys.append(character ^ ord(i))
    return keys


def score(word_list, language_dictionary):
    """
    Iterates on each word and try to find a match in a language dictionary.
    """
    number_of_match = 0
    for word in word_list:
        if word in language_dictionary:
            number_of_match += 1
    return float(float(number_of_match) / float(len(word_list)))


if __name__ == '__main__':
    source_file = open(sys.argv[1], "r")
    tok_list = tokenize(source_file.read())
    most_frequent_token = find_most_frequent_token(tok_list)
    key_list = find_key_from_token(most_frequent_token)
    best_score = 0
    key = ""
    clear_text = ""
    english_dictionary = open("words.txt").read()
    for key_element in key_list:
        plaintext = decipher_text(tok_list, key_element)
        words = plaintext.split()
        current_key_score = score(words, english_dictionary)
        if best_score < current_key_score:
            best_score = current_key_score
            key = str(key_element)
            clear_text = plaintext
    print "Key: " + key + "\nplaintext: " + "\"" + clear_text + "\""
    print 'Score: %.2f/1' % best_score
