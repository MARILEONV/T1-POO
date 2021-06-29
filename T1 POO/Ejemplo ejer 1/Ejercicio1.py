# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 15:10:33 2021

@author: maril
"""

class Clase:     
    def __init__(self):
        pass
    
    #EJERCICIO 1

    def ejemplo1(self):             
        Rad= float(input("Ingrese el radio del círculo: "))
        superf= 3.1416*(Rad**2)
        print("La superficie del círculo es {}" .format(superf))

clase1= Clase()
clase1.ejemplo1()
