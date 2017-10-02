#!/usr/bin/python3

import sys
import csv

# Abrimos el fichero .csv y declaramos operador y operando1
with open(sys.argv[1], newline='') as f:
    reader = csv.reader(f, delimiter=',')
    for operacion in reader:
        operador = operacion[0]
        operando1 = float(operacion[1])

# Declaramos las operaciones con sus respectivas excepciones
        if operador == 'suma':
            for operando in operacion[2:]:
                operando1 += float(operando)
        elif operador == 'resta':
            for operando in operacion[2:]:
                operando1 -= float(operando)
        elif operador == 'multiplica':
            for operando in operacion[2:]:
                operando1 *= float(operando)
        elif operador == 'divide':
            try:
                for operando in operacion[2:]:
                    operando1 /= float(operando)
            except ZeroDivisionError:
                sys.exit("Division by zero is not allowed")
        else:
            sys.exit('Error: Sólo puedes operar suma, resta, multipli y divi.')

print(operador, operando1)
