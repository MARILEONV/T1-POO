# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 17:18:28 2021

@author: maril
"""
class EstructuraSelectivas:     
    def __init__(self):
        pass

#EJERCICIO 4
#ESTRUCTURA SELECTIVA SIMPLE      
    def calificación1 (self): 
        cal= float(input("Ingrese la calificación del examen: "))
        if cal>=7:
            print("La nota es {}, APROBADO" .format(cal))

 #EJERCICIO 5
#ESTRUCTURA SELECTIVA DOBLE          
    def calificación2(self):                           
        cal= float(input("Ingrese la calificación del examen: "))
        if cal >=7:
            print("La nota es {}, APROBADO" .format(cal))
        else:
            print("La nota es {}, REPROBADO" .format(cal))

#EJERCICIO 6
#ESTRUCTURA SELECTIVA DOBLE
    def sueldo(self):                           
        SInicial= float(input("Ingrese el sueldo inicial: "))
        if SInicial <= 600:
            NSueldo= SInicial+(SInicial*0.1)
            print("Su nuevo sueldo es {}" .format(NSueldo))
        else:
            NSueldo= SInicial
            print("Su sueldo sigue siendo {}" .format(NSueldo))

#EJERCICIO 7
#ESTRUCTURA SELECTIVA COMPUESTA     
    def pago(self):                             
        HTrab= int(input("Ingrese las horas que trabajó: "))
        PHora= float(input("Ingrese el pago de la hora normal: "))
        if HTrab > 40:
            HExtras= HTrab-40
            if HExtras > 8:
                HExtP= HExtras-8
                PHExtras= (PHora*2*8) + (PHora*3*HExtP)
            else:
                PHExtras= PHora*2*HExtras
            PTrab= PHora*40+PHExtras
        else:
            PTrab= PHora*HTrab
        print("El pago semanal por las horas trabajadas es {}" .format(PTrab))

#EJERCICIO 8
#ESTRUCTURA SELECTIVA COMPUESTA
    def NumMayor(self):                             
        Num1= int(input("Ingrese el primer número: "))
        Num2= int(input("Ingrese el segundo número: "))
        Num3= int(input("Ingrese el tercer número: "))
        if Num1> Num2 and Num1> Num3:
            print("El número mayor es {}" .format(Num1))
        elif Num2> Num1 and Num2> Num3:
            print("El número mayor es {}" .format(Num2))
        else:
            print("El número mayor es {}" .format(Num3))

#EJERCICIO 9
#ESTRUCTURAS SELECTIVAS MÚLTIPLES
    def valores(self):                            
        Val1= int(input("Ingrese un número: "))
        Val2= int(input("Ingrese un valor: "))
        if Val1== 1:
            Result= 100*Val2
        elif Val1== 2:
            Result= 100**Val2
        elif Val1== 3:
            Result= 100/Val2
        else:
            Result= 0
        print("El resultado del número {} y el valor {} es de: {} ".format(Val1,Val2, Result))

#EJERCICIO 10
#EXPRESIONES LÓGICAS - USO DE "AND" "OR"
    def log1(self):                                
        Cal1= int(input("Ingrese la primera calificación: "))
        Cal2= int(input("Ingrese la segunda calificación: "))
        if Cal1 >=80 and Cal2>=80:
            print("La calificacion 1: {},la calificación 2:{} es ACEPTADO" .format(Cal1,Cal2))
        else:
            print("La calificacion 1: {},la calificación 2:{} es RECHAZADO" .format(Cal1,Cal2))


    def log2(self):
        Cal1= int(input("Ingrese la primera calificación: "))
        Cal2= int(input("Ingrese la segunda calificación: "))
        if Cal1 >=90 or Cal2>=90:
            print("La calificacion 1: {},la calificación 2:{} es ACEPTADO" .format(Cal1,Cal2))
        else:
            print("La calificacion 1: {},la calificación 2:{} es RECHAZADO" .format(Cal1,Cal2))


clase1= EstructuraSelectivas()
clase1.calificación1()
clase1.calificación2()
clase1.sueldo()
clase1.pago()
clase1.NumMayor()
clase1.valores()
clase1.log1()
clase1.log2()

