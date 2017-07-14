#!/usr/bin/env python


def hex_xor(s1, s2):
    """Challenge 2 - Hexadecimal xored"""
    return hex(s1 ^ s2)


print(hex_xor(0x1c0111001f010100061a024b53535009181c, 0x686974207468652062756c6c277320657965))