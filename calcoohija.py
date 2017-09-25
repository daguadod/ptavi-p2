#!/usr/bin/python3

import calcoo
import sys


class CalculadoraHija(calcoo.Calculadora):

    def multi(self):
        return self.valor1 * self.valor2
    
    def divi(self):
        return self.valor1 / self.valor2


if __name__ == "__main__":
    try:
        objetohijo = CalculadoraHija(int(sys.argv[1]), int(sys.argv[3]))
    except ValueError: 
        sys.exit("Error: Usar solo enteros.")

    if sys.argv[2] == 'suma':
       result = objetohijo.suma()
    elif sys.argv[2] == 'resta':
       result = objetohijo.resta()
    elif sys.argv[2] == 'multiplicacion':
        result = objetohijo.multi()
    else: 
        try:
            result = objetohijo.divi()
        except ZeroDivisionError:
            sys.exit("Dividiendo por 0") 

print(result)
