# -*- coding: utf-8 -*-
# Implementation by Gilles Van Assche and Benoit Viguier, hereby denoted as "the implementers".
#
# For more information, feedback or questions, please refer to our website:
# https://keccak.team/
#
# To the extent possible under law, the implementers has waived all copyright
# and related or neighboring rights to the source code in this file.
# http://creativecommons.org/publicdomain/zero/1.0/

from __future__ import print_function

def outputHex(s):
    for i in range(len(s)):
        print("{0:02X}".format(s[i]), end=' ')
        if i % 16 == 15:
            print()
    print()
    print()