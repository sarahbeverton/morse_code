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

#def decode_bits(bits):
#    return


def decode_morse(morse):
    """
    decoded = ''
    for char in morse:
        if char != ' ':
            decoded += MORSE_2_ASCII.get(char)
        else:
            decoded += ' '
    return decoded
    """
    '''
    morse_codes = morse.split()
    letters = []
    for morse_code in morse_codes:
        letters.append(MORSE_2_ASCII.get(morse_code))
    return ''.join(letters)
    '''
    
    morse_codes_init = re.split(r"([.-]+)\s", morse)
    print(morse_codes_init)
    morse_codes = list(filter(lambda x: x != "", morse_codes_init))
    print(morse_codes)
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
