#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


def plus(op1, op2):
    """ Function to sum the operands. Ops have to be ints """
    return op1 + op2


def minus(op1, op2):
    """ Function to substract the operands """
    return op1 - op2

if __name__ == "__main__":

    operando1, operando2 = int(sys.argv[1]), int(sys.argv[3])

    if sys.argv[2] == "suma":
        result = plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = minus(operando1, operando2)

    print(result)
