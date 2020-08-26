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
from itertools import groupby
import re


def decode_bits(bits):
    # group by character then sort by length of group
    group_lst = [''.join(g) for k, g in groupby(bits)]
    sorted_lst = sorted(group_lst, key=len)
    # find multiplier
    if len(sorted_lst[0]) == 1:
        multiplier = 1
    elif len(sorted_lst[-1]) == 2:
        multiplier = 2
    elif len(sorted_lst[-1]) == 3:
        multiplier = 3
    elif len(sorted_lst[-1]) == 5:
        multiplier = 5
    elif len(sorted_lst[-1]) % 7 == 0:
        multiplier = len(sorted_lst[-1])//7
    elif len(sorted_lst[-1]) % 3 == 0:
        multiplier = len(sorted_lst[-1])//3
    else:
        multiplier = 1
    # get rid of start and end 0's
    if(group_lst[0][0] == '0'):
        del group_lst[0]
    if(group_lst[-1][0] == '0'):
        del group_lst[-1]
    # create list of bits divided by multiplier
    bits_list = []
    for num in group_lst:
        if len(num) >= multiplier:
            if(multiplier == 1):
                bits_list.append(num)
            else:
                bits_list.append(num[:-(len(num) - len(num)//multiplier)])
        else:
            bits_list.append(num[:1])
    # translate bits to morse
    morse_list = []
    # if only one element in bits and all are 1's, then it is a dot
    pattern = re.compile("^[1]+$")
    if len(bits_list) == 1 and pattern.match(bits_list[0]):
        morse_list.append(".")
    elif multiplier >= 3:
        for bit in bits_list:
            if bit == '1':
                morse_list.append(".")
            elif bit == '11' or bit == '111':
                morse_list.append("-")
            elif bit == '0':
                morse_list.append('')
            elif bit == '00' or bit == '000':
                morse_list.append(' ')
            elif bit == '0000000':
                morse_list.append('   ')
    else:
        for bit in bits_list:
            if bit == '1' or bit == '11':
                morse_list.append(".")
            elif bit == '111':
                morse_list.append("-")
            elif bit == '0':
                morse_list.append('')
            elif bit == '00' or bit == '000':
                morse_list.append(' ')
            elif bit == '0000000':
                morse_list.append('   ')
    return ''.join(morse_list)


def decode_morse(morse):
    morse_codes = morse.split('   ')
    letters = []
    for morse_word in morse_codes:
        chars = morse_word.split(" ")
        for char in chars:
            for k, v in MORSE_2_ASCII.items():
                if char == k:
                    letters.append(v)
        letters.append(" ")
    return ''.join(letters).strip()


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
