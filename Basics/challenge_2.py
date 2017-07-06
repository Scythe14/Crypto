#!/usr/bin/env python

if __name__ == '__main__':
    s1 = 0x1c0111001f010100061a024b53535009181c
    s2 = 0x686974207468652062756c6c277320657965

    print(hex(s1 ^ s2))
