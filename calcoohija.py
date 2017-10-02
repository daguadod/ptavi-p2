#!/usr/bin/python3

import calcoo
import sys

#Declaramos que la clase viene de una clase madre "Calculadora"
class CalculadoraHija(calcoo.Calculadora):

#Operaciones de multiplicación y división 
    def multi(self):
        return self.valor1 * self.valor2
    
    def divi(self):
        return self.valor1 / self.valor2

if __name__ == "__main__":
    try:
        objetohijo = CalculadoraHija(float(sys.argv[1]), float(sys.argv[3]))
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == 'suma':
       result = objetohijo.suma()
    elif sys.argv[2] == 'resta':
       result = objetohijo.resta()
    elif sys.argv[2] == 'multiplica':
       result = objetohijo.multi()
    elif sys.argv[2] == 'divide':
        try:
            result = objetohijo.divi()
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed") 
    else:
        sys.exit('Error: Sólo puedes operar suma, resta, multiplicacion y division.')

print(result)
