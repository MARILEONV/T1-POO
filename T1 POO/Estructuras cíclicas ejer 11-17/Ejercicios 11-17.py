# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 17:18:29 2021

@author: maril
"""

class EstructuraCiclicas:     
    def __init__(self):
        pass

#EJERCICIO 11
#ESTRUCTURAS FOR
    def suma1(self):                        
        i=1
        sum=0
        for i in range(100):
            sum= sum+i*i
            i+=1
        print("La suma de los 100 números es: {}" .format(sum))

#EJERCICIO 12
#ESTRUCTURAS WHILE - BUCLE CONTROLADO POR CONTADOR   
    def num1(self):       
        i=1
        while i<=100:
            print("Presentación de los números: {}" .format(i))
            i+=1
        return i

#EJERCICIO 13
#ESTRUCTURAS WHILE - BUCLE CONTROLADO POR CONDICIÓN
    def suma2(self):       
        suma=0
        product=1
        print("Desea continuar [S/N]:  ")
        respt= input().capitalize()
        while respt == "S":
            num= int(input("Ingrese un número: "))
            suma= suma+num
            product= product*num
            print("El total de la suma es: {}" .format(suma))
            print("El total del producto es: {}" .format(product))
            print("Desea continuar [S/N]:  ")
            respt=input().capitalize()

#EJERCICIO 14
#ESTRUCTURAS WHILE - BUCLE CONTROLADO POR CONDICIÓN
    def suma3(self):             
        suma=0
        product=1
        num= int(input("Ingrese un número: "))
        while num!=-1:
            suma= suma+num
            product= product*num
            print("El total de la suma es: {}" .format(suma))
            print("El total del producto es: {}" .format(product))
            num= int(input("Ingrese un número: "))

#EJERCICIO 15
#ESTRUCTURAS WHILE - BUCLE CONTROLADO POR BANDERAS O INTERRUPTORES
    def num2(self):             
        primo= True
        div=2
        num= int(input("Ingrese un número: "))
        while div<num and primo==True:
            rest= num%div
            if rest==0:
                primo= False
            div+=1
        if primo== True:
            print("El número {} es primo" .format(num))
        else:
            print("El número {} no es primo" .format(num))

#EJERCICIO 16
#ESTRUCTURAS REPEAT
    def num3(self):                          
        I=1
        ser=0
        num= int(input("Ingrese un número: "))
        band=True
        while band:
            if band ==True:
                ser= ser+(1/I)
                band= False
            else:
                ser= ser-(1/I)
                band= True
            I+=1
            if I>num:
                break
            print("El resultado de la serie es: {}" .format(ser))

#EJERCICIO 17
#BUCLES ANIDADOS
    def faltorial(self):                        
        num= int(input("Ingrese un número: "))
        fac=1
        for i in range(1, num+1):
            fac*=i
        print("El factorial del número {} es: {}" .format(num, fac))

clase1= EstructuraCiclicas()
clase1.suma1()
clase1.num1()
clase1.suma2()
clase1.suma3()
clase1.num2()
clase1.num3()
clase1.factorial() 
