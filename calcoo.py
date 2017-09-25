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

#Llamamos a la calculadora segun se introduzca en la maquina de comandos
if __name__ == "__main__":
    objeto = Calculadora(int(sys.argv[1]), int(sys.argv[3]))
    if sys.argv[2] == 'suma':
       result = objeto.suma()
    elif sys.argv[2] == 'resta':
       result = objeto.resta()
    else:
        sys.exit('Operar solo enteros.')
