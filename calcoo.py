#!/usr/bin/python3

import sys

#Creamos la clase Calculadora
class Calculadora:

#definimos las variables y las operaciones de la Calculadora
    def __init__(self,valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

#Llamamos a la calculadora según se introduzca en la maquina de comandos
if __name__ == "__main__":
    try:
        objeto = Calculadora(float(sys.argv[1]), float(sys.argv[3]))
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == 'suma':
       result = objeto.suma()
    elif sys.argv[2] == 'resta':
       result = objeto.resta()
