# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 17:18:27 2021

@author: maril
"""

class EstructuraSecuenciales:      
    def __init__(self):
        pass
    
    #EJERCICIO 2

    def descuento (self):                   
        TCompra= float(input("Ingrese el total de la compra: "))
        Desc= TCompra*0.15
        VPagar= TCompra-Desc
        print("El total de la compra es {}, su valor a pagar es {}" .format(TCompra,VPagar))

    #EJERCICIO 3

    def sueldo(self):                  
        SalBas= float(input("Ingrese su salario base: "))
        Venta1= float(input("Ingrese el valor de su primera venta: "))
        Venta2= float(input("Ingrese el valor de su segunda venta: "))
        Venta3= float(input("Ingrese el valor de su tercera venta: "))
        TOTVentas= Venta1+Venta2+Venta3
        Com= TOTVentas*0.1
        TRec= SalBas+Com
        print("Su salario base es {}, mas las ventas realizadas {}, usted recibirá un total {}" .format(SalBas,TOTVentas,TRec))

clase1= EstructuraSecuenciales()
clase1.descuento()
clase1.sueldo() 