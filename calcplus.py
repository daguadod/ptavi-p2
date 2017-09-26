#/usr/bin/python3

import sys
import csv

with open(sys.argv[1], newline = '') as f:
    reader = csv.reader(f,delimiter = ',')
    for operacion in reader:
        operador = operacion[0]
        operando1 = int(operacion[1])

        if operador == 'suma':
            for operando in operacion[2:]:
                operando1 += int(operando)
        elif operador == 'resta':
            for operando in operacion[2:]:
                operando1 -= int(operando)
        elif operador == 'multiplicacion':
            for operando in operacion[2:]:
                operando1 *= int(operando)
        elif operador == 'division':
            try:
                for operando in operacion[2:]:
                    operando1 /= int(operando)
            except ZeroDivisionError:
                sys.exit("Division by zero is not allowed")
        else:
            sys.exit('Error: Sólo puedes operar suma, resta, multiplicacion y division.')

        print(operando1)
      
