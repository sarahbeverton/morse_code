#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'Sarah Beverton'


from morse_dict import MORSE_2_ASCII
import re
from itertools import groupby


def decode_bits(bits):
    group_lst = [''.join(g) for k, g in groupby(bits)]
    sorted_lst = sorted(group_lst, key=len)
    print(group_lst)
    print(sorted_lst)
    multiplier = len(sorted_lst[-1])//7
    print(multiplier)
    bits_list = []
    for num in group_lst:
        if len(num) >= multiplier:
            bits_list.append(num[:-(len(num) - len(num)//multiplier)])
        else:
            bits_list.append(num[:1])
    print(bits_list)
    morse_list = []
    for bit in bits_list:
        if bit == '1':
            morse_list.append(".")
        elif bit == '11' or bit == '111':
            morse_list.append("-")
        elif bit == '0':
            morse_list.append('')
        elif bit == '00':
            morse_list.append(' ')
        elif bit == '0000000':
            morse_list.append('   ')
    print(''.join(morse_list))
    return ''.join(morse_list)


def decode_morse(morse):
    morse_codes_init = re.split(r"([.-]+)\s", morse)
    morse_codes = list(filter(lambda x: x != "", morse_codes_init))
    letters = []
    for morse_code in morse_codes:
        if morse_code != '  ':
            letters.append(MORSE_2_ASCII.get(morse_code))
        else:
            letters.append(' ')
    return ''.join(letters)


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011" # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
